#!/usr/bin/env python3
"""«Плохая» корреляционная матрица."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd

from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, save_figure


def main() -> None:
    apply_style()
    corr = pd.read_csv(DATA_DIR / "26_dataset.csv").corr()
    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    image = ax.imshow(corr, cmap="jet", vmin=-1, vmax=1)
    ax.set_xticks(range(len(corr)))
    ax.set_xticklabels(corr.columns, rotation=45, ha="right")
    ax.set_yticks(range(len(corr)))
    ax.set_yticklabels(corr.columns)
    ax.set_title("Корреляции", fontsize=18, fontweight="bold")
    fig.colorbar(image, ax=ax)
    fig.tight_layout()
    save_figure(fig, "05_26_bad_corr_matrix", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
