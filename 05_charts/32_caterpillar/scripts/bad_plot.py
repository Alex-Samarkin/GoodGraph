#!/usr/bin/env python3
"""«Плохой» caterpillar: без сортировки и CI."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, save_figure


def main() -> None:
    apply_style()
    df = pd.read_csv(DATA_DIR / "32_dataset.csv")
    rates = df["events"] / df["n"] * 100
    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    ax.scatter(np.arange(len(df)), rates, s=70, color="#D62728", edgecolors="black")
    ax.set_ylim(0, 15)
    ax.grid(True, axis="both", color="#BDBDBD", linewidth=1.0)
    ax.set_axisbelow(True)
    ax.set_title("Осложнения по центрам", fontsize=18, fontweight="bold")
    ax.set_xlabel("Центры", fontsize=14)
    ax.set_ylabel("%", fontsize=14)
    fig.tight_layout()
    save_figure(fig, "05_32_bad_caterpillar", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
