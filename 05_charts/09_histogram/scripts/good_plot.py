#!/usr/bin/env python3
"""«Правильная» гистограмма для раздела 5.09.

Что улучшено
------------
1. Ширина бина 2 нг/мл: видна форма распределения и правый хвост.
2. Полный диапазон 0–70 нг/мл.
3. Один цвет, белые края, без 3D и теней.
4. Порог дефицита 20 нг/мл и медиана 23,4 нг/мл.
5. Подпись n и доли дефицита; заголовок-вывод.
6. Единицы, лёгкая сетка только по Y, 85 мм.

Выход: images/05_09_good_histogram.{svg,png}
Запуск: uv run python 05_charts/09_histogram/scripts/good_plot.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from goodgraph.palettes import ACCENT_VERMILLION, PRIMARY_BLUE
from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, figure_size, save_figure


def main() -> None:
    apply_style()

    df = pd.read_csv(DATA_DIR / "09_dataset.csv")
    values = df["vitamin_d_ng_ml"].to_numpy()
    median = float(np.median(values))
    share = float((values < 20).mean() * 100)

    fig, ax = plt.subplots(
        figsize=figure_size("single", height_mm=72),
        layout="constrained",
    )
    fig.set_constrained_layout_pads(w_pad=0.04, h_pad=0.02)

    bins = np.arange(0, 72, 2)
    counts, _, _ = ax.hist(
        values,
        bins=bins,
        color=PRIMARY_BLUE,
        alpha=0.80,
        edgecolor="white",
        linewidth=0.4,
        zorder=2,
    )
    ymax = counts.max() * 1.15
    ax.set_ylim(0, ymax)

    ax.axvline(
        20,
        color=ACCENT_VERMILLION,
        linestyle=(0, (3, 2)),
        linewidth=0.9,
        zorder=3,
    )
    ax.axvline(
        median,
        color="#333333",
        linestyle=(0, (1, 2)),
        linewidth=0.9,
        zorder=3,
    )

    ax.text(
        20.8,
        ymax * 0.93,
        "порог 20",
        fontsize=6.5,
        color=ACCENT_VERMILLION,
        va="top",
    )
    median_text = f"{median:.1f}".replace(".", ",")
    ax.text(
        median + 1.2,
        ymax * 0.80,
        f"медиана {median_text}",
        fontsize=6.5,
        color="#333333",
        va="top",
    )
    ax.text(
        68,
        ymax * 0.96,
        f"n = {len(df)}",
        fontsize=7,
        color="#333333",
        ha="right",
        va="top",
    )

    ax.set_xlim(0, 70)
    ax.set_xticks([0, 20, 40, 60])
    ax.set_xlabel("25(OH)D, нг/мл")
    ax.set_ylabel("Пациенты")
    ax.set_title(f"Дефицит витамина D у {share:.0f} %", loc="left", fontsize=9.5, pad=6)

    ax.grid(axis="y", color="#E8E8E8", linewidth=0.6)
    ax.grid(axis="x", visible=False)

    save_figure(fig, "05_09_good_histogram", formats=("svg", "png"), dpi=600)

    print(f"n = {len(df)}, медиана = {median:.1f}, дефицит = {share:.1f} %")


if __name__ == "__main__":
    main()
