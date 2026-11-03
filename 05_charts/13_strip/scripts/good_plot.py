#!/usr/bin/env python3
"""«Правильный» strip plot для раздела 5.13.

Что улучшено
------------
1. Jitter по X: все 30 точек в группе видны отдельно.
2. Один цвет, полупрозрачные точки.
3. Полный диапазон 0–100 мм.
4. Медиана отмечена горизонтальной линией.
5. Единицы, n, заголовок-вывод.
6. Лёгкая сетка только по Y, 85 мм.

Выход: images/05_13_good_strip.{svg,png}
Запуск: uv run python 05_charts/13_strip/scripts/good_plot.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from goodgraph.palettes import PRIMARY_BLUE
from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, figure_size, save_figure

GROUPS = ["НПВС", "опиоид", "комбинация"]


def main() -> None:
    apply_style()

    df = pd.read_csv(DATA_DIR / "13_dataset.csv")
    rng = np.random.default_rng(31)

    fig, ax = plt.subplots(
        figsize=figure_size("single", height_mm=75),
        layout="constrained",
    )
    fig.set_constrained_layout_pads(w_pad=0.04, h_pad=0.02)

    for position, group in enumerate(GROUPS, start=1):
        values = df.loc[df["analgesia"] == group, "vas_mm"].to_numpy()
        jitter = rng.normal(0.0, 0.09, len(values))
        ax.scatter(
            position + jitter,
            values,
            s=18,
            color=PRIMARY_BLUE,
            alpha=0.65,
            linewidths=0,
            zorder=3,
        )
        median = float(np.median(values))
        ax.hlines(
            median,
            position - 0.18,
            position + 0.18,
            color="#333333",
            linewidth=1.5,
            zorder=4,
        )

    ax.text(
        0.02,
        0.97,
        f"n = {len(df) // len(GROUPS)} в каждой группе",
        transform=ax.transAxes,
        fontsize=7,
        color="#333333",
        va="top",
    )

    ax.set_xlim(0.5, 3.5)
    ax.set_ylim(0, 100)
    ax.set_xticks([1, 2, 3])
    ax.set_xticklabels(GROUPS)
    ax.set_yticks([0, 20, 40, 60, 80, 100])

    ax.set_xlabel("Схема обезболивания")
    ax.set_ylabel("ВАШ, мм")
    ax.set_title("Комбинация снижает боль сильнее", loc="left", fontsize=9.5, pad=6)

    ax.grid(axis="y", color="#E8E8E8", linewidth=0.6)
    ax.grid(axis="x", visible=False)

    save_figure(fig, "05_13_good_strip", formats=("svg", "png"), dpi=600)


if __name__ == "__main__":
    main()
