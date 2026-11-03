#!/usr/bin/env python3
"""«Правильный» contour для раздела 5.07.

Что улучшено
------------
1. Контурная карта плотности с логарифмической шкалой и 8 уровнями.
2. cividis вместо jet: последовательная и доступная шкала.
3. Полный диапазон осей 20–80 лет и 90–200 мм рт. ст.
4. Подписанный colorbar: «Пациенты (лог. шкала)».
5. Порог 140 мм рт. ст. выделен линией.
6. Единицы, n и r; заголовок-вывод.
7. 85 мм, без тяжёлой сетки.

Выход: images/05_07_good_contour.{svg,png}
Запуск: uv run python 05_charts/07_contour/scripts/good_plot.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import LogNorm
from scipy.ndimage import gaussian_filter

from goodgraph.palettes import ACCENT_VERMILLION
from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, figure_size, save_figure


def main() -> None:
    apply_style()

    df = pd.read_csv(DATA_DIR / "07_dataset.csv")
    age = df["age_years"].to_numpy()
    sbp = df["sbp_mm_hg"].to_numpy()
    r = df["age_years"].corr(df["sbp_mm_hg"])

    hist, xedges, yedges = np.histogram2d(
        age, sbp, bins=(45, 45), range=[[20, 80], [90, 200]]
    )
    xcenters = 0.5 * (xedges[:-1] + xedges[1:])
    ycenters = 0.5 * (yedges[:-1] + yedges[1:])
    xx, yy = np.meshgrid(xcenters, ycenters)

    smooth = gaussian_filter(hist, sigma=1.2)
    levels = np.logspace(0, np.log10(smooth.max()), 9)
    hist_masked = np.ma.masked_less_equal(smooth, 0)
    fig, ax = plt.subplots(
        figsize=figure_size("single", height_mm=72),
        layout="constrained",
    )
    fig.set_constrained_layout_pads(w_pad=0.04, h_pad=0.02)

    filled = ax.contourf(
        xx,
        yy,
        hist_masked.T,
        levels=levels,
        cmap="cividis",
        norm=LogNorm(vmin=1, vmax=smooth.max()),
    )
    ax.contour(
        xx,
        yy,
        hist_masked.T,
        levels=levels[3::2],
        colors="white",
        linewidths=0.4,
        alpha=0.75,
    )

    cbar = fig.colorbar(filled, ax=ax, fraction=0.05, pad=0.02, shrink=0.85)
    cbar.set_label("Пациенты (лог. шкала)", fontsize=7)
    cbar.set_ticks([1, 3, 10, 20])
    cbar.ax.set_yticklabels(["1", "3", "10", "20"])
    cbar.ax.tick_params(labelsize=6.5)

    ax.axhline(
        140,
        color=ACCENT_VERMILLION,
        linestyle=(0, (3, 2)),
        linewidth=0.9,
        zorder=5,
    )
    ax.text(
        21,
        142,
        "САД 140",
        fontsize=6.5,
        color=ACCENT_VERMILLION,
        va="bottom",
    )

    r_text = f"{r:.2f}".replace(".", ",")
    ax.text(
        21,
        195,
        f"n = {len(df)}; r = {r_text}",
        fontsize=7.5,
        color="#333333",
        va="top",
    )

    ax.set_xlim(20, 80)
    ax.set_ylim(90, 200)
    ax.set_xticks([20, 40, 60, 80])
    ax.set_yticks([100, 140, 180])

    ax.set_xlabel("Возраст, лет")
    ax.set_ylabel("САД, мм рт. ст.")
    ax.set_title("Плотность: возраст и САД", loc="left", fontsize=9.5, pad=6)

    ax.grid(False)

    save_figure(fig, "05_07_good_contour", formats=("svg", "png"), dpi=600)

    print(f"n = {len(df)}, r = {r:.3f}")
    print(f"Максимум плотности: {hist.max():.0f} пациентов в бине")


if __name__ == "__main__":
    main()
