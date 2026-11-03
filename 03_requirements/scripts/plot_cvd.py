#!/usr/bin/env python3
"""Симуляция дальтонизма: Okabe–Ito против «красный–зелёный».

Схема для раздела 3. Показывает, почему нельзя кодировать смысл только
красным и зелёным и почему палитра Okabe–Ito остаётся различимой.

Матрицы — Machado, Oliveira, Fernandes (2009), severity 100 %.
Прямое применение матриц в линейном RGB; sRGB-гамма снимается и
возвращается вручную, чтобы не зависеть от внешних библиотек.

Выход: images/03_cvd.{svg,png}
Запуск: uv run python 03_requirements/scripts/plot_cvd.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import to_rgb
from matplotlib.patches import Rectangle

from goodgraph.palettes import OKABE_ITO
from goodgraph.style import apply_style, figure_size, save_figure

# Machado et al., 2009, severity 100 %.
# Матрицы применяются к линейному RGB.
CVD_MATRICES = {
    "deuteranomaly": np.array(
        [
            [0.367322, 0.860646, -0.227968],
            [0.280085, 0.672501, 0.047413],
            [-0.011820, 0.042940, 0.968881],
        ]
    ),
    "protanomaly": np.array(
        [
            [0.152286, 1.052583, -0.204868],
            [0.114503, 0.786281, 0.099216],
            [-0.003882, -0.048116, 1.051998],
        ]
    ),
    "tritanomaly": np.array(
        [
            [1.255528, -0.076749, -0.178779],
            [-0.078411, 0.930809, 0.147602],
            [0.004733, 0.691367, 0.303900],
        ]
    ),
}

PALETTES = {
    "Okabe–Ito": list(OKABE_ITO.values())[:-1],
    "Красный–зелёный": [
        "#D7191C",
        "#1A9641",
        "#FDAE61",
        "#A6D96A",
        "#A50026",
        "#006837",
        "#FFFFBF",
    ],
}

ROWS = [
    ("Норма", None),
    ("Дейтеранопия", "deuteranomaly"),
    ("Протанопия", "protanomaly"),
    ("Тританопия", "tritanomaly"),
    ("Градации серого", "gray"),
]


def srgb_to_linear(rgb: np.ndarray) -> np.ndarray:
    """Снять sRGB-гамму."""
    return np.where(rgb <= 0.04045, rgb / 12.92, ((rgb + 0.055) / 1.055) ** 2.4)


def linear_to_srgb(rgb: np.ndarray) -> np.ndarray:
    """Нанести sRGB-гамму и обрезать в допустимый диапазон."""
    rgb = np.clip(rgb, 0.0, 1.0)
    return np.where(rgb <= 0.0031308, rgb * 12.92, 1.055 * rgb ** (1 / 2.4) - 0.055)


def simulate(colors: list[str], cvd_type: str | None) -> np.ndarray:
    """Вернуть RGB-цвета после симуляции нарушения цветового зрения."""
    rgb = np.array([to_rgb(color) for color in colors])
    linear = srgb_to_linear(rgb)

    if cvd_type is None:
        return rgb

    if cvd_type == "gray":
        luminance = linear @ np.array([0.2126, 0.7152, 0.0722])
        out_linear = np.stack([luminance, luminance, luminance], axis=1)
    else:
        out_linear = linear @ CVD_MATRICES[cvd_type].T

    return np.clip(linear_to_srgb(out_linear), 0.0, 1.0)


def draw_strip(ax: plt.Axes, colors: np.ndarray) -> None:
    """Нарисовать ряд квадратов и тонкую рамку."""
    n = len(colors)
    for i, color in enumerate(colors):
        ax.add_patch(
            Rectangle(
                (i, 0),
                1,
                1,
                facecolor=color,
                edgecolor="white",
                linewidth=0.8,
            )
        )
    ax.add_patch(Rectangle((0, 0), n, 1, fill=False, edgecolor="#4D4D4D", linewidth=0.5))
    ax.set_xlim(0, n)
    ax.set_ylim(0, 1)
    ax.axis("off")


def main() -> None:
    apply_style(font_size=8)

    fig, axes = plt.subplots(
        len(ROWS),
        3,
        figsize=figure_size("double", height_mm=100),
        gridspec_kw={"width_ratios": [1.3, 4, 4]},
        layout="constrained",
    )
    fig.set_constrained_layout_pads(w_pad=0.03, h_pad=0.03)

    for col, (palette_name, _) in enumerate(PALETTES.items(), start=1):
        axes[0, col].set_title(palette_name, fontsize=8.5, pad=4)

    for row, (label, cvd_type) in enumerate(ROWS):
        label_ax = axes[row, 0]
        label_ax.set_xlim(0, 1)
        label_ax.set_ylim(0, 1)
        label_ax.axis("off")
        label_ax.text(
            0.98,
            0.5,
            label,
            ha="right",
            va="center",
            fontsize=7,
            color="#333333",
        )

        for col, colors in enumerate(PALETTES.values(), start=1):
            ax = axes[row, col]
            draw_strip(ax, simulate(colors, cvd_type))

    save_figure(fig, "03_cvd", formats=("svg", "png"), dpi=600)


if __name__ == "__main__":
    main()
