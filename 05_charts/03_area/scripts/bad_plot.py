#!/usr/bin/env python3
"""«Плохой» area chart для раздела 5.03.

Что специально сделано неправильно
----------------------------------
1. Заливка начинается с y = 4, а не с нуля: площадь под кривой больше
   не пропорциональна AUC. Это главная ошибка area chart.
2. Ось Y обрезана до 4–10: пик и хвост искажены.
3. Яркая красная заливка, зелёная линия, тени и крупные маркеры.
4. Тяжёлая сетка по обеим осям и полная рамка.
5. Заголовок «Концентрация препарата» ничего не сообщает.
6. Нет единиц, n и AUC — площадь не подписана.
7. Легенда из одной бесполезной строки.
8. Тёмная заливка закрывает сетку и делает график тяжёлым.

Выход: images/05_03_bad_area.{svg,png}
Запуск: uv run python 05_charts/03_area/scripts/bad_plot.py
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

    df = pd.read_csv(DATA_DIR / "03_dataset.csv")
    mean = df.groupby("time_h")["conc_mg_l"].mean()
    time = mean.index.to_numpy()

    fig, ax = plt.subplots(figsize=(6.4, 4.8))

    # Заливка от 4, а не от 0: площадь теряет смысл.
    ax.fill_between(
        time,
        4,
        mean.to_numpy(),
        color="#D62728",
        alpha=0.9,
        zorder=2,
    )
    (line,) = ax.plot(
        time,
        mean.to_numpy(),
        color="#2CA02C",
        linewidth=3.5,
        marker="o",
        markersize=9,
        markeredgecolor="black",
        markeredgewidth=1.0,
        label="Кривая",
        zorder=3,
    )
    line.set_path_effects(
        [
            pe.SimpleLineShadow(offset=(2, -2), shadow_color="0.4", alpha=0.6),
            pe.Normal(),
        ]
    )

    ax.set_ylim(4, 10)
    ax.set_yticks(np.arange(4, 11, 1))

    ax.grid(True, which="major", axis="both", color="#BDBDBD", linewidth=1.0)
    ax.set_axisbelow(False)
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1.5)
        spine.set_color("black")

    ax.tick_params(labelsize=13, width=1.4, length=5)
    ax.set_xticks([0, 6, 12, 18, 24])
    ax.set_xticklabels(["0", "6", "12", "18", "24"], fontsize=13)

    ax.set_title("Концентрация препарата", fontsize=18, fontweight="bold")
    ax.set_ylabel("Концентрация", fontsize=15)
    ax.set_xlabel("Время", fontsize=15)

    ax.legend(
        loc="upper right",
        fontsize=11,
        frameon=True,
        edgecolor="black",
        facecolor="white",
    )

    fig.tight_layout()
    save_figure(fig, "05_03_bad_area", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
