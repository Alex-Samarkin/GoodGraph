#!/usr/bin/env python3
"""«Правильный» treemap."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
import squarify

from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, figure_size, save_figure

COLORS = ["#084C61", "#1B6A7A", "#2E8893", "#41A6AC", "#54C4C4", "#67E2DC"]


def main() -> None:
    apply_style(font_size=7)
    df = pd.read_csv(DATA_DIR / "23_dataset.csv").sort_values("cost_mln_rub", ascending=False)
    labels = [
        f"{program}\n{cost} млн"
        for program, cost in zip(df["program"], df["cost_mln_rub"], strict=True)
    ]

    fig, ax = plt.subplots(figsize=figure_size("single", height_mm=80), layout="constrained")
    squarify.plot(
        sizes=df["cost_mln_rub"],
        label=labels,
        color=COLORS,
        ax=ax,
        pad=True,
        text_kwargs={"fontsize": 7, "color": "white"},
    )
    ax.set_title("Кардиология и онкология — 50 % затрат", loc="left", fontsize=9.5, pad=8)
    ax.axis("off")
    save_figure(fig, "05_23_good_treemap", formats=("svg", "png"), dpi=600)


if __name__ == "__main__":
    main()
