#!/usr/bin/env python3
"""«Правильный» график для раздела 1: те же данные, другой смысл.

Что улучшено
------------
1. Нулевая линия и точечная оценка: положение, а не длина, поэтому
   обрезать ось не нужно — но и ложной разницы не возникает.
2. Показаны индивидуальные наблюдения, среднее и 95 % ДИ: виден разброс,
   а не только «среднее в столбике».
3. Палитра Okabe–Ito: серый контроль, синий и вермилион — различимы
   при дальтонизме и в оттенках серого.
4. Прямые подписи групп вместо легенды; n указано рядом с группой.
5. Лёгкая сетка только по Y, без верхней и правой рамок.
6. Заголовок сформулирован как вывод, а не как «результаты».
7. Указаны единицы измерения; десятичная запятая — как в русском тексте.
8. Ширина 85 мм (одна журнальная колонка), кегли 7–9 pt.

Файл: images/01_good_dot_ci.{svg,png}
Запуск: uv run python 01_principles/scripts/good_plot.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd
from scipy import stats

from goodgraph.palettes import ACCENT_VERMILLION, CONTROL_GREY, PRIMARY_BLUE
from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, figure_size, save_figure

GROUP_ORDER = ["Плацебо", "Препарат A 10 мг", "Препарат B 20 мг"]
GROUP_SHORT = {
    "Плацебо": "Плацебо",
    "Препарат A 10 мг": "Препарат A\n10 мг",
    "Препарат B 20 мг": "Препарат B\n20 мг",
}
GROUP_COLORS = {
    "Плацебо": CONTROL_GREY,
    "Препарат A 10 мг": PRIMARY_BLUE,
    "Препарат B 20 мг": ACCENT_VERMILLION,
}


def summarize(df: pd.DataFrame) -> pd.DataFrame:
    """Среднее, SD, n и 95 % доверительный интервал (t-распределение)."""
    rows = []
    for group in GROUP_ORDER:
        values = df.loc[df["group"] == group, "change_sbp_mm_hg"].to_numpy()
        n = values.size
        mean = values.mean()
        sd = values.std(ddof=1)
        se = sd / np.sqrt(n)
        half_width = stats.t.ppf(0.975, df=n - 1) * se
        rows.append(
            {
                "group": group,
                "n": n,
                "mean": mean,
                "sd": sd,
                "ci_low": mean - half_width,
                "ci_high": mean + half_width,
            }
        )
    return pd.DataFrame(rows).set_index("group")


def main() -> None:
    apply_style()
    df = pd.read_csv(DATA_DIR / "00_dataset.csv")
    summary = summarize(df)

    # Точная физическая ширина: 85 мм, высота — 90 % ширины.
    fig, ax = plt.subplots(
        figsize=figure_size("single", ratio=0.90),
        layout="constrained",
    )
    # Небольшой внутренний отступ, чтобы подписи не прилипали к краю.
    fig.set_constrained_layout_pads(w_pad=0.05, h_pad=0.02)

    rng = np.random.default_rng(7)
    x = np.arange(len(GROUP_ORDER))

    # 1. Индивидуальные наблюдения: полупрозрачные точки с горизонтальным джиттером.
    for i, group in enumerate(GROUP_ORDER):
        values = df.loc[df["group"] == group, "change_sbp_mm_hg"].to_numpy()
        jitter = rng.uniform(-0.12, 0.12, size=values.size)
        ax.scatter(
            i + jitter,
            values,
            s=11,
            color=GROUP_COLORS[group],
            alpha=0.30,
            linewidths=0,
            zorder=2,
        )

    # 2. Среднее и 95 % ДИ.
    for i, group in enumerate(GROUP_ORDER):
        row = summary.loc[group]
        ax.errorbar(
            i,
            row["mean"],
            yerr=[[row["mean"] - row["ci_low"]], [row["ci_high"] - row["mean"]]],
            fmt="o",
            color=GROUP_COLORS[group],
            markersize=6.5,
            markeredgecolor="white",
            markeredgewidth=0.9,
            elinewidth=1.3,
            capsize=3,
            capthick=1.1,
            zorder=4,
        )
        ax.annotate(
            f"{row['mean']:.1f}".replace(".", ","),
            (i, row["ci_high"]),
            xytext=(0, 4),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=8,
            fontweight="bold",
            color=GROUP_COLORS[group],
            path_effects=[pe.withStroke(linewidth=2.5, foreground="white")],
        )

    # 3. Нулевая линия: отсутствие изменения.
    ax.axhline(0, color="#7F7F7F", linewidth=0.8, linestyle=(0, (3, 2)), zorder=1)

    # 4. Оси и подписи.
    y_min = min(df["change_sbp_mm_hg"].min(), 0) - 1
    y_max = max(df["change_sbp_mm_hg"].max(), summary["ci_high"].max()) + 4
    ax.set_ylim(np.floor(y_min), np.ceil(y_max))
    ax.yaxis.set_major_locator(mticker.MultipleLocator(10))
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"{v:g}".replace(".", ",")))

    ax.set_ylabel("Изменение САД, мм рт. ст.")
    ax.set_xlim(-0.45, 2.45)
    ax.set_xticks(x)
    ax.set_xticklabels(
        [f"{GROUP_SHORT[g]}\nn = {summary.loc[g, 'n']}" for g in GROUP_ORDER],
        fontsize=7.5,
    )
    ax.tick_params(axis="x", length=0, pad=5)

    ax.set_title(
        "Препарат B снижает САД\nвдвое сильнее плацебо",
        loc="left",
        fontsize=9.5,
        pad=6,
    )

    # 5. Аккуратные рамки и сетка.
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_linewidth(0.8)
        ax.spines[side].set_color("#4D4D4D")
    ax.grid(axis="y", color="#E8E8E8", linewidth=0.6)
    ax.grid(axis="x", visible=False)

    save_figure(fig, "01_good_dot_ci", formats=("svg", "png"), dpi=600)

    print("\nСводка, использованная на графике:")
    print(summary.round(2).to_string())


if __name__ == "__main__":
    main()
