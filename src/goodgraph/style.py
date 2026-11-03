"""Единый стиль научной графики.

Философия модуля
----------------
1. Ничего не скрывать: все настройки — это обычные rcParams, их видно
   и можно переопределить в любой момент.
2. Один стиль на всю методичку: одинаковые шрифты, толщины, палитра,
   поля и правила сохранения.
3. Размеры — в миллиметрах, потому что журналы задают ширину колонки
   в миллиметрах, а не в дюймах.

Типичный сценарий::

    from goodgraph import apply_style, figure_size, save_figure

    apply_style()                       # «бумажный» контекст, 9 pt
    fig, ax = plt.subplots(figsize=figure_size("single", ratio=0.85))
    ...
    save_figure(fig, "01_good_example")  # images/*.svg и *.png
"""

from __future__ import annotations

import matplotlib as mpl
import matplotlib.pyplot as plt

from .palettes import (
    CONTROL_GREY,
    LIGHT_GRID,
    OKABE_ITO,
    PRIMARY_BLUE,
    TEXT_GREY,
    okabe_ito,
)
from .paths import IMAGES_DIR

# Физические ширины, которые чаще всего требуют журналы.
# 85 мм — одна колонка, 114 мм — полторы, 170–180 мм — две колонки.
FIGURE_WIDTHS_MM: dict[str, float] = {
    "single": 85.0,
    "one_half": 114.0,
    "double": 170.0,
    "max": 180.0,
}

# Базовые размеры шрифта для разных носителей.
_CONTEXT_FONT_SIZE = {
    "paper": 9.0,
    "slide": 14.0,
    "poster": 20.0,
}


def mm(value: float) -> float:
    """Перевести миллиметры в дюймы (единицы matplotlib)."""
    return value / 25.4


def figure_size(
    width: str | float = "single",
    *,
    height_mm: float | None = None,
    ratio: float = 0.72,
) -> tuple[float, float]:
    """Размер рисунка в дюймах по ширине колонки журнала.

    Parameters
    ----------
    width:
        ``"single"`` (85 мм), ``"one_half"`` (114 мм), ``"double"`` (170 мм),
        ``"max"`` (180 мм) или число миллиметров.
    height_mm:
        Высота в миллиметрах. Если не задана, вычисляется как
        ``ширина * ratio``.
    ratio:
        Доля высоты от ширины. 0.72 — близко к «золотому» и удобно
        для большинства точечных и столбчатых графиков.

    Examples
    --------
    >>> figure_size("single")
    (3.346..., 2.409...)
    """
    width_mm = FIGURE_WIDTHS_MM.get(width, width) if isinstance(width, str) else width
    if not isinstance(width_mm, (int, float)):
        raise ValueError(f"Неизвестная ширина: {width!r}")
    if height_mm is None:
        height_mm = width_mm * ratio
    return mm(width_mm), mm(height_mm)


