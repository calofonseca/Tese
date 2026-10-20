"""Plot archived scenario inputs; this script does not execute a controller."""
from pathlib import Path
import hashlib
import json

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

HERE = Path(__file__).parent
SOURCE = Path('/home/tiago/dev/Simulator')
DATA = SOURCE / 'data/datasets/rec_pt_2023_core_30_v2'
SESSIONS = SOURCE / 'docs/portugal_rec_native/dataset_description/sessions.csv'
N = 70176

plt.rcParams.update({
    'font.family': 'DejaVu Sans', 'font.size': 9,
    'axes.spines.top': False, 'axes.spines.right': False,
    'axes.edgecolor': '#78909c', 'axes.labelcolor': '#233a46',
    'text.color': '#233a46', 'xtick.color': '#536872',
    'ytick.color': '#536872', 'pdf.fonttype': 42,
})

sources = {}
energy = np.zeros((N, 2), dtype=float)
for file in sorted((DATA / 'timeseries').glob('*.parquet')):
    values = pd.read_parquet(file, columns=['non_shiftable_load', 'solar_generation'])
    assert len(values) == N
    energy += values.to_numpy(dtype=float)
    sources[str(file)] = hashlib.sha256(file.read_bytes()).hexdigest()

sessions = pd.read_csv(SESSIONS)
sessions = sessions.loc[sessions.family == 'Core-30']
sources[str(SESSIONS)] = hashlib.sha256(SESSIONS.read_bytes()).hexdigest()
presence = {}
for name, mask in [('Residential', sessions.category == 'residential'),
                   ('Service', sessions.category != 'residential')]:
    delta = np.zeros(N + 1, dtype=int)
    for visit in sessions.loc[mask].itertuples():
        start, stop = max(int(visit.arrival), 0), min(int(visit.departure), N)
        assert 0 <= start <= stop <= N
        delta[start] += 1
        delta[stop] -= 1
    presence[name] = np.cumsum(delta[:-1])

index = pd.date_range('2023-01-01', periods=N, freq='15min', tz='UTC').tz_convert('Europe/Lisbon')
frame = pd.DataFrame(energy / 0.25, index=index, columns=['Demand', 'PV'])
for key, values in presence.items():
    frame[key] = values
frame['quarter'] = index.hour * 4 + index.minute // 15
seasons = [('Winter', [12, 1, 2]), ('Summer', [6, 7, 8])]
fig, axes = plt.subplots(2, 2, figsize=(6.6, 4.6), sharex=True, sharey='row',
                         gridspec_kw={'height_ratios': [1.15, 1]}, layout='constrained')
profiles = []
summary = {}
for col, (season, months) in enumerate(seasons):
    selected = frame[(index.year == 2024) & (index.dayofweek < 5) & index.month.isin(months)]
    mean = selected.groupby('quarter')[['Demand', 'PV', 'Residential', 'Service']].mean()
    assert len(mean) == 96
    out = mean.copy()
    out['season'] = season
    out['local_hour'] = mean.index / 4
    profiles.append(out.reset_index())
    x = np.arange(97) / 4
    for key, colour, style in [('Demand', '#508ab9', '-'), ('PV', '#76a95d', '--')]:
        y = np.r_[mean[key].to_numpy(), mean[key].iloc[0]]
        axes[0, col].plot(x, y, color=colour, linestyle=style, linewidth=1.8,
                          label='Non-shiftable demand' if key == 'Demand' else 'PV production')
    for key, colour, style in [('Residential', '#508ab9', '-'), ('Service', '#a27baf', '--')]:
        y = np.r_[mean[key].to_numpy(), mean[key].iloc[0]]
        axes[1, col].plot(x, y, color=colour, linestyle=style, linewidth=1.8, label=key)
    axes[0, col].set_title(season, loc='left', fontweight='bold')
    axes[1, col].set_xlabel('Local time (Europe/Lisbon)')
    summary[season] = {
        'days': int(len(selected) / 96),
        'mean_daily_input_kwh': selected[['Demand', 'PV']].sum().div(4 * len(selected) / 96).to_dict(),
        'peak_hour': {k: float(mean[k].idxmax() / 4) for k in mean.columns},
        'mean_connected_at_12h': mean.loc[48, ['Residential', 'Service']].to_dict(),
        'mean_connected_at_20h': mean.loc[80, ['Residential', 'Service']].to_dict(),
    }
for ax in axes.flat:
    ax.set_xlim(0, 24)
    ax.set_xticks([0, 6, 12, 18, 24], ['00:00', '06:00', '12:00', '18:00', '24:00'])
    ax.set_ylim(bottom=0)
    ax.grid(axis='y', alpha=.18)
axes[0, 0].set_ylabel('Mean input power (kW)')
axes[1, 0].set_ylabel('Mean connected vehicles')
axes[0, 0].legend(loc='upper left', frameon=False, fontsize=8)
axes[1, 0].legend(loc='upper right', frameon=False, fontsize=8)
fig.savefig(HERE / 'simulator-portugal-daily.pdf', bbox_inches='tight')
plt.close(fig)
pd.concat(profiles, ignore_index=True).to_csv(HERE / 'simulator-portugal-daily-profiles.csv', index=False)
(HERE / 'simulator-portugal-daily-sources.json').write_text(json.dumps({
    'edition': 'portugal-native-2023-2024-v3.1',
    'scope': 'Core-30 static base inputs and scheduled vehicle presence; no controller execution',
    'selection': 'All Monday-Friday intervals in calendar year 2024, DJF and JJA; public holidays are retained',
    'units': 'Input energy is converted to interval-average kW at 900 s; presence uses [arrival, departure)',
    'aggregation': 'Arithmetic mean by Lisbon local quarter-hour; the 24:00 point repeats the 00:00 mean',
    'sources': sources, 'summary': summary,
}, indent=2))
print(json.dumps(summary, indent=2))
