#!/usr/bin/env python3
"""Boxplot + гистограмма для раздела 5.11.

Что улучшено
------------
1. Гистограмма показывает форму, boxplot — медиану, IQR и выбросы.
2. Общая ось X: гистограмма и коробка выровнены.
3. Один цвет, единицы, n, заголовок.
4. 85 мм, без лишней сетки.

Выход: images/05_11_good_box_hist.{svg,png}
Запуск: uv run python 05_charts/11_box/scripts/good_box_hist.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from goodgraph.palettes import PRIMARY_BLUE
from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, figure_size, save_figure


def main() -> None:
    apply_style()

    df = pd.read_csv(DATA_DIR / "11_dataset.csv")
    values = df.loc[df["activity"] == "низкая", "bmi_kg_m2"].to_numpy()
    median = float(np.median(values))

    fig, (ax_hist, ax_box) = plt.subplots(
        2,
        1,
        figsize=figure_size("single", height_mm=80),
        sharex=True,
        gridspec_kw={"height_ratios": [3, 1]},
        layout="constrained",
    )
    fig.set_constrained_layout_pads(w_pad=0.04, h_pad=0.02)

    ax_hist.hist(
        values,
        bins=np.arange(15, 47, 2),
        color=PRIMARY_BLUE,
        alpha=0.80,
        edgecolor="white",
        linewidth=0.4,
    )
    ax_hist.set_ylabel("Пациенты")
    ax_hist.set_title("Низкая активность: гистограмма + коробка", loc="left", fontsize=9.5, pad=6)
    ax_hist.grid(axis="y", color="#E8E8E8", linewidth=0.6)
    ax_hist.grid(axis="x", visible=False)
    ax_hist.tick_params(labelbottom=False)

    ax_box.boxplot(
        [values],
        orientation="horizontal",
        positions=[0.5],
        widths=0.5,
        patch_artist=True,
        showfliers=False,
        boxprops={"facecolor": "white", "edgecolor": PRIMARY_BLUE, "linewidth": 0.9},
        medianprops={"color": "#333333", "linewidth": 1.2},
        whiskerprops={"color": PRIMARY_BLUE, "linewidth": 0.8},
        capprops={"color": PRIMARY_BLUE, "linewidth": 0.8},
    )
    ax_box.text(
        median,
        0.80,
        f"медиана {median:.1f}".replace(".", ","),
        fontsize=6.5,
        color="#333333",
        ha="center",
        va="bottom",
    )
    ax_box.set_yticks([])
    ax_box.set_ylim(0, 1)
    ax_box.set_xlim(15, 45)
    ax_box.set_xticks([15, 20, 25, 30, 35, 40, 45])
    ax_box.set_xlabel("BMI, кг/м²")
    ax_box.spines["left"].set_visible(False)
    ax_box.grid(False)

    save_figure(fig, "05_11_good_box_hist", formats=("svg", "png"), dpi=600)


if __name__ == "__main__":
    main()
