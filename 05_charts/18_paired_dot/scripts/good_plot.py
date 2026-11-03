#!/usr/bin/env python3
"""«Правильный» paired dot для раздела 5.18.

Что улучшено
------------
1. Серые линии для отдельных пациентов, точки на обоих концах.
2. Средние до/после выделены цветом и толстой линией.
3. Полный диапазон 70–145 г/л.
4. Подписи «До/После», единицы, n = 30.
5. Среднее изменение +12,4 г/л подписано.
6. Заголовок-вывод, 85 мм.

Выход: images/05_18_good_paired_dot.{svg,png}
Запуск: uv run python 05_charts/18_paired_dot/scripts/good_plot.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd

from goodgraph.palettes import ACCENT_VERMILLION, PRIMARY_BLUE
from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, figure_size, save_figure


def main() -> None:
    apply_style()

    df = pd.read_csv(DATA_DIR / "18_dataset.csv")
    before = df["hemoglobin_before"].to_numpy()
    after = df["hemoglobin_after"].to_numpy()
    mean_before = float(before.mean())
    mean_after = float(after.mean())
    mean_change = mean_after - mean_before

    fig, ax = plt.subplots(
        figsize=figure_size("single", height_mm=75),
        layout="constrained",
    )
    fig.set_constrained_layout_pads(w_pad=0.04, h_pad=0.02)

    for b, a in zip(before, after, strict=True):
        ax.plot([0, 1], [b, a], color="#8A8A8A", linewidth=0.9, alpha=0.45, zorder=2)
        ax.scatter([0, 1], [b, a], s=8, color=PRIMARY_BLUE, alpha=0.45,
                   linewidths=0, zorder=3)

    ax.plot([0, 1], [mean_before, mean_after], color=ACCENT_VERMILLION,
            linewidth=2.2, marker="o", markersize=5, zorder=4)
    ax.text(
        0.5,
        (mean_before + mean_after) / 2 + 4,
        f"среднее +{mean_change:.1f} г/л".replace(".", ","),
        color=ACCENT_VERMILLION,
        fontsize=7,
        ha="center",
        va="bottom",
    )

    ax.text(
        0.02,
        0.97,
        f"n = {len(df)}",
        transform=ax.transAxes,
        fontsize=7,
        color="#333333",
        va="top",
    )

    ax.set_xlim(-0.25, 1.25)
    ax.set_ylim(70, 145)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["До", "После"])
    ax.set_yticks([80, 100, 120, 140])

    ax.set_ylabel("Гемоглобин, г/л")
    ax.set_title("Лечение повышает гемоглобин", loc="left", fontsize=9.5, pad=6)

    ax.grid(axis="y", color="#E8E8E8", linewidth=0.6)
    ax.grid(axis="x", visible=False)

    save_figure(fig, "05_18_good_paired_dot", formats=("svg", "png"), dpi=600)

    print(f"Среднее до/после: {mean_before:.1f} / {mean_after:.1f}")
    print(f"Среднее изменение: {mean_change:.1f} г/л")


if __name__ == "__main__":
    main()
