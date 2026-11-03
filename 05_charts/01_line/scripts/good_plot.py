#!/usr/bin/env python3
"""«Правильный» линейный график для раздела 5.01.

Что улучшено
------------
1. Ширина 85 мм, высота 72 мм — рисунок спроектирован в конечном размере.
2. Среднее и 95 % ДИ: видна неопределённость, а не только линия.
3. Палитра Okabe–Ito: серый контроль, синий A, вермилион B.
4. Прямые подписи в конце линий вместо легенды.
5. Заголовок-вывод: «Препарат B снижает САД на 20 мм рт. ст. за 12 недель».
6. Единицы, n, равномерные недели 0/4/8/12.
7. Лёгкая сетка только по Y, без верхней и правой рамок.
8. Ось Y 125–160: достаточный контекст, без обрезки «до невозможного».

Выход: images/05_01_good_line.{svg,png}
Запуск: uv run python 05_charts/01_line/scripts/good_plot.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

from goodgraph.palettes import ACCENT_VERMILLION, CONTROL_GREY, PRIMARY_BLUE
from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, figure_size, save_figure

GROUP_ORDER = ["Плацебо", "Препарат A 10 мг", "Препарат B 20 мг"]
GROUP_SHORT = {
    "Плацебо": "Плацебо",
    "Препарат A 10 мг": "A 10 мг",
    "Препарат B 20 мг": "B 20 мг",
}
GROUP_COLORS = {
    "Плацебо": CONTROL_GREY,
    "Препарат A 10 мг": PRIMARY_BLUE,
    "Препарат B 20 мг": ACCENT_VERMILLION,
}
WEEKS = [0, 4, 8, 12]


def summarize(df: pd.DataFrame) -> pd.DataFrame:
    """Среднее и 95 % ДИ для каждой группы и недели."""
    rows = []
    for group in GROUP_ORDER:
        for week in WEEKS:
            values = df.loc[
                (df["group"] == group) & (df["week"] == week), "sbp_mm_hg"
            ].to_numpy()
            n = values.size
            mean = values.mean()
            sd = values.std(ddof=1)
            se = sd / np.sqrt(n)
            half = stats.t.ppf(0.975, df=n - 1) * se
            rows.append(
                {
                    "group": group,
                    "week": week,
                    "n": n,
                    "mean": mean,
                    "ci_low": mean - half,
                    "ci_high": mean + half,
                }
            )
    return pd.DataFrame(rows)


def main() -> None:
    apply_style()
    df = pd.read_csv(DATA_DIR / "01_dataset.csv")
    summary = summarize(df)

    fig, ax = plt.subplots(
        figsize=figure_size("single", height_mm=72),
        layout="constrained",
    )
    fig.set_constrained_layout_pads(w_pad=0.04, h_pad=0.02)

    x = np.arange(len(WEEKS))

    for group in GROUP_ORDER:
        part = summary.loc[summary["group"] == group].sort_values("week")
        color = GROUP_COLORS[group]
        ax.fill_between(
            x,
            part["ci_low"],
            part["ci_high"],
            color=color,
            alpha=0.15,
            linewidth=0,
            zorder=1,
        )
        ax.plot(
            x,
            part["mean"],
            color=color,
            linewidth=1.8,
            marker="o",
            markersize=4.0,
            markeredgecolor="white",
            markeredgewidth=0.7,
            zorder=3,
        )
        ax.annotate(
            GROUP_SHORT[group],
            (x[-1] + 0.08, part["mean"].iloc[-1]),
            ha="left",
            va="center",
            fontsize=7,
            color=color,
            path_effects=[pe.withStroke(linewidth=2.5, foreground="white")],
        )

    ax.set_xlim(-0.1, 3.55)
    ax.set_ylim(125, 160)
    ax.set_xticks(x)
    ax.set_xticklabels([str(week) for week in WEEKS])
    ax.set_yticks([130, 140, 150, 160])

    ax.set_xlabel("Недели")
    ax.set_ylabel("САД, мм рт. ст.")
    ax.set_title(
        "Препарат B снижает САД\nна 20 мм рт. ст. за 12 недель",
        loc="left",
        fontsize=9.5,
        pad=6,
    )

    ax.text(
        0,
        126.0,
        "n = 40 в каждой группе",
        fontsize=6.5,
        color="#666666",
        ha="left",
        va="bottom",
    )

    ax.grid(axis="y", color="#E8E8E8", linewidth=0.6)
    ax.grid(axis="x", visible=False)

    save_figure(fig, "05_01_good_line", formats=("svg", "png"), dpi=600)

    print("\nСводка, использованная на графике:")
    print(summary.round(2).to_string(index=False))


if __name__ == "__main__":
    main()
