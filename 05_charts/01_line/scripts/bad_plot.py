#!/usr/bin/env python3
"""«Плохой» линейный график для раздела 5.01.

Что специально сделано неправильно
----------------------------------
1. Ось Y обрезана до 130–155: масштаб раздувает различия.
2. Светофорная палитра «красный — жёлтый — зелёный».
3. Толстые линии с тенями и крупными маркерами — декор вместо данных.
4. Тяжёлая сетка по обеим осям и полная рамка.
5. Заголовок «Динамика САД» ничего не сообщает.
6. Нет единиц, n, доверительных интервалов и числа наблюдений.
7. Легенда внутри поля данных.
8. Показаны только средние; разброс и неопределённость скрыты.
9. Брекет «p < 0,05» без теста и эффекта.

Выход: images/05_01_bad_line.{svg,png}
Запуск: uv run python 05_charts/01_line/scripts/bad_plot.py
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

GROUP_ORDER = ["Плацебо", "Препарат A 10 мг", "Препарат B 20 мг"]
TRAFFIC_COLORS = ["#D62728", "#FFC000", "#2CA02C"]
MARKERS = ["o", "s", "^"]
WEEK_LABELS = ["0", "4", "8", "12"]


def main() -> None:
    apply_style()

    df = pd.read_csv(DATA_DIR / "01_dataset.csv")
    means = (
        df.groupby(["group", "week"], sort=False)["sbp_mm_hg"]
        .mean()
        .unstack()
        .reindex(GROUP_ORDER)
    )

    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    x = np.arange(means.shape[1])

    for group, color, marker in zip(GROUP_ORDER, TRAFFIC_COLORS, MARKERS, strict=True):
        (line,) = ax.plot(
            x,
            means.loc[group].to_numpy(),
            color=color,
            linewidth=4.0,
            marker=marker,
            markersize=11,
            markeredgecolor="black",
            markeredgewidth=1.0,
            label=group,
            zorder=3,
        )
        line.set_path_effects(
            [
                pe.SimpleLineShadow(offset=(2, -2), shadow_color="0.5", alpha=0.6),
                pe.Normal(),
            ]
        )

    # Обрезанная ось — главный источник искажения.
    ax.set_ylim(130, 155)
    ax.set_yticks(np.arange(130, 156, 5))

    ax.grid(True, which="major", axis="both", color="#BDBDBD", linewidth=1.0)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1.5)
        spine.set_color("black")

    ax.tick_params(labelsize=13, width=1.4, length=5)
    ax.set_xticks(x)
    ax.set_xticklabels(WEEK_LABELS, fontsize=13)

    ax.set_title("Динамика САД", fontsize=18, fontweight="bold")
    ax.set_ylabel("САД", fontsize=15)
    ax.set_xlabel("Недели", fontsize=15)

    ax.legend(
        loc="upper right",
        fontsize=11,
        frameon=True,
        edgecolor="black",
        facecolor="white",
    )

    # Брекет значимости без теста и эффекта.
    ax.plot([0, 0, 3, 3], [152.8, 153.8, 153.8, 152.8], color="black", linewidth=1.2)
    ax.text(1.5, 154.0, "p < 0,05", ha="center", va="bottom", fontsize=11)

    fig.tight_layout()
    save_figure(fig, "05_01_bad_line", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
