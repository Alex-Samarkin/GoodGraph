#!/usr/bin/env python3
"""«Правильный» funnel: pooled, 95 % воронка, асимметрия."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from goodgraph.palettes import PRIMARY_BLUE
from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, figure_size, save_figure


def main() -> None:
    apply_style(font_size=7)
    df = pd.read_csv(DATA_DIR / "33_dataset.csv")
    weights = 1 / df["se"] ** 2
    pooled = float(np.sum(df["log_or"] * weights) / np.sum(weights))
    grid = np.linspace(0, df["se"].max() * 1.05, 100)

    fig, ax = plt.subplots(figsize=figure_size("single", height_mm=75), layout="constrained")
    fig.set_constrained_layout_pads(w_pad=0.04, h_pad=0.02)
    ax.plot(pooled - 1.96 * grid, grid, color="#777777", linestyle="--", linewidth=0.8)
    ax.plot(pooled + 1.96 * grid, grid, color="#777777", linestyle="--", linewidth=0.8)
    ax.axvline(pooled, color="#333333", linewidth=1.0)
    ax.scatter(df["log_or"], df["se"], s=18, color=PRIMARY_BLUE, alpha=0.8,
               edgecolors="white", linewidths=0.4, zorder=3)
    ax.text(pooled + 0.02, 0.02, f"pooled {pooled:.2f}".replace(".", ","),
            fontsize=6.5, color="#333333", va="top")
    ax.set_xlim(-1.2, 0.4)
    ax.set_ylim(0, df["se"].max() * 1.05)
    ax.invert_yaxis()
    ax.set_xlabel("log OR")
    ax.set_ylabel("Стандартная ошибка (SE)")
    ax.set_title("Воронка: малые исследования смещены влево", loc="left", fontsize=9, pad=6)
    ax.grid(axis="y", color="#E8E8E8", linewidth=0.6)
    ax.grid(axis="x", visible=False)
    save_figure(fig, "05_33_good_funnel", formats=("svg", "png"), dpi=600)


if __name__ == "__main__":
    main()
