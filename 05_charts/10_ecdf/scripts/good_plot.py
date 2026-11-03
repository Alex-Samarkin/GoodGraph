#!/usr/bin/env python3
"""«Правильная» ECDF для раздела 5.10.

Что улучшено
------------
1. Полный диапазон 0–25 дней: видны обе кривые целиком.
2. Синий и вермиллион, прямые подписи вместо легенды.
3. Медианы отмечены пунктиром и подписаны в заголовке.
4. Ось Y в процентах; указаны n и единицы.
5. Лёгкая сетка только по Y, 85 мм.

Выход: images/05_10_good_ecdf.{svg,png}
Запуск: uv run python 05_charts/10_ecdf/scripts/good_plot.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from goodgraph.palettes import ACCENT_VERMILLION, PRIMARY_BLUE
from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, figure_size, save_figure


def ecdf(values: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    xs = np.sort(values)
    ys = np.arange(1, len(xs) + 1) / len(xs) * 100.0
    return xs, ys


def main() -> None:
    apply_style()

    df = pd.read_csv(DATA_DIR / "10_dataset.csv")
    planned = df.loc[df["admission_type"] == "плановое", "los_days"].to_numpy()
    emergency = df.loc[df["admission_type"] == "экстренное", "los_days"].to_numpy()
    med_p = float(np.median(planned))
    med_e = float(np.median(emergency))

    fig, ax = plt.subplots(
        figsize=figure_size("single", height_mm=72),
        layout="constrained",
    )
    fig.set_constrained_layout_pads(w_pad=0.04, h_pad=0.02)

    for values, color, label in [
        (planned, PRIMARY_BLUE, "плановые"),
        (emergency, ACCENT_VERMILLION, "экстренные"),
    ]:
        xs, ys = ecdf(values)
        ax.step(xs, ys, where="post", color=color, linewidth=1.7, label=label)

    ax.text(0.6, 98, "плановые", color=PRIMARY_BLUE, fontsize=7.5, va="top", fontweight="bold")
    ax.text(0.6, 91, "экстренные", color=ACCENT_VERMILLION, fontsize=7.5, va="top")

    ax.axvline(med_p, color=PRIMARY_BLUE, linestyle=(0, (1, 2)), linewidth=0.8, alpha=0.8)
    ax.axvline(med_e, color=ACCENT_VERMILLION, linestyle=(0, (1, 2)), linewidth=0.8, alpha=0.8)

    med_e_text = f"{med_e:.1f}".replace(".", ",")
    ax.set_title(
        f"Экстренные: медиана {med_e_text} vs {med_p:.0f} дней",
        loc="left",
        fontsize=9.5,
        pad=6,
    )

    ax.text(
        24.5,
        3,
        f"n = {len(planned)} + {len(emergency)}",
        fontsize=7,
        color="#333333",
        ha="right",
        va="bottom",
    )

    ax.set_xlim(0, 25)
    ax.set_ylim(0, 100)
    ax.set_xticks([0, 5, 10, 15, 20, 25])
    ax.set_yticks([0, 25, 50, 75, 100])

    ax.set_xlabel("Длительность, дни")
    ax.set_ylabel("Доля пациентов, %")

    ax.grid(axis="y", color="#E8E8E8", linewidth=0.6)
    ax.grid(axis="x", visible=False)

    save_figure(fig, "05_10_good_ecdf", formats=("svg", "png"), dpi=600)
    print(f"Медианы: плановые {med_p:.1f}, экстренные {med_e:.1f}")


if __name__ == "__main__":
    main()
