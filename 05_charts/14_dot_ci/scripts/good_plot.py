#!/usr/bin/env python3
"""«Правильный» dot + CI для раздела 5.14.

Что улучшено
------------
1. 95 % доверительный интервал Уилсона для каждой доли.
2. Полный диапазон 0–35 %.
3. Один цвет, точки и усы без радуги.
4. Общая доля — пунктирная линия и подпись.
5. Сортировка по доле, единицы, n = 100.
6. Лёгкая сетка только по X, 85 мм.

Выход: images/05_14_good_dot_ci.{svg,png}
Запуск: uv run python 05_charts/14_dot_ci/scripts/good_plot.py
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

Z = 1.96


def wilson_ci(successes: int, n: int, z: float = Z) -> tuple[float, float]:
    """95 % доверительный интервал Уилсона для доли (в процентах)."""
    p = successes / n
    denominator = 1 + z**2 / n
    center = (p + z**2 / (2 * n)) / denominator
    half = z * np.sqrt(p * (1 - p) / n + z**2 / (4 * n**2)) / denominator
    return (center - half) * 100, (center + half) * 100


def main() -> None:
    apply_style()

    df = pd.read_csv(DATA_DIR / "14_dataset.csv")
    summary = (
        df.groupby("center")["complication"]
        .agg(["count", "sum", "mean"])
        .sort_values("mean")
    )
    overall = df["complication"].mean() * 100

    fig, ax = plt.subplots(
        figsize=figure_size("single", height_mm=75),
        layout="constrained",
    )
    fig.set_constrained_layout_pads(w_pad=0.04, h_pad=0.02)

    for y, (_, row) in enumerate(summary.iterrows()):
        n = int(row["count"])
        successes = int(row["sum"])
        p = row["mean"] * 100
        low, high = wilson_ci(successes, n)
        ax.errorbar(
            p,
            y,
            xerr=[[p - low], [high - p]],
            fmt="o",
            color=PRIMARY_BLUE,
            ecolor=PRIMARY_BLUE,
            markersize=5,
            elinewidth=1.2,
            capsize=0,
            zorder=3,
        )

    ax.axvline(
        overall,
        color=ACCENT_VERMILLION,
        linestyle=(0, (3, 2)),
        linewidth=0.9,
        zorder=2,
    )
    overall_text = f"{overall:.1f}".replace(".", ",")
    ax.text(
        overall + 0.8,
        len(summary) - 0.55,
        f"всего {overall_text} %",
        color=ACCENT_VERMILLION,
        fontsize=6.5,
        va="top",
    )

    ax.set_xlim(0, 35)
    ax.set_ylim(-0.6, len(summary) - 0.4)
    ax.set_yticks(range(len(summary)))
    ax.set_yticklabels(summary.index)
    ax.set_xticks([0, 10, 20, 30])

    ax.set_xlabel("Доля осложнений, %")
    ax.set_title("Доля осложнений с 95 % ДИ", loc="left", fontsize=9.5, pad=6)

    ax.text(
        34,
        -0.45,
        "n = 100 в каждом центре",
        fontsize=6.5,
        color="#333333",
        ha="right",
        va="bottom",
    )

    ax.grid(axis="x", color="#E8E8E8", linewidth=0.6)
    ax.grid(axis="y", visible=False)

    save_figure(fig, "05_14_good_dot_ci", formats=("svg", "png"), dpi=600)

    print(f"Общая доля: {overall:.1f} %")
    for center, row in summary.iterrows():
        low, high = wilson_ci(int(row["sum"]), int(row["count"]))
        print(f"{center}: {row['mean'] * 100:.1f} % (95 % ДИ {low:.1f}–{high:.1f})")


if __name__ == "__main__":
    main()
