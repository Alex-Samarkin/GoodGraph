#!/usr/bin/env python3
"""«Правильный» Bland–Altman для раздела 5.19.

Что улучшено
------------
1. По X — среднее двух методов, по Y — разница.
2. Bias и 95 % LoA показаны линиями и подписаны.
3. Полный диапазон разниц −2,5…+2,5 ммоль/л.
4. Один цвет, полупрозрачные точки.
5. Единицы, n = 150, заголовок-вывод.
6. 85 мм, лёгкая сетка.

Выход: images/05_19_good_bland_altman.{svg,png}
Запуск: uv run python 05_charts/19_bland_altman/scripts/good_plot.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd

from goodgraph.palettes import ACCENT_VERMILLION, PRIMARY_BLUE
from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, figure_size, save_figure


def main() -> None:
    apply_style()

    df = pd.read_csv(DATA_DIR / "19_dataset.csv")
    lab = df["lab_glucose"].to_numpy()
    meter = df["meter_glucose"].to_numpy()
    mean = (lab + meter) / 2
    diff = lab - meter
    bias = float(diff.mean())
    loa = 1.96 * float(diff.std(ddof=1))
    low, high = bias - loa, bias + loa

    fig, ax = plt.subplots(
        figsize=figure_size("single", height_mm=72),
        layout="constrained",
    )
    fig.set_constrained_layout_pads(w_pad=0.04, h_pad=0.02)

    ax.scatter(mean, diff, s=14, color=PRIMARY_BLUE, alpha=0.45, linewidths=0, zorder=2)

    ax.axhline(0, color="#999999", linewidth=0.7, zorder=1)
    ax.axhline(bias, color="#333333", linewidth=1.1, zorder=3)
    ax.axhline(low, color=ACCENT_VERMILLION, linestyle=(0, (3, 2)), linewidth=0.9, zorder=3)
    ax.axhline(high, color=ACCENT_VERMILLION, linestyle=(0, (3, 2)), linewidth=0.9, zorder=3)

    bias_text = f"{bias:+.2f}".replace(".", ",")
    low_text = f"{low:.2f}".replace(".", ",")
    high_text = f"{high:+.2f}".replace(".", ",")
    ax.text(
        12.8,
        0.15,
        f"bias {bias_text}",
        fontsize=6.5,
        ha="right",
        color="#333333",
        bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.0},
    )
    ax.text(12.8, high + 0.10, f"LoA {low_text}…{high_text}", fontsize=6.5,
            ha="right", color=ACCENT_VERMILLION)

    ax.set_xlim(3, 13)
    ax.set_ylim(-2.5, 2.5)
    ax.set_xticks([3, 6, 9, 12])
    ax.set_yticks([-2, -1, 0, 1, 2])

    ax.set_xlabel("Среднее двух методов, ммоль/л")
    ax.set_ylabel("Разница (лаборатория − глюкометр), ммоль/л")
    ax.set_title(f"Средняя разница {bias_text} ммоль/л", loc="left", fontsize=9.5, pad=6)

    ax.text(
        0.02,
        0.97,
        f"n = {len(df)}; 95 % LoA",
        transform=ax.transAxes,
        fontsize=7,
        color="#333333",
        va="top",
    )

    ax.grid(axis="y", color="#E8E8E8", linewidth=0.6)
    ax.grid(axis="x", visible=False)

    save_figure(fig, "05_19_good_bland_altman", formats=("svg", "png"), dpi=600)

    print(f"Bias: {bias:+.2f}; LoA: {low:+.2f}…{high:+.2f}")


if __name__ == "__main__":
    main()
