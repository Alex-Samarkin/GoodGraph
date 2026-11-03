#!/usr/bin/env python3
"""«Правильный» slope plot для раздела 5.17.

Что улучшено
------------
1. Серые линии для всех клиник, акцент на лидере.
2. Прямые подписи слева и справа, с лидер-линиями.
3. Полный диапазон 80–105 кг.
4. Подписи «До/После», единицы, n, изменение в кг.
5. Заголовок-вывод: все клиники снизили вес.
6. 120 мм — хватает места для подписей.

Выход: images/05_17_good_slope.{svg,png}
Запуск: uv run python 05_charts/17_slope/scripts/good_plot.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from goodgraph.palettes import ACCENT_VERMILLION
from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, save_figure


def spread(values: np.ndarray, min_gap: float) -> np.ndarray:
    """Развести подписи по вертикали, сохраняя порядок."""
    order = np.argsort(values)
    positions = np.array(values, dtype=float)
    for previous, current in zip(order[:-1], order[1:], strict=True):
        if positions[current] - positions[previous] < min_gap:
            positions[current] = positions[previous] + min_gap
    return positions


def main() -> None:
    apply_style(font_size=7)

    df = pd.read_csv(DATA_DIR / "17_dataset.csv")
    summary = (
        df.groupby("clinic")[["weight_before_kg", "weight_after_kg"]]
        .mean()
        .assign(change=lambda x: x["weight_after_kg"] - x["weight_before_kg"])
        .sort_values("weight_before_kg", ascending=False)
    )

    before = summary["weight_before_kg"].to_numpy()
    after = summary["weight_after_kg"].to_numpy()
    change = summary["change"].to_numpy()
    left_y = spread(before, 2.4)
    right_y = spread(after, 2.4)
    leader = int(np.argmin(change))

    fig, ax = plt.subplots(figsize=(120 / 25.4, 85 / 25.4))
    fig.subplots_adjust(left=0.27, right=0.78, top=0.86, bottom=0.16)

    for index, (clinic, row) in enumerate(summary.iterrows()):
        color = ACCENT_VERMILLION if index == leader else "#8A8A8A"
        alpha = 1.0 if index == leader else 0.55
        ax.plot(
            [0, 1],
            [row["weight_before_kg"], row["weight_after_kg"]],
            color=color,
            linewidth=2.0 if index == leader else 1.2,
            alpha=alpha,
            marker="o",
            markersize=4,
            zorder=3,
        )
        ax.annotate(
            f"{clinic}  {row['weight_before_kg']:.0f}",
            xy=(0, row["weight_before_kg"]),
            xytext=(-0.10, left_y[index]),
            ha="right",
            va="center",
            fontsize=6.4,
            color="#333333",
            arrowprops={"arrowstyle": "-", "color": "#BBBBBB", "lw": 0.4},
        )
        sign = "+" if row["change"] > 0 else "−"
        ax.annotate(
            f"{row['weight_after_kg']:.0f}  ({sign}{abs(row['change']):.1f})",
            xy=(1, row["weight_after_kg"]),
            xytext=(1.10, right_y[index]),
            ha="left",
            va="center",
            fontsize=6.4,
            color=ACCENT_VERMILLION if index == leader else "#333333",
            fontweight="bold" if index == leader else "normal",
            arrowprops={"arrowstyle": "-", "color": "#BBBBBB", "lw": 0.4},
        )

    ax.set_xlim(-0.55, 1.55)
    ax.set_ylim(80, 106)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["До", "После"])
    ax.set_yticks([80, 85, 90, 95, 100, 105])

    ax.set_ylabel("Вес, кг")
    overall_change = float(change.mean())
    ax.set_title(
        f"Все клиники снизили вес: в среднем на {abs(overall_change):.1f} кг"
        .replace(".", ","),
        loc="left",
        fontsize=9,
        pad=8,
    )

    ax.text(
        0.99,
        0.01,
        f"n = {len(df) // len(summary)} в каждой клинике",
        transform=ax.transAxes,
        fontsize=6,
        color="#555555",
        ha="right",
        va="bottom",
    )

    ax.grid(axis="y", color="#E8E8E8", linewidth=0.6)
    ax.grid(axis="x", visible=False)

    save_figure(fig, "05_17_good_slope", formats=("svg", "png"), dpi=600)


if __name__ == "__main__":
    main()
