#!/usr/bin/env python3
"""«Плохая» ECDF для раздела 5.10.

Что специально сделано неправильно
----------------------------------
1. Ось X обрезана до 0–12: правый хвост и половина ECDF скрыты.
2. Красно-зелёная пара и легенда: CVD и лишний поиск.
3. Толстые ступени, тяжёлая сетка, полная рамка.
4. Нет медиан, квантилей, единиц и n.
5. Заголовок «Длительность госпитализации» ничего не сообщает.

Выход: images/05_10_bad_ecdf.{svg,png}
Запуск: uv run python 05_charts/10_ecdf/scripts/bad_plot.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, save_figure


def ecdf(values: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    xs = np.sort(values)
    ys = np.arange(1, len(xs) + 1) / len(xs) * 100.0
    return xs, ys


def main() -> None:
    apply_style()

    df = pd.read_csv(DATA_DIR / "10_dataset.csv")
    groups = [
        ("плановое", "#2CA02C"),
        ("экстренное", "#D62728"),
    ]

    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    for group, color in groups:
        values = df.loc[df["admission_type"] == group, "los_days"].to_numpy()
        xs, ys = ecdf(values)
        ax.step(xs, ys, where="post", color=color, linewidth=2.8, label=group)

    ax.set_xlim(0, 12)
    ax.set_ylim(0, 100)

    ax.grid(True, which="major", axis="both", color="#BDBDBD", linewidth=1.0)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1.5)
        spine.set_color("black")

    ax.tick_params(labelsize=12, width=1.4, length=5)
    ax.set_title("Длительность госпитализации", fontsize=18, fontweight="bold")
    ax.set_ylabel("Доля", fontsize=15)
    ax.set_xlabel("Дни", fontsize=15)
    ax.legend(loc="lower right", fontsize=11, frameon=True, edgecolor="black")

    fig.tight_layout()
    save_figure(fig, "05_10_bad_ecdf", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
