# Analysis methods

## Run selection

The IEEE Access analysis reads [the run-level CSV](../dataset/reproducibility-runs.csv)
and selects the runs with `dataset=diablo`, `link_strategy=hop`,
`secondaries=10`, `cores=8`, `ram=16`, and `dynamic=0`. These conditions
select 4,080 observations across 300 combinations of blockchain, topology,
workload and validator-set size. Each combination has 9 to 26 observations.

The CSV field `hash` identifies a collection batch and `run` identifies a
run within that batch. The analysis groups by the experimental configuration.
The earlier three-workload subset covers GAFAM, PayPal and VISA.

## Transaction outcomes

A run can record at least one commit, record submissions with zero commits,
or record zero submissions. The analysis classifies these outcomes from the
transaction counters. See the [derived data dictionary](derived_outcome_data_dictionary.md)
for the rules and the fields written by the analysis.

Throughput and confirmation latency are assessed on runs with commits and
usable measurements. Seven such runs have throughput stored as `0.0` at the
precision of the export. They count as runs with commits, but their throughput
is excluded from statistics that require a point measurement. Diagrams and
models for energy use the runs with commits, while the descriptive energy
tables also cover all observed runs.

## Variability and statistical models

For each configuration and metric, the analysis reports the interquartile
range, sample standard deviation and deviations from the configuration mean.
The figures show deviations in the original units and as a percentage of that
mean. The thresholds and fitted models are described in the
[IEEE Access article](https://doi.org/10.1109/ACCESS.2026.3756802).

Within-configuration bootstrap samples quantify uncertainty. A separate
sensitivity analysis selects nine observations per configuration before
applying the metric eligibility rules. Logistic regression examines which
runs record a commit. Factorial models with robust covariance examine the
performance measures among runs with usable observations. Intraclass
correlation coefficients on log-scale measurements compare variability
between and within configurations for each blockchain.

## Files produced by the analysis

- [Transaction outcomes](../outputs/revision/m2_outcomes)
- [Dispersion statistics](../outputs/revision/m3_dispersion) and
  [bootstrap intervals](../outputs/revision/m4_bootstrap)
- [Statistical models](../outputs/revision/statistical_models) and
  [intraclass correlations](../outputs/revision/icc_by_blockchain)
- [Figures](../outputs/revision/m1_figures) and [tables](../paper_tables)

The [ACM DLT article](https://doi.org/10.1145/3828757) describes the analysis
behind the [aggregate CSV](../dataset/reproducibility-dataset.csv).
