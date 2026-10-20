"""Thesis figures from the archived Portugal input tables; no control execution.
Run --plots with the Simulator Python environment, --architecture with reportlab.
"""
from pathlib import Path
import sys,json,hashlib
HERE=Path(__file__).parent
SOURCE=Path('/home/tiago/dev/Simulator')

def architecture():
 from build_energaize_lifecycle import Diagram,controller,INK,BLUE,GREEN,PURPLE,GOLD,PALEBLUE,PALEORANGE,YELLOW
 d=Diagram('simulator-environment-architecture-revised.pdf',760,660)
 def icon(method,x,y,scale):
  d.c.saveState();d.c.translate(x,y);d.c.scale(scale,scale);getattr(d,method)(0,0);d.c.restoreState()
 def battery(x,y):
  d.rect(x-15,y-24,30,48,'#E8F2E2',GREEN,4,1.5);d.rect(x-5,y+24,10,4,GREEN,GREEN,1,1)
  for yy in [-13,0,13]:d.rect(x-10,y+yy-3,20,7,GREEN,GREEN,0,.5)
 def solar(x,y):
  d.polygon([(x-28,y-16),(x+24,y-16),(x+32,y+13),(x-20,y+13)],PALEBLUE,BLUE,1.5)
  for yy in [-6,4]:d.line([(x-26+yy/4,y+yy),(x+27+yy/4,y+yy)],BLUE,.8)
  d.line([(x-3,y-16),(x-3,y-29)],INK,2);d.line([(x-16,y-29),(x+12,y-29)],INK,2)
 def pylon(x,y):
  d.line([(x-15,y-22),(x,y+28),(x+15,y-22)],INK,2)
  for yy,ww in [(15,30),(4,25),(-7,20)]:d.line([(x-ww,y+yy),(x+ww,y+yy)],INK,2)
  d.line([(x-10,y-8),(x+7,y+8),(x-4,y+15)],INK,1.3)
 d.text(380,635,'CityLearn v3',24,True)
 d.text(380,611,'Each community uses its own scenario data and event streams',15)
 d.rect(16,536,262,52,PALEBLUE,BLUE,9,1.5);icon('document',42,562,.38)
 d.text(169,568,'Demand, weather and prices',14,True);d.text(169,548,'Time series, units and clock',13)
 d.rect(482,536,262,52,'#F1E7F4',PURPLE,9,1.5);d.text(613,568,'Membership, assets and failures',14,True);d.text(613,548,'Time-stamped scenario events',13)
 pylon(380,556);d.text(380,521,'Grid exchange / DR',13,True)
 for cx in [194,566]:
  d.arrow([(380,507),(cx,507),(cx,487)],GOLD,2)
 d.text(380,488,'One common clock',13,color=INK)
 for x,num in [(16,'1'),(388,'N')]:
  d.rect(x,112,356,363,YELLOW,GOLD,15,1.7)
  d.text(x+178,449,'Community '+num,20,True)
  d.text(x+178,425,'Buildings and their resources',14)
  # Two buildings remain distinct behind the local sharing interface.
  for xx in [x+96,x+260]:icon('house',xx,334,.75)
  d.text(x+96,298,'Building 1',13,True);d.text(x+260,298,'Building n',13,True)
  d.line([(x+96,383),(x+96,399),(x+260,399),(x+260,383)],GREEN,2)
  d.text(x+178,405,'Local energy sharing',12.5,color=GREEN)
  solar(x+63,265);battery(x+138,258);icon('charger',x+239,260,.63)
  d.rect(x+282,238,38,43,'#FFFFFF',BLUE,4,1.4);d.circle(x+301,256,11,PALEBLUE,BLUE,1.2)
  d.text(x+63,223,'PV',12);d.text(x+138,223,'Storage',12);d.text(x+239,223,'Charging',12);d.text(x+301,223,'Cycles',12)
  for left,mid,right in [(25,96,173),(190,260,340)]:
   controller(d,x+mid-41,139,82,50)
   d.arrow([(x+left,290),(x+left,171),(x+mid-45,171)],BLUE,1.4)
   d.arrow([(x+mid+45,154),(x+right,154),(x+right,282)],PURPLE,1.4)
  d.text(x+178,122,'Local controller interfaces',13,True)
  d.text(x+88,203,'Observations',12,color=BLUE)
  d.text(x+285,203,'Actions',12,color=PURPLE)
 # The header names per-community scenario inputs; gold arrows show grid/DR.
 d.text(147,520,'Per-community inputs',11.5,color=BLUE)
 d.text(613,520,'Per-community events',11.5,color=PURPLE)
 d.rect(16,18,728,66,'#E8F2E2',GREEN,10,1.5);icon('database',55,51,.45)
 d.text(423,61,'Local and combined evaluation',17,True)
 d.text(423,36,'Observations  /  requested and applied actions  /  services  /  KPIs',13.5)
 for cx in [194,566]:d.arrow([(cx,112),(cx,86)],GREEN,1.8)
 d.done()

