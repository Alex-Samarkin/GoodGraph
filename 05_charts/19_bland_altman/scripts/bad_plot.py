#!/usr/bin/env python3
"""«Плохой» Bland–Altman для раздела 5.19.

Что специально сделано неправильно
----------------------------------
1. По X — один метод, а не среднее двух: классическая ошибка BA.
2. Нет bias и пределов согласия (LoA).
3. Ось Y обрезана до 0–2: отрицательные разницы скрыты.
4. Радужные точки, тяжёлая сетка, полная рамка.
5. Заголовок «Разница методов» ничего не сообщает.
6. Нет единиц и n.

Выход: images/05_19_bad_bland_altman.{svg,png}
Запуск: uv run python 05_charts/19_bland_altman/scripts/bad_plot.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, save_figure


def main() -> None:
    apply_style()

    df = pd.read_csv(DATA_DIR / "19_dataset.csv")
    diff = df["lab_glucose"] - df["meter_glucose"]
    x = df["meter_glucose"].to_numpy()

    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    colors = plt.cm.rainbow(np.linspace(0.0, 1.0, len(df)))
    ax.scatter(x, diff, s=40, c=colors, edgecolors="black", linewidths=0.4, zorder=3)

    ax.set_xlim(3, 13)
    ax.set_ylim(0, 2)
    ax.grid(True, which="major", axis="both", color="#BDBDBD", linewidth=1.0)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1.5)
        spine.set_color("black")

    ax.tick_params(labelsize=12, width=1.4, length=5)
    ax.set_title("Разница методов", fontsize=18, fontweight="bold")
    ax.set_ylabel("Разница", fontsize=15)
    ax.set_xlabel("Глюкометр", fontsize=15)

    fig.tight_layout()
    save_figure(fig, "05_19_bad_bland_altman", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
