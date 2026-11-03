#!/usr/bin/env python3
"""«Плохой» stacked bar для раздела 5.20.

Что специально сделано неправильно
----------------------------------
1. Ось Y обрезана до 700: высокие столбцы и общий объём скрыты.
2. Радужные сегменты, чёрные края, тени, «3D».
3. Нет подписей значений и общего числа.
4. Тяжёлая сетка, полная рамка.
5. Заголовок «Исходы» ничего не сообщает.
6. Нет единиц и n.

Выход: images/05_20_bad_stacked_bar.{svg,png}
Запуск: uv run python 05_charts/20_stacked_bar/scripts/bad_plot.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, save_figure

OUTCOMES = ["выписан", "переведён", "умер"]


def main() -> None:
    apply_style()

    df = pd.read_csv(DATA_DIR / "20_dataset.csv")
    pivot = df.pivot(index="department", columns="outcome", values="patients").loc[
        ["Терапия", "Хирургия", "Кардиология", "ОРИТ"], OUTCOMES
    ]
    x = np.arange(len(pivot))
    bottom = np.zeros(len(pivot))
    colors = plt.cm.rainbow(np.linspace(0.0, 1.0, len(OUTCOMES)))

    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    for outcome, color in zip(OUTCOMES, colors, strict=True):
        bars = ax.bar(
            x,
            pivot[outcome],
            bottom=bottom,
            color=color,
            edgecolor="black",
            linewidth=2,
            label=outcome,
            zorder=3,
        )
        for bar in bars:
            bar.set_path_effects(
                [pe.withSimplePatchShadow(offset=(3, -3), shadow_rgbFace="0.5", alpha=0.5)]
            )
        bottom += pivot[outcome].to_numpy()

    ax.set_ylim(0, 700)
    ax.grid(True, which="major", axis="both", color="#BDBDBD", linewidth=1.0)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1.5)
        spine.set_color("black")

    ax.tick_params(labelsize=12, width=1.4, length=5)
    ax.set_xticks(x)
    ax.set_xticklabels(pivot.index, rotation=20, ha="right", fontsize=10)
    ax.set_title("Исходы", fontsize=18, fontweight="bold")
    ax.set_ylabel("Число", fontsize=15)
    ax.legend(loc="upper right", fontsize=9, frameon=True, edgecolor="black")

    fig.tight_layout()
    save_figure(fig, "05_20_bad_stacked_bar", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
