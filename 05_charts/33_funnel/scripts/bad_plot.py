#!/usr/bin/env python3
"""«Плохой» funnel: без воронки и pooled-эффекта."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd

from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, save_figure


def main() -> None:
    apply_style()
    df = pd.read_csv(DATA_DIR / "33_dataset.csv")
    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    ax.scatter(df["log_or"], df["se"], s=70, color="#D62728", edgecolors="black")
    ax.invert_yaxis()
    ax.grid(True, axis="both", color="#BDBDBD", linewidth=1.0)
    ax.set_axisbelow(True)
    ax.set_title("Исследования", fontsize=18, fontweight="bold")
    ax.set_xlabel("Эффект", fontsize=14)
    ax.set_ylabel("SE", fontsize=14)
    fig.tight_layout()
    save_figure(fig, "05_33_bad_funnel", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
