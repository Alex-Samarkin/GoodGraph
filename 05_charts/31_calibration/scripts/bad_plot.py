#!/usr/bin/env python3
"""«Плохая» калибровка: без диагонали и CI."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd

from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, save_figure


def main() -> None:
    apply_style()
    df = pd.read_csv(DATA_DIR / "31_dataset.csv")
    df["bin"] = pd.qcut(df["predicted_risk"], 6, labels=False, duplicates="drop")
    grouped = df.groupby("bin").agg(pred=("predicted_risk", "mean"), obs=("outcome", "mean"))
    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    ax.plot(grouped["pred"], grouped["obs"], "o-", color="#D62728", markersize=8, linewidth=3)
    ax.set_xlim(0.2, 0.8)
    ax.set_ylim(0.2, 0.8)
    ax.grid(True, axis="both", color="#BDBDBD", linewidth=1.0)
    ax.set_axisbelow(True)
    ax.set_title("Калибровка", fontsize=18, fontweight="bold")
    ax.set_xlabel("Прогноз", fontsize=14)
    ax.set_ylabel("Наблюдение", fontsize=14)
    fig.tight_layout()
    save_figure(fig, "05_31_bad_calibration", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
