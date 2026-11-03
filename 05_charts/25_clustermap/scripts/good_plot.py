#!/usr/bin/env python3
"""«Правильный» clustermap: z-score, кластеризация, diverging."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import pandas as pd
import seaborn as sns

from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, save_figure


def main() -> None:
    apply_style(font_size=7)
    df = pd.read_csv(DATA_DIR / "25_dataset.csv").set_index("gene")
    grid = sns.clustermap(
        df,
        z_score=0,
        cmap="RdBu_r",
        center=0,
        figsize=(120 / 25.4, 100 / 25.4),
        dendrogram_ratio=0.15,
        cbar_pos=(0.02, 0.82, 0.03, 0.14),
        linewidths=0.3,
        linecolor="white",
        xticklabels=True,
        yticklabels=True,
    )
    grid.ax_heatmap.set_xlabel("Пациенты")
    grid.ax_heatmap.set_ylabel("Гены")
    grid.fig.suptitle("Два кластера экспрессии", x=0.02, ha="left", fontsize=9.5)
    save_figure(grid.fig, "05_25_good_clustermap", formats=("svg", "png"), dpi=600)


if __name__ == "__main__":
    main()
