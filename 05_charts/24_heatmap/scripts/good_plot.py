#!/usr/bin/env python3
"""«Правильная» heatmap."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd

from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, figure_size, save_figure


def main() -> None:
    apply_style(font_size=7)
    df = pd.read_csv(DATA_DIR / "24_dataset.csv")
    pivot = df.pivot(index="department", columns="hour", values="wait_min")
    pivot = pivot.loc[pivot.mean(axis=1).sort_values(ascending=False).index]

    fig, ax = plt.subplots(figsize=figure_size("single", height_mm=70), layout="constrained")
    image = ax.imshow(pivot, cmap="cividis", aspect="auto", vmin=0)
    ax.set_xticks(range(len(pivot.columns)))
    ax.set_xticklabels([f"{h}:00" for h in pivot.columns])
    ax.set_yticks(range(len(pivot.index)))
    ax.set_yticklabels(pivot.index)

    for i in range(len(pivot.index)):
        for j in range(len(pivot.columns)):
            value = pivot.iloc[i, j]
            ax.text(j, i, f"{value:.0f}", ha="center", va="center",
                    fontsize=6, color="white" if value < 45 else "#333333")

    cbar = fig.colorbar(image, ax=ax, fraction=0.05, pad=0.02, shrink=0.85)
    cbar.set_label("Минуты", fontsize=7)
    cbar.ax.tick_params(labelsize=6.5)
    ax.set_xlabel("Час")
    ax.set_title("Хирургия — самое долгое ожидание", loc="left", fontsize=9.5, pad=6)
    ax.grid(False)
    save_figure(fig, "05_24_good_heatmap", formats=("svg", "png"), dpi=600)


if __name__ == "__main__":
    main()
