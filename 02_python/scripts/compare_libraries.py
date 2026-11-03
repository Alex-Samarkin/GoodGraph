#!/usr/bin/env python3
"""Один и тот же scatter-plot тремя библиотеками.

Зачем этот скрипт
-----------------
Раздел 2 объясняет разницу между императивным matplotlib, дата-ориентированным
seaborn и декларативным plotnine. Чтобы разница не осталась только на словах,
здесь один и тот же набор данных (HbA1c до и после 12 недель, 132 пациента)
рисуется трижды — по одной библиотеке на панель.

Данные генерируются отдельным скриптом `make_data.py` и лежат в
`data/02_python_dataset.csv`. Раздел 2 не переиспользует данные раздела 1:
у каждого раздела и вида графика — свой генератор и свой набор.

Выход
-----
images/02_matplotlib_scatter.{svg,png}
images/02_seaborn_scatter.{svg,png}
images/02_plotnine_scatter.{svg,png}

Запуск
------
uv run python 02_python/scripts/compare_libraries.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")  # без дисплея: скрипт должен работать на сервере и в CI

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from plotnine import (
    aes,
    coord_fixed,
    element_blank,
    element_line,
    element_text,
    geom_abline,
    geom_point,
    ggplot,
    labs,
    scale_color_manual,
    scale_shape_manual,
    scale_x_continuous,
    scale_y_continuous,
    theme,
    theme_bw,
)

from goodgraph.palettes import ACCENT_VERMILLION, CONTROL_GREY, PRIMARY_BLUE
from goodgraph.paths import DATA_DIR, IMAGES_DIR
from goodgraph.style import apply_style, figure_size, save_figure

# Размер одной панели: три панели по 54 мм образуют журнальную ширину 170 мм.
WIDTH_MM = 54
HEIGHT_MM = 62

# Общие пределы и деления, чтобы панели были сравнимы.
LIM_MIN, LIM_MAX = 4.5, 11.5
TICKS = [6, 8, 10]

GROUP_ORDER = ["Плацебо", "Препарат A 10 мг", "Препарат B 20 мг"]
GROUP_COLORS = {
    "Плацебо": CONTROL_GREY,
    "Препарат A 10 мг": PRIMARY_BLUE,
    "Препарат B 20 мг": ACCENT_VERMILLION,
}
# Форма маркера дублирует цвет: панель остаётся читаемой в оттенках серого.
GROUP_MARKERS = {
    "Плацебо": "o",
    "Препарат A 10 мг": "^",
    "Препарат B 20 мг": "s",
}


def load_data() -> pd.DataFrame:
    """Прочитать общий CSV и проверить, что все группы на месте."""
    df = pd.read_csv(DATA_DIR / "02_python_dataset.csv")
    missing = set(GROUP_ORDER) - set(df["group"].unique())
    if missing:
        raise ValueError(f"В данных нет групп: {sorted(missing)}")
    return df


def style_axes(ax: plt.Axes, title: str) -> None:
    """Единое оформление осей для matplotlib и seaborn."""
    ax.plot(
        [LIM_MIN, LIM_MAX],
        [LIM_MIN, LIM_MAX],
        color="#7F7F7F",
        linewidth=0.4,
        linestyle=(0, (3, 2)),
        zorder=1,
    )
    ax.set_xlim(LIM_MIN, LIM_MAX)
    ax.set_ylim(LIM_MIN, LIM_MAX)
    ax.set_xticks(TICKS)
    ax.set_yticks(TICKS)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("HbA1c до, %")
    ax.set_ylabel("HbA1c после, %")
    ax.set_title(title, fontsize=7.5, pad=3, loc="center")
    ax.grid(True, which="major", axis="both", color="#E8E8E8", linewidth=0.3)
    ax.tick_params(labelsize=6.5, length=2.5, width=0.5)


def plot_matplotlib(df: pd.DataFrame) -> None:
    """Императивный подход: сами создаём Figure, Axes и каждый слой."""
    apply_style(font_size=7)
    fig, ax = plt.subplots(
        figsize=figure_size(WIDTH_MM, height_mm=HEIGHT_MM),
        layout="constrained",
    )
    fig.set_constrained_layout_pads(w_pad=0.02, h_pad=0.02)

    for group in GROUP_ORDER:
        part = df.loc[df["group"] == group]
        ax.scatter(
            part["baseline_hba1c_pct"],
            part["followup_hba1c_pct"],
            s=9,
            marker=GROUP_MARKERS[group],
            color=GROUP_COLORS[group],
            alpha=0.5,
            linewidths=0,
            zorder=2,
        )

    style_axes(ax, "A · matplotlib")
    save_figure(fig, "02_matplotlib_scatter", formats=("svg", "png"), dpi=600)


def plot_seaborn(df: pd.DataFrame) -> None:
    """Дата-ориентированный подход: одна функция, данные в long-формате."""
    apply_style(font_size=7)
    fig, ax = plt.subplots(
        figsize=figure_size(WIDTH_MM, height_mm=HEIGHT_MM),
        layout="constrained",
    )
    fig.set_constrained_layout_pads(w_pad=0.02, h_pad=0.02)

    sns.scatterplot(
        data=df,
        x="baseline_hba1c_pct",
        y="followup_hba1c_pct",
        hue="group",
        style="group",
        hue_order=GROUP_ORDER,
        style_order=GROUP_ORDER,
        palette=GROUP_COLORS,
        markers=GROUP_MARKERS,
        s=9,
        alpha=0.5,
        linewidth=0,
        legend=False,
        ax=ax,
    )

    style_axes(ax, "B · seaborn")
    save_figure(fig, "02_seaborn_scatter", formats=("svg", "png"), dpi=600)


def plot_plotnine(df: pd.DataFrame) -> None:
    """Декларативный подход: грамматика графики, слои через «+»."""
    apply_style(font_size=7)

    plot = (
        ggplot(
            df,
            aes(
                x="baseline_hba1c_pct",
                y="followup_hba1c_pct",
                color="group",
                shape="group",
            ),
        )
        + geom_point(size=1.2, alpha=0.5, stroke=0)
        + geom_abline(
            slope=1,
            intercept=0,
            linetype="dashed",
            color="#7F7F7F",
            size=0.4,
        )
        + scale_color_manual(values=GROUP_COLORS)
        + scale_shape_manual(values=GROUP_MARKERS)
        + scale_x_continuous(breaks=TICKS)
        + scale_y_continuous(breaks=TICKS)
        + coord_fixed(ratio=1, xlim=(LIM_MIN, LIM_MAX), ylim=(LIM_MIN, LIM_MAX))
        + labs(
            x="HbA1c до, %",
            y="HbA1c после, %",
            title="C · plotnine",
        )
        + theme_bw()
        + theme(
            text=element_text(family="Liberation Sans", size=7, color="#333333"),
            plot_title=element_text(size=7.5, ha="center", margin={"t": 0, "b": 2}),
            axis_title=element_text(size=7),
            axis_text=element_text(size=6.5),
            panel_grid_major=element_line(color="#E8E8E8", linewidth=0.3),
            panel_grid_minor=element_blank(),
            panel_border=element_blank(),
            axis_line=element_line(color="#4D4D4D", linewidth=0.4),
            legend_position="none",
            plot_margin=0.02,
        )
    )

    size = {"width": WIDTH_MM / 25.4, "height": HEIGHT_MM / 25.4, "dpi": 600}
    for fmt in ("svg", "png"):
        path = IMAGES_DIR / f"02_plotnine_scatter.{fmt}"
        plot.save(str(path), **size, verbose=False, metadata={"Date": None})
        print(f"  ✓ {path}")


def main() -> None:
    df = load_data()
    plot_matplotlib(df)
    plot_seaborn(df)
    plot_plotnine(df)
    print(f"\nГотово: три панели по {WIDTH_MM}×{HEIGHT_MM} мм, данные — {len(df)} строк.")


if __name__ == "__main__":
    main()
