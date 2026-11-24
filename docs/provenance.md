# Data sources

Zenodo archives the [ACM DLT dataset](https://doi.org/10.5281/zenodo.21381461)
and the [IEEE Access reproducibility package](https://doi.org/10.5281/zenodo.24394925).
Use the [dataset DOI](https://doi.org/10.5281/zenodo.17681717) to cite the collection.

## Network inputs

The experiments used [Lilith](https://doi.org/10.5281/zenodo.11409100). The raw
label `diablo` identifies the 2023 AWS RTT trace included in
[`inputs/topologies`](../inputs/topologies). The selected runs took place from
21 April 2024 to 8 August 2025.

The topology folder contains the trace and ten reference XML files generated
with [Lilith's topology script][topology] and the included trace. Each of the
five topology modes has a 10- and a 40-validator instance. The generator uses
seed 443. The run-level CSV reports the topology mode and network size.

## PayPal and Gaming workload inputs

Lilith's [runner][runner] selects the [PayPal][paypal] and [Gaming][dota]
profiles. The PayPal workload records about 200 offered transactions per second
in the selected runs. For Gaming, the recorded median offered load is
13,328.2 transactions per second. This differs from the schedule in the
released Gaming profile, so the analysis uses the rates recorded in the CSV.

## GAFAM workload input

The [GAFAM workload][gafam] selected by the Lilith runner is included under
[`inputs/workloads`](../inputs/workloads). Diablo interpolates between the
specified times and sending rates over 300 seconds. The run-level CSV
identifies these executions by the label `gafam`.

[topology]: https://github.com/vindipe/lilith/blob/dd1d457c6079661b158f601cdf70817cbe2a5f2a/scripts/gen_topo.py
[runner]: https://github.com/vindipe/lilith/blob/dd1d457c6079661b158f601cdf70817cbe2a5f2a/kollaps/examples/diablo/primary/minion.sh#L49-L81
[paypal]: https://github.com/vindipe/lilith/blob/dd1d457c6079661b158f601cdf70817cbe2a5f2a/kollaps/examples/diablo/primary/fixes/workload-paypal.yaml
[dota]: https://github.com/vindipe/lilith/blob/dd1d457c6079661b158f601cdf70817cbe2a5f2a/kollaps/examples/diablo/primary/fixes/workload-dota.yaml
[gafam]: https://github.com/vindipe/lilith/blob/dd1d457c6079661b158f601cdf70817cbe2a5f2a/kollaps/examples/diablo/primary/fixes/workload-gafam-long.yaml
