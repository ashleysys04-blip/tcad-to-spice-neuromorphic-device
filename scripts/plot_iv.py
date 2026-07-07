"""Plot I-V curves exported from TCAD or SPICE.

Expected CSV format:
    voltage,current
    0.0,1e-12
    0.1,2e-12

Usage:
    python plot_iv.py data/processed/example_iv.csv
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python plot_iv.py <iv_csv_file>")

    csv_path = Path(sys.argv[1])
    if not csv_path.exists():
        raise FileNotFoundError(f"File not found: {csv_path}")

    df = pd.read_csv(csv_path)
    required = {"voltage", "current"}
    if not required.issubset(df.columns):
        raise ValueError(f"CSV must contain columns: {required}")

    plt.figure()
    plt.semilogy(df["voltage"], df["current"].abs())
    plt.xlabel("Voltage (V)")
    plt.ylabel("|Current| (A)")
    plt.title("I-V Curve")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