def apply_style(
    context: str = "paper",
    *,
    font_size: float | None = None,
    font_family: str | None = None,
    grid: bool = True,
) -> None:
    """Применить стиль GoodGraph.

    Parameters
    ----------
    context:
        ``"paper"`` (9 pt), ``"slide"`` (14 pt) или ``"poster"`` (20 pt).
    font_size:
        Явный базовый размер шрифта; переопределяет ``context``.
    font_family:
        Основная гарнитура. По умолчанию Liberation Sans — метрический
        аналог Arial, с полной поддержкой кириллицы.
    grid:
        Включать ли лёгкую сетку по оси Y. Для «чистых» графиков
        без сетки передайте ``grid=False``.
    """
    if context not in _CONTEXT_FONT_SIZE:
        raise ValueError(f"context должен быть одним из {list(_CONTEXT_FONT_SIZE)}")

    base = float(font_size if font_size is not None else _CONTEXT_FONT_SIZE[context])
    family = font_family or "Liberation Sans"

    mpl.rcParams.update(
        {
            # --- Шрифты -------------------------------------------------
            "font.family": "sans-serif",
            "font.sans-serif": [family, "Arial", "Helvetica", "DejaVu Sans", "Nimbus Sans"],
            "font.size": base,
            "axes.titlesize": base + 1,
            "axes.titleweight": "normal",
            "axes.titlelocation": "left",
            "axes.titlepad": 8,
            "axes.labelsize": base,
            "axes.labelpad": 4,
            "xtick.labelsize": base - 1,
            "ytick.labelsize": base - 1,
            "legend.fontsize": base - 1,
            "figure.titlesize": base + 2,
            "mathtext.fontset": "dejavusans",
            # --- Цвета и текст ------------------------------------------
            "text.color": TEXT_GREY,
            "axes.labelcolor": TEXT_GREY,
            "axes.edgecolor": "#4D4D4D",
            "xtick.color": "#4D4D4D",
            "ytick.color": "#4D4D4D",
            "axes.linewidth": 0.8,
            "axes.unicode_minus": False,
            # --- Оси, сетка, рамки --------------------------------------
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": grid,
            "axes.grid.axis": "y",
            "axes.axisbelow": True,
            "grid.color": LIGHT_GRID,
            "grid.linewidth": 0.6,
            "grid.alpha": 1.0,
            "xtick.direction": "out",
            "ytick.direction": "out",
            "xtick.major.size": 3.0,
            "ytick.major.size": 3.0,
            "xtick.major.width": 0.8,
            "ytick.major.width": 0.8,
            # --- Линии и маркеры ----------------------------------------
            "lines.linewidth": 1.8,
            "lines.markersize": 5.0,
            "errorbar.capsize": 3.0,
            "patch.linewidth": 0.8,
            # --- Легенда -------------------------------------------------
            "legend.frameon": False,
            "legend.handlelength": 2.0,
            "legend.borderaxespad": 0.2,
            # --- Рисунок и сохранение -----------------------------------
            "figure.dpi": 110,
            "savefig.dpi": 600,
            "savefig.facecolor": "white",
            "savefig.edgecolor": "white",
            "svg.fonttype": "path",   # текст в SVG превращается в кривые
            "svg.hashsalt": "goodgraph",  # воспроизводимые id в SVG
            "pdf.fonttype": 42,       # TrueType, текст остаётся редактируемым
            "ps.fonttype": 42,
        }
    )

    # Цветовой цикл: первые цвета Okabe–Ito, без чёрного.
    mpl.rcParams["axes.prop_cycle"] = mpl.cycler(color=okabe_ito(6))


def panel_label(
    ax: plt.Axes,
    label: str,
    *,
    x: float = -0.14,
    y: float = 1.04,
    fontsize: float | None = None,
) -> None:
    """Поставить метку панели (A, B, C…) слева над осями.

    Метка выровнена по левому краю и не перекрывает заголовок.
    """
    ax.text(
        x,
        y,
        label,
        transform=ax.transAxes,
        fontsize=fontsize or mpl.rcParams["font.size"] + 1,
        fontweight="bold",
        va="bottom",
        ha="left",
        color=TEXT_GREY,
        clip_on=False,
    )


def save_figure(
    fig: plt.Figure,
    stem: str,
    *,
    outdir=IMAGES_DIR,
    formats: tuple[str, ...] = ("svg", "png"),
    dpi: int = 600,
    tight: bool = False,
    pad_inches: float = 0.02,
) -> list[str]:
    """Сохранить рисунок в нескольких форматах и закрыть его.

    Parameters
    ----------
    fig:
        Объект ``matplotlib.figure.Figure``.
    stem:
        Имя файла без расширения, например ``"01_good_dot_ci"``.
    outdir:
        Каталог назначения; по умолчанию общий ``images/``.
    formats:
        Форматы. По умолчанию SVG (вектор) и PNG (растр для просмотра).
    dpi:
        Разрешение растра. 600 dpi достаточно для растровых вставок;
        для чисто векторных журнальных рисунков DPI не важен.
    tight:
        Обрезать поля по содержимому. Включайте осознанно: при этом
        физический размер рисунка перестаёт быть ровно 85/170 мм.
    pad_inches:
        Поля при ``tight=True``.

    Returns
    -------
    list[str]
        Пути сохранённых файлов.
    """
    outdir.mkdir(parents=True, exist_ok=True)
    paths: list[str] = []
    for fmt in formats:
        path = outdir / f"{stem}.{fmt}"
        fig.savefig(
            path,
            format=fmt,
            dpi=dpi,
            bbox_inches="tight" if tight else None,
            pad_inches=pad_inches if tight else None,
            facecolor="white",
            metadata={"Date": None} if fmt == "svg" else None,
        )
        paths.append(str(path))
    plt.close(fig)
    for path in paths:
        print(f"  ✓ {path}")
    return paths


# Удобные псевдонимы для читателя.
__all__ = [
    "FIGURE_WIDTHS_MM",
    "apply_style",
    "figure_size",
    "mm",
    "panel_label",
    "save_figure",
    "CONTROL_GREY",
    "LIGHT_GRID",
    "OKABE_ITO",
    "PRIMARY_BLUE",
]
