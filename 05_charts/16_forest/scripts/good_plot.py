#!/usr/bin/env python3
"""«Правильный» forest plot для раздела 5.16.

Что улучшено
------------
1. 95 % доверительные интервалы для каждого OR.
2. Логарифмическая ось OR: 0,3–2,0.
3. Линия «нет эффекта» OR = 1.
4. Размер квадрата пропорционален числу пациентов.
5. Общая оценка — ромб внизу.
6. Справа — OR (95 % ДИ); слева — подгруппы.
7. Один цвет, лёгкая сетка, 170 мм.

Выход: images/05_16_good_forest.{svg,png}
Запуск: uv run python 05_charts/16_forest/scripts/good_plot.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Polygon
from matplotlib.ticker import NullLocator

from goodgraph.palettes import ACCENT_VERMILLION, PRIMARY_BLUE
from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, figure_size, save_figure


def odds_ratio(a: int, n1: int, c: int, n2: int) -> tuple[float, float, float]:
    b = n1 - a
    d = n2 - c
    odds = (a / b) / (c / d)
    se = np.sqrt(1 / a + 1 / b + 1 / c + 1 / d)
    return odds, np.exp(np.log(odds) - 1.96 * se), np.exp(np.log(odds) + 1.96 * se)


def fmt(value: float) -> str:
    return f"{value:.2f}".replace(".", ",")


def main() -> None:
    apply_style(font_size=7.5)

    df = pd.read_csv(DATA_DIR / "16_dataset.csv")
    sub = df[df["subgroup"] != "Все пациенты"].reset_index(drop=True)
    overall = df[df["subgroup"] == "Все пациенты"].iloc[0]

    fig, ax = plt.subplots(figsize=figure_size("double", height_mm=90))
    fig.subplots_adjust(left=0.25, right=0.72, top=0.86, bottom=0.16)

    y = np.arange(len(sub))[::-1]
    for yi, (_, row) in zip(y, sub.iterrows(), strict=True):
        odds, low, high = odds_ratio(
            int(row["events_treatment"]),
            int(row["n_treatment"]),
            int(row["events_control"]),
            int(row["n_control"]),
        )
        ax.hlines(yi, low, high, color=PRIMARY_BLUE, linewidth=1.3, zorder=2)
        size = (row["n_treatment"] + row["n_control"]) / 3.0
        ax.scatter(odds, yi, s=size, color=PRIMARY_BLUE, edgecolors="white",
                   linewidths=0.5, zorder=3)
        ax.text(2.05, yi, f"{fmt(odds)} ({fmt(low)}–{fmt(high)})",
                fontsize=7, va="center", clip_on=False)

    odds, low, high = odds_ratio(
        int(overall["events_treatment"]),
        int(overall["n_treatment"]),
        int(overall["events_control"]),
        int(overall["n_control"]),
    )
    diamond = Polygon(
        [[low, -1], [odds, -1.28], [high, -1], [odds, -0.72]],
        closed=True,
        facecolor=ACCENT_VERMILLION,
        edgecolor=ACCENT_VERMILLION,
        zorder=4,
    )
    ax.add_patch(diamond)
    ax.text(2.05, -1, f"{fmt(odds)} ({fmt(low)}–{fmt(high)})",
            fontsize=7, va="center", color=ACCENT_VERMILLION,
            fontweight="bold", clip_on=False)

    ax.axvline(1, color="#777777", linestyle=(0, (3, 2)), linewidth=0.8, zorder=1)
    ax.set_xscale("log")
    ax.xaxis.set_minor_locator(NullLocator())
    ax.set_xlim(0.3, 2.0)
    ax.set_xticks([0.3, 0.5, 0.7, 1.0, 1.5, 2.0])
    ax.set_xticklabels(["0,3", "0,5", "0,7", "1", "1,5", "2"])

    labels = list(sub["subgroup"]) + ["Все пациенты"]
    ax.set_yticks(list(y) + [-1])
    ax.set_yticklabels(labels)
    ax.set_ylim(-1.8, len(sub) - 0.2)

    ax.set_xlabel("OR (лог. шкала)")
    ax.set_title("Эффект лечения по подгруппам", loc="left", fontsize=10, pad=8)
    ax.text(2.05, len(sub) - 0.35, "OR (95 % ДИ)", fontsize=7,
            fontweight="bold", va="bottom", clip_on=False)

    ax.grid(axis="x", color="#E8E8E8", linewidth=0.6)
    ax.grid(axis="y", visible=False)

    save_figure(fig, "05_16_good_forest", formats=("svg", "png"), dpi=600)


if __name__ == "__main__":
    main()
