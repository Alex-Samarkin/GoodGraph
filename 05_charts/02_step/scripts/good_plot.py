#!/usr/bin/env python3
"""«Правильный» ступенчатый график для раздела 5.02.

Что улучшено
------------
1. `ax.step(..., where="post")`: доза сохраняется до следующего визита,
   а не меняется плавно.
2. Маркеры только в моменты измерения; вертикальные сегменты показывают
   скачок дозы.
3. Прямые подписи P01/P02/P03 вместо легенды.
4. Ось Y 0–8: виден масштаб доз, без обрезки «под эффект».
5. Единицы «мг/сут», недели 0–12.
6. Заголовок сообщает, что доза титруется шагами.
7. Палитра Okabe–Ito, лёгкая сетка только по Y.
8. 85 мм в ширину — конечный журнальный размер.

Выход: images/05_02_good_step.{svg,png}
Запуск: uv run python 05_charts/02_step/scripts/good_plot.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
import pandas as pd

from goodgraph.palettes import ACCENT_VERMILLION, CONTROL_GREY, PRIMARY_BLUE
from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, figure_size, save_figure

PATIENTS = ["P01", "P02", "P03"]
COLORS = {
    "P01": CONTROL_GREY,
    "P02": PRIMARY_BLUE,
    "P03": ACCENT_VERMILLION,
}


def main() -> None:
    apply_style()

    df = pd.read_csv(DATA_DIR / "02_dataset.csv")
    doses = df.pivot(index="week", columns="patient_id", values="dose_mg")[PATIENTS]
    weeks = doses.index.to_numpy()

    fig, ax = plt.subplots(
        figsize=figure_size("single", height_mm=72),
        layout="constrained",
    )
    fig.set_constrained_layout_pads(w_pad=0.04, h_pad=0.02)

    for patient in PATIENTS:
        color = COLORS[patient]
        ax.step(
            weeks,
            doses[patient].to_numpy(),
            where="post",
            color=color,
            linewidth=1.8,
            marker="o",
            markersize=3.5,
            markeredgecolor="white",
            markeredgewidth=0.6,
            zorder=3,
        )
        ax.annotate(
            patient,
            (weeks[-1] + 0.18, doses[patient].iloc[-1]),
            ha="left",
            va="center",
            fontsize=7,
            color=color,
            path_effects=[pe.withStroke(linewidth=2.5, foreground="white")],
        )

    ax.set_xlim(-0.2, 13.6)
    ax.set_ylim(0, 8)
    ax.set_xticks(weeks)
    ax.set_xticklabels([str(week) for week in weeks])
    ax.set_yticks([0, 2, 4, 6, 8])

    ax.set_xlabel("Недели")
    ax.set_ylabel("Доза варфарина, мг/сут")
    ax.set_title("Доза варфарина меняется шагами", loc="left", fontsize=9.5, pad=6)

    ax.grid(axis="y", color="#E8E8E8", linewidth=0.6)
    ax.grid(axis="x", visible=False)

    save_figure(fig, "05_02_good_step", formats=("svg", "png"), dpi=600)

    print("\nДозы, использованные на графике:")
    print(doses.to_string())


if __name__ == "__main__":
    main()
