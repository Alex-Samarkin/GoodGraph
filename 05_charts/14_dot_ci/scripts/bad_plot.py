#!/usr/bin/env python3
"""«Плохой» dot + CI для раздела 5.14.

Что специально сделано неправильно
----------------------------------
1. Вместо 95 % ДИ — стандартное отклонение бинарного исхода (SE/SD):
   интервалы выглядят узкими и не являются доверительными.
2. Ось X обрезана до 0–15 %: центры с высокой долей скрыты.
3. Радужные точки и толстые усы.
4. Тяжёлая сетка, полная рамка.
5. Заголовок «Осложнения по центрам» ничего не сообщает.
6. Нет общей доли, n и единиц.

Выход: images/05_14_bad_dot_ci.{svg,png}
Запуск: uv run python 05_charts/14_dot_ci/scripts/bad_plot.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, save_figure

CENTERS = ["Центр A", "Центр B", "Центр C", "Центр D", "Центр E", "Центр F"]


def main() -> None:
    apply_style()

    df = pd.read_csv(DATA_DIR / "14_dataset.csv")
    fig, ax = plt.subplots(figsize=(6.4, 4.8))

    colors = plt.cm.rainbow(np.linspace(0.0, 1.0, len(CENTERS)))
    for y, (center, color) in enumerate(zip(CENTERS, colors, strict=True)):
        values = df.loc[df["center"] == center, "complication"].to_numpy()
        p = values.mean() * 100
        sd = np.sqrt(values.mean() * (1 - values.mean())) * 100
        ax.errorbar(
            p,
            y,
            xerr=sd,
            fmt="o",
            color=color,
            ecolor=color,
            markersize=9,
            elinewidth=2.5,
            capsize=4,
            markeredgecolor="black",
        )

    ax.set_xlim(0, 15)
    ax.set_ylim(-0.6, len(CENTERS) - 0.4)
    ax.set_yticks(range(len(CENTERS)))
    ax.set_yticklabels(CENTERS, fontsize=11)

    ax.grid(True, which="major", axis="both", color="#BDBDBD", linewidth=1.0)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1.5)
        spine.set_color("black")

    ax.tick_params(labelsize=12, width=1.4, length=5)
    ax.set_title("Осложнения по центрам", fontsize=18, fontweight="bold")
    ax.set_xlabel("%", fontsize=15)

    fig.tight_layout()
    save_figure(fig, "05_14_bad_dot_ci", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
