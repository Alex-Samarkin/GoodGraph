#!/usr/bin/env python3
"""«Плохая» heatmap."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd

from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, save_figure


def main() -> None:
    apply_style()
    df = pd.read_csv(DATA_DIR / "24_dataset.csv")
    pivot = df.pivot(index="department", columns="hour", values="wait_min")

    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    image = ax.imshow(pivot, cmap="jet", aspect="auto")
    ax.set_xticks(range(len(pivot.columns)))
    ax.set_xticklabels(pivot.columns, rotation=30)
    ax.set_yticks(range(len(pivot.index)))
    ax.set_yticklabels(pivot.index)
    ax.set_title("Время ожидания", fontsize=18, fontweight="bold")
    fig.colorbar(image, ax=ax)
    fig.tight_layout()
    save_figure(fig, "05_24_bad_heatmap", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
