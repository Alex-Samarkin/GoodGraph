#!/usr/bin/env python3
"""«Правильный» bar chart для раздела 5.15.

Что улучшено
------------
1. Горизонтальные столбцы: длинные подписи читаются.
2. Сортировка по величине.
3. Нулевая база: ось X начинается с 0.
4. Значения подписаны прямо у столбцов.
5. Один цвет, без теней и 3D.
6. Единицы, общее число, заголовок-вывод, 85 мм.

Выход: images/05_15_good_bar.{svg,png}
Запуск: uv run python 05_charts/15_bar/scripts/good_plot.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd

from goodgraph.palettes import PRIMARY_BLUE
from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, figure_size, save_figure


def main() -> None:
    apply_style()

    df = pd.read_csv(DATA_DIR / "15_dataset.csv").sort_values("admissions")
    fig, ax = plt.subplots(
        figsize=figure_size("single", height_mm=75),
        layout="constrained",
    )
    fig.set_constrained_layout_pads(w_pad=0.04, h_pad=0.02)

    bars = ax.barh(
        df["department"],
        df["admissions"],
        color=PRIMARY_BLUE,
        height=0.62,
        zorder=2,
    )

    for bar in bars:
        value = int(bar.get_width())
        ax.text(
            value + 25,
            bar.get_y() + bar.get_height() / 2,
            f"{value:,}".replace(",", " "),
            va="center",
            fontsize=7,
            color="#333333",
        )

    ax.set_xlim(0, 1400)
    ax.set_xticks([0, 500, 1000, 1400])
    ax.set_xlabel("Госпитализаций за год")
    ax.set_title("Терапия — крупнейшее отделение", loc="left", fontsize=9.5, pad=6)

    ax.text(
        0.99,
        0.02,
        f"всего {df['admissions'].sum():,}".replace(",", " ") + " госпитализаций",
        transform=ax.transAxes,
        ha="right",
        va="bottom",
        fontsize=6.5,
        color="#555555",
    )

    ax.grid(axis="x", color="#E8E8E8", linewidth=0.6)
    ax.grid(axis="y", visible=False)

    save_figure(fig, "05_15_good_bar", formats=("svg", "png"), dpi=600)


if __name__ == "__main__":
    main()
