#!/usr/bin/env python3
"""Violin с внутренней коробкой (rectangles) для раздела 5.12.

Что улучшено
------------
1. Тело скрипки показывает плотность, внутренняя коробка — медиану и IQR.
2. Полный диапазон 0–130 мл/мин/1,73 м².
3. Точки с jitter: видны наблюдения.
4. Единицы, n, заголовок, 85 мм.

Выход: images/05_12_good_violin_box.{svg,png}
Запуск: uv run python 05_charts/12_violin/scripts/good_violin_box.py
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

STAGES = ["1–2", "3", "4–5"]


def main() -> None:
    apply_style()

    df = pd.read_csv(DATA_DIR / "12_dataset.csv")
    rng = np.random.default_rng(22)
    data = [df.loc[df["ckd_stage"] == stage, "egfr_ml_min_1_73m2"].to_numpy() for stage in STAGES]

    fig, ax = plt.subplots(
        figsize=figure_size("single", height_mm=75),
        layout="constrained",
    )
    fig.set_constrained_layout_pads(w_pad=0.04, h_pad=0.02)

    violins = ax.violinplot(
        data,
        positions=[1, 2, 3],
        widths=0.8,
        showmeans=False,
        showmedians=False,
        showextrema=False,
        points=100,
    )
    for body in violins["bodies"]:
        body.set_facecolor(PRIMARY_BLUE)
        body.set_edgecolor(PRIMARY_BLUE)
        body.set_alpha(0.15)
        body.set_linewidth(0.6)

    ax.boxplot(
        data,
        positions=[1, 2, 3],
        widths=0.16,
        patch_artist=True,
        showfliers=False,
        boxprops={"facecolor": "white", "edgecolor": PRIMARY_BLUE, "linewidth": 0.8},
        medianprops={"color": "#333333", "linewidth": 1.1},
        whiskerprops={"color": PRIMARY_BLUE, "linewidth": 0.7},
        capprops={"color": PRIMARY_BLUE, "linewidth": 0.7},
    )

    for position, values in zip([1, 2, 3], data, strict=True):
        jitter = rng.normal(0.0, 0.07, len(values))
        ax.scatter(
            position + jitter,
            values,
            s=3,
            color=PRIMARY_BLUE,
            alpha=0.10,
            linewidths=0,
            zorder=4,
        )

    ax.text(
        0.02,
        0.97,
        f"n = {len(data[0])} в каждой группе",
        transform=ax.transAxes,
        fontsize=7,
        color="#333333",
        va="top",
    )

    ax.set_xlim(0.4, 3.6)
    ax.set_ylim(0, 130)
    ax.set_xticks([1, 2, 3])
    ax.set_xticklabels(STAGES)
    ax.set_yticks([0, 30, 60, 90, 120])

    ax.set_xlabel("Стадия ХБП")
    ax.set_ylabel("eGFR, мл/мин/1,73 м²")
    ax.set_title("Violin с внутренней коробкой", loc="left", fontsize=9.5, pad=6)

    ax.grid(axis="y", color="#E8E8E8", linewidth=0.6)
    ax.grid(axis="x", visible=False)

    save_figure(fig, "05_12_good_violin_box", formats=("svg", "png"), dpi=600)


if __name__ == "__main__":
    main()
