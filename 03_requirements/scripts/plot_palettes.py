#!/usr/bin/env python3
"""Три типа палитр: качественная, последовательная, дивергентная.

Схема для раздела 3. Это не график данных: набор CSV здесь не нужен,
цвета заданы явно. Смысл рисунка — показать, что палитра выбирается
под задачу, а не «по вкусу».

Выход: images/03_palettes.{svg,png}
Запуск: uv run python 03_requirements/scripts/plot_palettes.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from goodgraph.palettes import OKABE_ITO, TOL_BRIGHT
from goodgraph.style import apply_style, figure_size, save_figure

# Качественные палитры: 7 цветов, без чёрного (чёрный — для текста и осей).
QUALITATIVE = {
    "Okabe–Ito": list(OKABE_ITO.values())[:-1],
    "Paul Tol bright": TOL_BRIGHT,
}

# Последовательные: воспринимаются равномерно, читаются при дальтонизме.
SEQUENTIAL = ["viridis", "cividis"]

# Дивергентные: два полюса и нейтральная середина.
DIVERGING = ["RdBu_r", "PuOr", "BrBG"]

N_STRIPES = 64


def draw_discrete(ax, colors, y, height=1.0):
    """Нарисовать ряд дискретных цветовых квадратов."""
    n = len(colors)
    for i, color in enumerate(colors):
        ax.add_patch(
            Rectangle(
                (i, y),
                1.0,
                height,
                facecolor=color,
                edgecolor="white",
                linewidth=0.8,
            )
        )
    ax.add_patch(
        Rectangle((0, y), n, height, fill=False, edgecolor="#4D4D4D", linewidth=0.5)
    )
    ax.set_xlim(0, n)
    ax.set_ylim(0, 2.4)


def draw_gradient(ax, cmap_name, y, height=1.0):
    """Нарисовать непрерывную градиентную полосу."""
    cmap = plt.get_cmap(cmap_name)
    for i in range(N_STRIPES):
        ax.add_patch(
            Rectangle(
                (i / N_STRIPES, y),
                1 / N_STRIPES,
                height,
                facecolor=cmap(i / (N_STRIPES - 1)),
                edgecolor="none",
            )
        )
    ax.add_patch(
        Rectangle((0, y), 1, height, fill=False, edgecolor="#4D4D4D", linewidth=0.5)
    )
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 2.4)


def main() -> None:
    apply_style(font_size=8)

    fig, axes = plt.subplots(
        1,
        3,
        figsize=figure_size("double", height_mm=62),
        layout="constrained",
    )
    fig.set_constrained_layout_pads(w_pad=0.03, h_pad=0.03)

    # A. Качественная: две палитры, по 7 цветов.
    ax = axes[0]
    for row, (name, colors) in enumerate(QUALITATIVE.items()):
        y = 1.3 - row * 1.1
        draw_discrete(ax, colors, y)
        label_color = "white" if row == 0 else "#333333"
        ax.text(
            0.02,
            y + 0.5,
            name,
            transform=ax.transData,
            fontsize=6.5,
            va="center",
            color=label_color,
            fontweight="bold",
        )
    ax.set_title("Качественная", fontsize=9, pad=5)
    ax.axis("off")

    # B. Последовательная: виридно-подобные шкалы.
    ax = axes[1]
    for row, name in enumerate(SEQUENTIAL):
        y = 1.3 - row * 1.1
        draw_gradient(ax, name, y)
        ax.text(
            0.02,
            y + 0.5,
            name,
            transform=ax.transData,
            fontsize=6.5,
            va="center",
            color="white",
        )
    ax.set_title("Последовательная", fontsize=9, pad=5)
    ax.axis("off")

    # C. Дивергентная: три шкалы с нейтральной серединой.
    ax = axes[2]
    for row, name in enumerate(DIVERGING):
        y = 1.8 - row * 0.9
        draw_gradient(ax, name, y, height=0.8)
        ax.text(0.5, y + 0.4, name, transform=ax.transData, fontsize=6.5, va="center",
                ha="center", color="#333333", fontweight="bold")
    ax.set_ylim(0, 2.7)
    ax.set_title("Дивергентная", fontsize=9, pad=5)
    ax.axis("off")

    save_figure(fig, "03_palettes", formats=("svg", "png"), dpi=600)


if __name__ == "__main__":
    main()
