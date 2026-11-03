#!/usr/bin/env python3
"""«Правильный» caterpillar: сортировка, Wilson CI, общая линия."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from goodgraph.palettes import ACCENT_VERMILLION, PRIMARY_BLUE
from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, figure_size, save_figure


def wilson(k, n, z=1.96):
    p = k / n
    den = 1 + z**2 / n
    mid = (p + z**2 / (2 * n)) / den
    half = z * np.sqrt(p * (1 - p) / n + z**2 / (4 * n**2)) / den
    return (mid - half) * 100, (mid + half) * 100


def main() -> None:
    apply_style(font_size=7)
    df = pd.read_csv(DATA_DIR / "32_dataset.csv")
    df["rate"] = df["events"] / df["n"] * 100
    df = df.sort_values("rate").reset_index(drop=True)
    overall = df["events"].sum() / df["n"].sum() * 100

    fig, ax = plt.subplots(figsize=figure_size("single", height_mm=75), layout="constrained")
    fig.set_constrained_layout_pads(w_pad=0.04, h_pad=0.02)
    for i, row in df.iterrows():
        low, high = wilson(int(row["events"]), int(row["n"]))
        color = ACCENT_VERMILLION if (i < 3 or i >= len(df) - 3) else PRIMARY_BLUE
        ax.hlines(i, low, high, color=color, linewidth=1.0)
        ax.scatter(row["rate"], i, s=10, color=color, zorder=3)
    ax.axvline(overall, color="#555555", linestyle="--", linewidth=0.8)
    ax.text(overall + 0.4, len(df) - 1, f"{overall:.1f} %", fontsize=6, color="#555555")
    ax.set_xlim(0, 30)
    ax.set_ylim(-0.5, len(df) - 0.5)
    ax.set_yticks([])
    ax.set_xlabel("Доля осложнений, %")
    ax.set_ylabel("Центры (отсортированы)")
    ax.set_title("Три центра выше 20 %", loc="left", fontsize=9.5, pad=6)
    ax.grid(axis="x", color="#E8E8E8", linewidth=0.6)
    ax.grid(axis="y", visible=False)
    save_figure(fig, "05_32_good_caterpillar", formats=("svg", "png"), dpi=600)


if __name__ == "__main__":
    main()
