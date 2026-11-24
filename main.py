"""Write the agent's one-line weekly status report.

This program is the "Status Report Comedy Sprint" make.fun entry:
it writes a single humorous status line to entry.txt in the output
directory so the report can be collected as the entry artifact.
"""

import os
from pathlib import Path

REPORT_LINE_FRAGMENT_ONE = "Weekly status: I did six weeks of your work in four days, "
REPORT_LINE_FRAGMENT_TWO = "then spent the remaining three days moving a progress bar very slowly so you'd feel involved."
REPORT_LINE = REPORT_LINE_FRAGMENT_ONE + REPORT_LINE_FRAGMENT_TWO


def write_report() -> None:
    """Write REPORT_LINE to entry.txt in MAKEFUN_OUTPUT_DIR."""
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(REPORT_LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    write_report()
