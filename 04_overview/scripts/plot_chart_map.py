#!/usr/bin/env python3
"""Карта семейств научных графиков.

Схема для раздела 4: вопрос → семейство → примеры → номер раздела 5.
Это не график данных, поэтому CSV не нужен: карточки заданы явно.

Выход: images/04_chart_map.{svg,png}
Запуск: uv run python 04_overview/scripts/plot_chart_map.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

from goodgraph.style import apply_style, figure_size, save_figure

# Заголовок, примеры, номер раздела, цвет.
CARDS = [
    ("Сравнение", "точка + 95 % ДИ\nстолбцы, полосы", "5.03 · 5.05", "#0072B2", "white"),
    ("Распределение", "гистограмма, box\nviolin, strip", "5.04", "#009E73", "white"),
    ("Связь", "scatter, hexbin\ncontour, loess", "5.02", "#E69F00", "#333333"),
    ("Динамика", "линия\nsmall multiples", "5.01 · 5.09", "#D55E00", "white"),
    ("Состав", "stacked bar\n100 % bar; pie", "5.03 · 5.11", "#CC79A7", "#333333"),
    ("Матрица", "heatmap\nclustermap", "5.08", "#56B4E9", "#333333"),
    ("Выживаемость", "Kaplan–Meier\nчисло рисков", "5.06", "#4D4D4D", "white"),
    ("Диагностика", "ROC, PR\nпорог, prevalence", "5.07", "#F0E442", "#333333"),
]


def main() -> None:
    apply_style(font_size=7)

    fig = plt.figure(figsize=figure_size("double", height_mm=95))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 2)
    ax.axis("off")

    ax.text(
        2.0,
        1.94,
        "Карта видов графиков",
        ha="center",
        va="center",
        fontsize=10,
        fontweight="bold",
        color="#333333",
    )

    width, height = 0.94, 0.84
    for index, (title, examples, section, color, text_color) in enumerate(CARDS):
        col = index % 4
        row = index // 4
        x = 0.03 + col * 0.99
        y = 0.03 + (1 - row) * 0.93

        ax.add_patch(
            FancyBboxPatch(
                (x, y),
                width,
                height,
                boxstyle="round,pad=0.008,rounding_size=0.03",
                linewidth=0.6,
                edgecolor=color,
                facecolor="#FAFAFA",
            )
        )
        ax.add_patch(
            Rectangle(
                (x + 0.006, y + height - 0.19),
                width - 0.012,
                0.184,
                facecolor=color,
                edgecolor="none",
            )
        )
        ax.text(
            x + width / 2,
            y + height - 0.095,
            title,
            ha="center",
            va="center",
            fontsize=7.5,
            fontweight="bold",
            color=text_color,
        )
        ax.text(
            x + width / 2,
            y + 0.36,
            examples,
            ha="center",
            va="center",
            fontsize=6.5,
            color="#333333",
            linespacing=1.25,
        )
        ax.text(
            x + width / 2,
            y + 0.11,
            section,
            ha="center",
            va="center",
            fontsize=5.8,
            color="#777777",
        )

    save_figure(fig, "04_chart_map", formats=("svg", "png"), dpi=600)


if __name__ == "__main__":
    main()
