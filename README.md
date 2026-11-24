# Network-Controlled Blockchain Benchmarking Dataset and Analysis

[![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17681717.svg)](https://doi.org/10.5281/zenodo.17681717)

This repository contains the measurements, analysis code, tables, and figures
for two studies of blockchain performance under controlled network conditions.

- [The Impact of Network Topology on Performance Metrics and Energy Consumption for Blockchains: Towards Repeatable Benchmarking](https://doi.org/10.1145/3828757) · ACM DLT, 2026
- [Experimental Repeatability and Performance Predictability in Network-Controlled Blockchain Evaluation](https://doi.org/10.1109/ACCESS.2026.3756802) · IEEE Access, 2026

## Data

| File | Contents |
| --- | --- |
| [Run-level CSV](dataset/reproducibility-runs.csv) | 4,105 recorded executions, with transaction counts and throughput, confirmation latency, energy, and network measurements. [Column definitions](docs/run_level_data_dictionary.md) |
| [Aggregate CSV](dataset/reproducibility-dataset.csv) | 300 configurations and 50 columns of descriptive statistics. [Column definitions](docs/data_dictionary.md) |

The main IEEE Access analysis selects 4,080 observed executions across
300 configurations, with 9 to 26 runs per configuration. The configurations
span Algorand, Diem, Ethereum Clique, Quorum IBFT, and Solana, five network
topologies, six workloads, and deployments with 10 or 40 validators.

The analysis writes [derived outcomes and metric eligibility flags](docs/derived_outcome_data_dictionary.md)
to a separate CSV. The [methodology](docs/methodology.md) documents the filters,
run counts, dispersion measures, and statistical models. [Provenance](docs/provenance.md)
records the archive versions and the sources of the workload and topology inputs.

## Reproduce the analysis

Use Python 3.12 and install the pinned dependencies.

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 analysis/run_revision_workflow.py
```

Use `--icc-workers N` to select the number of workers for the ICC bootstrap.

- [Figures and analysis outputs](outputs/revision)
- [LaTeX tables](paper_tables)
- [Topology and workload inputs](inputs)

The earlier aggregation and plots can be regenerated with
`python3 analysis/plot_reproducibility.py`. To rerun the original experiments,
follow the installation and batch execution instructions for
[Lilith](https://doi.org/10.5281/zenodo.11409100), including its `multi-run.sh` launcher.

## License and citation

The data, code, and documentation are distributed under [CC BY 4.0](LICENSE).
Cite the [Zenodo dataset](https://doi.org/10.5281/zenodo.17681717) and the article
relevant to your use. See [CITATION.cff](CITATION.cff) for the creator names and DOIs.
