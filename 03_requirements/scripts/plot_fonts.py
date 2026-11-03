#!/usr/bin/env python3
"""Образец кеглей: как один и тот же текст выглядит при 85 мм ширины.

Схема для раздела 3. Размеры в точках — реальные: рисунок спроектирован
в конечном размере 85 мм, поэтому 6 pt здесь действительно 6 pt, а не
«6 pt, умноженные на масштаб слайда».

Выход: images/03_fonts.{svg,png}
Запуск: uv run python 03_requirements/scripts/plot_fonts.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

from goodgraph.style import apply_style, figure_size, save_figure

SIZES = [6, 7, 8, 9, 10, 12]
SAMPLE = "САД 128/82 · HbA1c 7,4 %"


def main() -> None:
    apply_style(font_size=8)

    fig = plt.figure(figsize=figure_size("single", height_mm=75))
    fig.text(
        0.04,
        0.95,
        "Кегли в конечном размере (85 мм)",
        fontsize=8,
        fontweight="bold",
        va="top",
    )
    fig.text(
        0.04,
        0.89,
        "Liberation Sans",
        fontsize=7,
        color="#666666",
        va="top",
    )

    y_positions = [0.78, 0.67, 0.56, 0.45, 0.34, 0.23]
    for size, y in zip(SIZES, y_positions, strict=True):
        color = "#B22222" if size < 7 else "#333333"
        fig.text(
            0.04,
            y,
            f"{size} pt — {SAMPLE}",
            fontsize=size,
            color=color,
            va="center",
        )
        fig.add_artist(
            Line2D(
                [0.04, 0.96],
                [y - 0.035, y - 0.035],
                color="#E6E6E6",
                linewidth=0.5,
            )
        )

    fig.text(
        0.04,
        0.06,
        "6 pt — ниже практического минимума; 7–10 pt — рабочий диапазон",
        fontsize=6.5,
        color="#666666",
        va="bottom",
    )

    save_figure(fig, "03_fonts", formats=("svg", "png"), dpi=600)


if __name__ == "__main__":
    main()
