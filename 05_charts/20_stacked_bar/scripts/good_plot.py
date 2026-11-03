#!/usr/bin/env python3
"""«Правильный» stacked bar для раздела 5.20.

Что улучшено
------------
1. Горизонтальные столбцы, сортировка по общему числу.
2. Нулевая база, полный масштаб.
3. Палитра Okabe–Ito, без 3D и теней.
4. Значения и общее число подписаны.
5. Легенда сверху, единицы, n.
6. Заголовок-вывод, 85 мм.

Выход: images/05_20_good_stacked_bar.{svg,png}
Запуск: uv run python 05_charts/20_stacked_bar/scripts/good_plot.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, figure_size, save_figure

OUTCOMES = ["выписан", "переведён", "умер"]
COLORS = ["#0072B2", "#E69F00", "#D55E00"]


def main() -> None:
    apply_style(font_size=7)

    df = pd.read_csv(DATA_DIR / "20_dataset.csv")
    pivot = df.pivot(index="department", columns="outcome", values="patients")[OUTCOMES]
    pivot["total"] = pivot.sum(axis=1)
    pivot = pivot.sort_values("total")

    fig, ax = plt.subplots(
        figsize=figure_size("single", height_mm=80),
        layout="constrained",
    )
    fig.set_constrained_layout_pads(w_pad=0.04, h_pad=0.04)

    left = np.zeros(len(pivot))
    for outcome, color in zip(OUTCOMES, COLORS, strict=True):
        bars = ax.barh(
            pivot.index,
            pivot[outcome],
            left=left,
            color=color,
            height=0.62,
            label=outcome,
            zorder=2,
        )
        for bar in bars:
            width = bar.get_width()
            if width >= 90:
                ax.text(
                    bar.get_x() + width / 2,
                    bar.get_y() + bar.get_height() / 2,
                    f"{int(width)}",
                    ha="center",
                    va="center",
                    fontsize=6,
                    color="white" if outcome != "переведён" else "#333333",
                )
        left += pivot[outcome].to_numpy()

    for y, total in enumerate(pivot["total"]):
        ax.text(total + 15, y, f"{int(total)}", va="center", fontsize=7, color="#333333")

    ax.set_xlim(0, 1150)
    ax.set_xticks([0, 500, 1000])
    ax.set_xlabel("Пациенты")
    ax.set_title("В ОРИТ 44 % пациентов переведены", loc="left", fontsize=9.5, pad=18)
    ax.text(
        0.99, 0.01, f"всего {int(pivot['total'].sum())} пациентов",
        transform=ax.transAxes, ha="right", va="bottom", fontsize=6.5, color="#555555",
    )

    ax.legend(
        loc="lower left",
        bbox_to_anchor=(0.0, 1.02),
        ncol=3,
        frameon=False,
        fontsize=6.5,
        handlelength=1.2,
        columnspacing=1.0,
    )
    ax.grid(axis="x", color="#E8E8E8", linewidth=0.6)
    ax.grid(axis="y", visible=False)

    save_figure(fig, "05_20_good_stacked_bar", formats=("svg", "png"), dpi=600)


if __name__ == "__main__":
    main()
