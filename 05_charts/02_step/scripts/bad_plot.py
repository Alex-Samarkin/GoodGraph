#!/usr/bin/env python3
"""«Плохой» ступенчатый график для раздела 5.02.

Что специально сделано неправильно
----------------------------------
1. Дозы соединены наклонными линиями: создаётся впечатление плавного
   изменения, которого не было. Доза меняется только на визите.
2. Ось Y обрезана до 2,5–8: масштаб раздувает различия.
3. Светофорная палитра «красный — жёлтый — зелёный».
4. Толстые линии с тенями и крупными маркерами.
5. Тяжёлая сетка по обеим осям и полная рамка.
6. Заголовок «Дозы варфарина» ничего не сообщает.
7. Нет единиц, числа пациентов и контекста INR.
8. Легенда внутри поля данных.

Выход: images/05_02_bad_step.{svg,png}
Запуск: uv run python 05_charts/02_step/scripts/bad_plot.py
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

PATIENTS = ["P01", "P02", "P03"]
TRAFFIC_COLORS = ["#D62728", "#FFC000", "#2CA02C"]
MARKERS = ["o", "s", "^"]


def main() -> None:
    apply_style()

    df = pd.read_csv(DATA_DIR / "02_dataset.csv")
    doses = df.pivot(index="week", columns="patient_id", values="dose_mg")[PATIENTS]
    weeks = doses.index.to_numpy()

    fig, ax = plt.subplots(figsize=(6.4, 4.8))

    for patient, color, marker in zip(PATIENTS, TRAFFIC_COLORS, MARKERS, strict=True):
        (line,) = ax.plot(
            weeks,
            doses[patient].to_numpy(),
            color=color,
            linewidth=3.5,
            marker=marker,
            markersize=9,
            markeredgecolor="black",
            markeredgewidth=1.0,
            label=patient,
            zorder=3,
        )
        line.set_path_effects(
            [
                pe.SimpleLineShadow(offset=(2, -2), shadow_color="0.5", alpha=0.6),
                pe.Normal(),
            ]
        )

    ax.set_ylim(2.5, 8.0)
    ax.set_yticks(np.arange(3, 9, 1))

    ax.grid(True, which="major", axis="both", color="#BDBDBD", linewidth=1.0)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1.5)
        spine.set_color("black")

    ax.tick_params(labelsize=12, width=1.4, length=5)
    ax.set_xticks(weeks)
    ax.set_xticklabels([str(week) for week in weeks], fontsize=11)

    ax.set_title("Дозы варфарина", fontsize=18, fontweight="bold")
    ax.set_ylabel("Доза", fontsize=15)
    ax.set_xlabel("Недели", fontsize=15)

    ax.legend(
        loc="upper right",
        fontsize=11,
        frameon=True,
        edgecolor="black",
        facecolor="white",
    )

    fig.tight_layout()
    save_figure(fig, "05_02_bad_step", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
