"""Extract approximate breakdown voltage from an I-V CSV file.

Definition used here:
    breakdown voltage = first reverse-bias voltage where |I| exceeds threshold.

Expected CSV columns:
    voltage,current
"""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


def extract_breakdown_voltage(csv_path: Path, current_threshold: float = 1e-6) -> float | None:
    df = pd.read_csv(csv_path)
    reverse = df[df["voltage"] < 0].copy()
    reverse["abs_current"] = reverse["current"].abs()
    hit = reverse[reverse["abs_current"] >= current_threshold]
    if hit.empty:
        return None
    return float(hit.iloc[0]["voltage"])


def main() -> None:
    if len(sys.argv) not in {2, 3}:
        raise SystemExit("Usage: python extract_breakdown_voltage.py <iv_csv_file> [current_threshold]")

    csv_path = Path(sys.argv[1])
    threshold = float(sys.argv[2]) if len(sys.argv) == 3 else 1e-6
    bv = extract_breakdown_voltage(csv_path, threshold)

    if bv is None:
        print(f"No breakdown found for threshold={threshold:g} A")
    else:
        print(f"Approximate breakdown voltage: {bv:.4g} V")


if __name__ == "__main__":
    main()
