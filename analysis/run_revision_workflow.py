"""Run the IEEE Access analysis."""

from __future__ import annotations

import argparse
import subprocess
import sys
from collections.abc import Sequence
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


def workflow_commands(icc_workers: int | None = None) -> list[list[str]]:
    python = sys.executable
    commands = [
        [python, "analysis/audit_observed_runs.py"],
        [python, "analysis/audit_topology_instances.py"],
        [python, "analysis/derive_run_outcomes.py"],
        [python, "analysis/compute_corrected_dispersion.py"],
        [python, "analysis/balanced_sensitivity.py"],
        [python, "analysis/bootstrap_dispersion_tables.py"],
        [python, "analysis/fit_two_part_models.py"],
    ]
    icc = [python, "analysis/icc_by_blockchain.py"]
    if icc_workers is not None:
        icc.extend(["--workers", str(icc_workers)])
    commands.extend(
        [
            icc,
            [python, "analysis/audit_gafam_trace.py"],
            [python, "analysis/workload_catalog.py"],
            [python, "analysis/plot_run_level_deviations.py"],
            [python, "analysis/audit_campaign_structure.py"],
        ]
    )
    return commands


def run_workflow(icc_workers: int | None = None) -> None:
    for command in workflow_commands(icc_workers):
        print(f"Running {command[1]}", flush=True)
        subprocess.run(command, cwd=REPOSITORY_ROOT, check=True)


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--icc-workers",
        type=int,
        default=None,
        help="Explicit worker count for the full 1,000-repetition ICC bootstrap.",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    run_workflow(args.icc_workers)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
