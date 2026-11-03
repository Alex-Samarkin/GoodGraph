"""GoodGraph — общий стиль и утилиты для методички по научной графике.

Пакет небольшой и намеренно не прячет matplotlib: он только задаёт
разумные значения rcParams, палитры и правила сохранения рисунков.
Такой подход позволяет читателю видеть, что именно меняется.

Пример
------
>>> from goodgraph import apply_style, figure_size, save_figure
>>> apply_style()
>>> fig, ax = plt.subplots(figsize=figure_size("single"))
>>> ...
>>> save_figure(fig, "example")
"""

from __future__ import annotations

from .palettes import OKABE_ITO, TOL_BRIGHT, TOL_MUTED, okabe_ito, tol_bright
from .paths import DATA_DIR, IMAGES_DIR, ROOT_DIR
from .style import apply_style, figure_size, mm, panel_label, save_figure

__all__ = [
    "DATA_DIR",
    "IMAGES_DIR",
    "ROOT_DIR",
    "OKABE_ITO",
    "TOL_BRIGHT",
    "TOL_MUTED",
    "apply_style",
    "figure_size",
    "mm",
    "okabe_ito",
    "panel_label",
    "save_figure",
    "tol_bright",
]
