#!/usr/bin/env python3
"""«Плохой» violinplot для раздела 5.12.

Что специально сделано неправильно
----------------------------------
1. Ось Y обрезана до 25–100: нижняя стадия и верхний хвост скрыты.
2. Радужные тела скрипок и толстые чёрные контуры.
3. Нет медианы, квартилей и точек: форма есть, сводки нет.
4. Тяжёлая сетка, полная рамка.
5. Заголовок «eGFR и стадия ХБП» ничего не сообщает.
6. Нет единиц и n.

Выход: images/05_12_bad_violin.{svg,png}
Запуск: uv run python 05_charts/12_violin/scripts/bad_plot.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, save_figure

STAGES = ["1–2", "3", "4–5"]


def main() -> None:
    apply_style()

    df = pd.read_csv(DATA_DIR / "12_dataset.csv")
    data = [df.loc[df["ckd_stage"] == stage, "egfr_ml_min_1_73m2"].to_numpy() for stage in STAGES]

    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    violins = ax.violinplot(
        data,
        positions=[1, 2, 3],
        widths=0.8,
        showmeans=False,
        showmedians=False,
        showextrema=False,
    )
    colors = plt.cm.jet(np.linspace(0.0, 1.0, len(violins["bodies"])))
    for body, color in zip(violins["bodies"], colors, strict=True):
        body.set_facecolor(color)
        body.set_edgecolor("black")
        body.set_linewidth(2.0)
        body.set_alpha(1.0)

    ax.set_ylim(25, 100)
    ax.grid(True, which="major", axis="both", color="#BDBDBD", linewidth=1.0)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1.5)
        spine.set_color("black")

    ax.tick_params(labelsize=12, width=1.4, length=5)
    ax.set_xticks([1, 2, 3])
    ax.set_xticklabels(STAGES, fontsize=11)
    ax.set_title("eGFR и стадия ХБП", fontsize=18, fontweight="bold")
    ax.set_ylabel("eGFR", fontsize=15)
    ax.set_xlabel("Стадия ХБП", fontsize=15)

    fig.tight_layout()
    save_figure(fig, "05_12_bad_violin", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