def plots():
 import pandas as pd
 import numpy as np
 import matplotlib
 matplotlib.use('Agg')
 import matplotlib.pyplot as plt
 from matplotlib.lines import Line2D
 plt.rcParams.update({'font.family':'DejaVu Sans','font.size':8.5,'axes.spines.top':False,'axes.spines.right':False,'axes.edgecolor':'#78909c','axes.labelcolor':'#233a46','text.color':'#233a46','xtick.color':'#536872','ytick.color':'#536872','pdf.fonttype':42})
 tables=SOURCE/'docs/portugal_rec_native/dataset_description';families=['Core-4','Core-15','Core-30','Premium-100'];dirs=['micro_4','core_15','core_30','premium_100'];col=['#508ab9','#76a95d','#a27baf','#d6a02d']
 fig,axs=plt.subplots(2,2,figsize=(6.6,4.9),constrained_layout=True)
 index=pd.date_range('2023-01-01',periods=70176,freq='15min',tz='UTC');provenance={}
 for ax,f,folder in zip(axs.flat,families,dirs):
  agg=np.zeros((70176,2));files=sorted((SOURCE/f'data/datasets/rec_pt_2023_{folder}_v2/timeseries').glob('*.parquet'))
  for p in files:
   a=pd.read_parquet(p,columns=['non_shiftable_load','solar_generation']);agg+=a.to_numpy();provenance[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
  frame=pd.DataFrame(agg,index=index,columns=['Demand','PV']);monthly=frame.resample('MS').sum();monthly=monthly.div(monthly.index.days_in_month,axis=0)/1000
  for year,ls in [(2023,'--'),(2024,'-')]:
   for typ,c in [('Demand','#508ab9'),('PV','#76a95d')]:
    ar=monthly.loc[str(year),typ];ax.plot(range(1,13),ar,linestyle=ls,color=c,lw=1.5,marker='o' if typ=='Demand' else '^',markevery=2,markersize=2.8)
  ax.set_title(f,loc='left',weight='bold');ax.set_xticks([1,3,5,7,9,11],['Jan','Mar','May','Jul','Sep','Nov']);ax.set_ylabel('Daily-average energy (MWh)');ax.set_ylim(bottom=0);ax.grid(axis='y',alpha=.18)
 fig.legend(handles=[Line2D([0],[0],color='#508ab9',marker='o',markersize=4,label='Demand'),Line2D([0],[0],color='#76a95d',marker='^',markersize=4,label='PV'),Line2D([0],[0],color='#536872',ls='--',label='2023'),Line2D([0],[0],color='#536872',label='2024')],loc='outside lower center',ncol=4,frameon=False)
 fig.savefig(HERE/'simulator-portugal-seasonal.pdf',bbox_inches='tight');plt.close(fig)
 frame=pd.read_csv(tables/'annual_member_energy.csv');fig,axs=plt.subplots(2,2,figsize=(6.6,4.6),constrained_layout=True)
 for ax,f in zip(axs.flat,families):
  a=frame[(frame.family==f)&(frame.year==2024)]
  for cat,color,marker in [('residential','#508ab9','o'),('service','#d6a02d','s')]:
   z=a[(a.category=='residential') if cat=='residential' else (a.category!='residential')]
   ax.scatter(z.load_kwh/1000,z.pv_kwh/1000,c=color,marker=marker,s=24,edgecolor='white',lw=.35,label=cat.title(),alpha=.8)
  m=max(a.load_kwh.max(),a.pv_kwh.max())/1000*1.08;ax.plot([0,m],[0,m],ls=':',color='#82949c',lw=1);ax.set_xlim(-.03*m,m);ax.set_ylim(-.03*m,m);ax.set_title(f,loc='left',weight='bold');ax.set_xlabel('Non-shiftable demand (MWh)');ax.set_ylabel('PV production (MWh)');ax.grid(alpha=.12)
 fig.legend(*axs.flat[-1].get_legend_handles_labels(),loc='outside lower center',ncol=2,frameon=False);fig.savefig(HERE/'simulator-portugal-member-energy.pdf',bbox_inches='tight');plt.close(fig)
 sessions=pd.read_csv(tables/'sessions.csv');sessions=sessions[~sessions.left_censored & ~sessions.right_censored];cycles=pd.read_csv(tables/'cycles.csv')
 fig,axs=plt.subplots(1,2,figsize=(6.6,3.2),constrained_layout=True)
 for ax,data,field,label,factor in [(axs[0],sessions,'target_soc','Departure target (%)',100),(axs[1],cycles,'start_slack_h','Admissible start-window slack (h)',1)]:
  values=[data.loc[data.family==f,field].dropna()*factor for f in families];bp=ax.boxplot(values,vert=False,patch_artist=True,showfliers=False,medianprops={'color':'#233a46','linewidth':1.4})
  for patch,color in zip(bp['boxes'],col):patch.set_facecolor(color);patch.set_alpha(.45)
  ax.set_yticks(range(1,5),families);ax.set_xlabel(label);ax.grid(axis='x',alpha=.15);ax.invert_yaxis()
 fig.savefig(HERE/'simulator-portugal-services.pdf',bbox_inches='tight');plt.close(fig)
 (HERE/'simulator-dataset-figure-sources.json').write_text(json.dumps({'edition':'portugal-native-2023-2024-v3.1','scope':'Descriptive inputs only; no simulator execution','monthly_sources':provenance,'tables':{f:hashlib.sha256((tables/f).read_bytes()).hexdigest() for f in ['annual_member_energy.csv','sessions.csv','cycles.csv']}},indent=2))

if __name__=='__main__':
 if '--architecture' in sys.argv:architecture()
 if '--plots' in sys.argv:plots()
