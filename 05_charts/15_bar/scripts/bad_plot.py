#!/usr/bin/env python3
"""«Плохой» bar chart для раздела 5.15.

Что специально сделано неправильно
----------------------------------
1. Ось Y обрезана до 800–1300: нулевая база скрыта, различия
   преувеличены.
2. Радужные столбцы, чёрные края и тени.
3. Отделения не отсортированы.
4. Тяжёлая сетка по обеим осям и полная рамка.
5. Заголовок «Госпитализации» ничего не сообщает.
6. Нет значений на столбцах, единиц и n.

Выход: images/05_15_bad_bar.{svg,png}
Запуск: uv run python 05_charts/15_bar/scripts/bad_plot.py
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


def main() -> None:
    apply_style()

    df = pd.read_csv(DATA_DIR / "15_dataset.csv")
    order = [2, 0, 4, 1, 3]
    df = df.iloc[order].reset_index(drop=True)
    x = np.arange(len(df))

    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    colors = plt.cm.jet(np.linspace(0.0, 1.0, len(df)))
    bars = ax.bar(
        x,
        df["admissions"],
        color=colors,
        edgecolor="black",
        linewidth=2.0,
        zorder=3,
    )
    for bar in bars:
        bar.set_path_effects(
            [pe.withSimplePatchShadow(offset=(3, -3), shadow_rgbFace="0.5", alpha=0.6)]
        )

    ax.set_ylim(800, 1300)
    ax.grid(True, which="major", axis="both", color="#BDBDBD", linewidth=1.0)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1.5)
        spine.set_color("black")

    ax.tick_params(labelsize=12, width=1.4, length=5)
    ax.set_xticks(x)
    ax.set_xticklabels(df["department"], rotation=30, ha="right", fontsize=10)
    ax.set_title("Госпитализации", fontsize=18, fontweight="bold")
    ax.set_ylabel("Число", fontsize=15)

    fig.tight_layout()
    save_figure(fig, "05_15_bad_bar", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
