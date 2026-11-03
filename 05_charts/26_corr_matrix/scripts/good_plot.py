#!/usr/bin/env python3
"""«Правильная» корреляционная матрица."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, save_figure


def main() -> None:
    apply_style(font_size=7)
    corr = pd.read_csv(DATA_DIR / "26_dataset.csv").corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))

    fig, ax = plt.subplots(figsize=(100 / 25.4, 85 / 25.4))
    sns.heatmap(
        corr,
        mask=mask,
        cmap="RdBu_r",
        vmin=-1,
        vmax=1,
        center=0,
        annot=True,
        fmt=".2f",
        annot_kws={"fontsize": 5.5},
        square=True,
        linewidths=0.4,
        linecolor="white",
        cbar_kws={"shrink": 0.75, "label": "r"},
        ax=ax,
    )
    ax.set_title("Возраст, САД и eGFR связаны", loc="left", fontsize=9, pad=6)
    ax.tick_params(axis="x", rotation=45)
    ax.tick_params(axis="y", rotation=0)
    save_figure(fig, "05_26_good_corr_matrix", formats=("svg", "png"), dpi=600)


if __name__ == "__main__":
    main()
