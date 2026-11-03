#!/usr/bin/env python3
"""«Плохой» boxplot для раздела 5.11.

Что специально сделано неправильно
----------------------------------
1. Ось Y обрезана до 22–32: выбросы и хвосты скрыты.
2. Радужные ящики, красные медианы и выбросы: декор вместо данных.
3. Нет отдельных точек: не видно формы распределения и размера групп.
4. Тяжёлая сетка, полная рамка, толстые линии.
5. Заголовок «BMI и активность» ничего не сообщает.
6. Нет единиц и n.

Выход: images/05_11_bad_box.{svg,png}
Запуск: uv run python 05_charts/11_box/scripts/bad_plot.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, save_figure

GROUPS = ["низкая", "умеренная", "высокая"]


def main() -> None:
    apply_style()

    df = pd.read_csv(DATA_DIR / "11_dataset.csv")
    data = [df.loc[df["activity"] == group, "bmi_kg_m2"].to_numpy() for group in GROUPS]

    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    box = ax.boxplot(
        data,
        positions=[1, 2, 3],
        widths=0.6,
        patch_artist=True,
        medianprops={"color": "#D62728", "linewidth": 3},
        whiskerprops={"color": "black", "linewidth": 2},
        capprops={"color": "black", "linewidth": 2},
        flierprops={
            "marker": "o",
            "markerfacecolor": "#D62728",
            "markeredgecolor": "black",
            "markersize": 7,
        },
    )

    colors = plt.cm.jet(np.linspace(0.0, 1.0, len(box["boxes"])))
    for patch, color in zip(box["boxes"], colors, strict=True):
        patch.set_facecolor(color)
        patch.set_edgecolor("black")
        patch.set_linewidth(2)

    ax.set_ylim(22, 32)
    ax.grid(True, which="major", axis="both", color="#BDBDBD", linewidth=1.0)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1.5)
        spine.set_color("black")

    ax.tick_params(labelsize=12, width=1.4, length=5)
    ax.set_xticks([1, 2, 3])
    ax.set_xticklabels(GROUPS, fontsize=11)
    ax.set_title("BMI и активность", fontsize=18, fontweight="bold")
    ax.set_ylabel("BMI", fontsize=15)
    ax.set_xlabel("Активность", fontsize=15)

    fig.tight_layout()
    save_figure(fig, "05_11_bad_box", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
