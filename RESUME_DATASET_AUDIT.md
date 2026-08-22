# Completion point — annual REC dataset audit

Completed on 2026-08-21. No annual audit process remains active.

## Frozen evidence contract

- Dataset contract: `2023-q15-v1.9`
- Simulator source root: `/home/tiago/dev/Simulator/citylearn`
- Simulator source SHA-256: `988001c92e14264dca4e20bb2cc0ed3f04efaf33769e344accc0d8f0096d71e7`
- Runtime attestation SHA-256: `70d2f77c7208a32e3cecdd02e411de0b461f040efc1d5cc5646df664e927ec52`

## Completed evidence

- Structural/cross-family audit: 1,817 checks passed.
- Diversity audit: passed, zero findings and zero individually infeasible EV sessions.
- Scientific audit: `ready_with_declared_scope`; two declared medium limitations only.
- Deterministic regeneration: byte-identical manifests for 25/47/84/260 files.
- Official smoke: 9 schemas, 6,048 regular transitions, 120 topology events/effects, and 31,565 causal-price checks passed.
- Simulator regression: 457 tests passed, 18 warnings.
- Algorithms regression: 1,392 tests passed, 108 warnings.
- Annual BAU/RBC Smart campaign: 18/18 runs completed; 630,720 control transitions and 630,738 state points.
- Aggregate annual validation: `pass`, 18 runs, zero findings.
- Final annual-audit targeted regression: 10 tests passed.
- All annual runs: zero residual total/per-phase electrical violation and zero EV energy-accounting shortfall.

## Authoritative outputs

- Root audit: `/home/tiago/dev/Simulator/results/raw/annual_rec_suite_final_audit_2026-08-21.md`
- Aggregate validation: `/home/tiago/dev/Algorithms/runs/annual_rec_baseline_audit_v1_9_asset_count_attested_full_summary/aggregate_validation.json`
- Annual interpretation: `/home/tiago/dev/Algorithms/runs/annual_rec_baseline_audit_v1_9_asset_count_attested_full_summary/annual_analysis.md`
- Machine-readable interpretation: `/home/tiago/dev/Algorithms/runs/annual_rec_baseline_audit_v1_9_asset_count_attested_full_summary/annual_analysis.json`

## Scientific boundary

The suite is ready for controlled benchmarking of the thesis objectives. It is not a statistically fitted sample of Portuguese REC populations and does not implement feeder voltage, reactive power, impedance, protection, or power-flow physics. Any experiment requiring those stronger claims must use a new versioned dataset contract rather than silently changing `2023-q15-v1.9`.
