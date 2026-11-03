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
    (
        "Сравнение",
        "точка + 95 % ДИ (14)\nстолбцы (15)\nforest (16)\nslope (17)",
        "5.14–5.17",
        "#0072B2",
        "white",
    ),
    (
        "Распределение",
        "гистограмма (09)\nECDF (10)\nbox (11)\nviolin (12)\nstrip (13)",
        "5.09–5.13",
        "#009E73",
        "white",
    ),
    (
        "Связь",
        "scatter (05)\nhexbin (06)\ncontour (07)\nloess (08)",
        "5.05–5.08",
        "#E69F00",
        "#333333",
    ),
    (
        "Динамика",
        "линия (01)\nstep (02)\narea (03)\nsmall multiples (04)",
        "5.01–5.04",
        "#D55E00",
        "white",
    ),
    (
        "Состав",
        "stacked (20)\n100 % bar (21)\npie (22)\ntreemap (23)",
        "5.20–5.23",
        "#CC79A7",
        "#333333",
    ),
    (
        "Матрица",
        "heatmap (24)\nclustermap (25)\ncorr matrix (26)",
        "5.24–5.26",
        "#56B4E9",
        "#333333",
    ),
    (
        "Выживаемость",
        "Kaplan–Meier (27)\ncum. incidence (28)",
        "5.27–5.28",
        "#4D4D4D",
        "white",
    ),
    (
        "Диагностика",
        "ROC (29)\nPR-кривая (30)\ncalibration (31)",
        "5.29–5.31",
        "#F0E442",
        "#333333",
    ),
    (
        "Парные",
        "slope (17)\npaired dot (18)\nBland–Altman (19)",
        "5.17–5.19",
        "#0072B2",
        "white",
    ),
    (
        "Оценки",
        "forest (16)\ncaterpillar (32)\nfunnel (33)",
        "5.16, 5.32–5.33",
        "#4D4D4D",
        "white",
    ),
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
            fontsize=5.9,
            color="#333333",
            linespacing=1.15,
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
