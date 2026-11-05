#!/usr/bin/env python3
"""Журнальные и веб-настройки GoodGraph.

Модуль не «магия», а набор явных пресетов и функций экспорта.
Его можно импортировать из своих скриптов или взять за основу
сгенерированного файла (см. make_journal_style.py).

Пример
------
>>> from journal_style import apply_journal_style, export_journal
>>> apply_journal_style("nature", base_size=7)
>>> export_journal(fig, "07_journal_figure")
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt

from goodgraph.palettes import LIGHT_GRID, TEXT_GREY, okabe_ito
from goodgraph.paths import IMAGES_DIR


@dataclass(frozen=True)
class JournalPreset:
    """Параметры одного журнального/веб-пресета."""

    name: str
    single_mm: float
    double_mm: float
    base_pt: float
    dpi: int
    formats: tuple[str, ...]
    note: str


PRESETS: dict[str, JournalPreset] = {
    "nature": JournalPreset("Nature", 89.0, 183.0, 7.0, 600, ("svg", "pdf", "png", "tiff"),
                            "7 pt, одна колонка 89 мм, две 183 мм"),
    "elsevier": JournalPreset("Elsevier", 90.0, 190.0, 8.0, 600, ("svg", "pdf", "png", "tiff"),
                              "8 pt, 90/190 мм, обычно TIFF/PDF"),
    "ieee": JournalPreset("IEEE", 88.9, 181.0, 8.0, 600, ("pdf", "png", "tiff"),
                          "8 pt, 3.5/7.16 in, PDF/TIFF"),
    "web": JournalPreset("Web/HTML", 160.0, 320.0, 12.0, 160, ("svg", "png"),
                         "960–1200 px, sRGB, 1x/2x"),
}


def apply_journal_style(preset: str = "nature", base_pt: float | None = None) -> JournalPreset:
    """Применить rcParams журнального пресета и вернуть его параметры."""
    if preset not in PRESETS:
        raise ValueError(f"Неизвестный пресет: {preset}. Доступны: {sorted(PRESETS)}")
    cfg = PRESETS[preset]
    size = float(base_pt or cfg.base_pt)

    mpl.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Arial", "Helvetica", "Liberation Sans", "DejaVu Sans"],
            "font.size": size,
            "axes.titlesize": size + 1,
            "axes.labelsize": size,
            "xtick.labelsize": size - 1,
            "ytick.labelsize": size - 1,
            "legend.fontsize": size - 1,
            "axes.linewidth": 0.6,
            "axes.edgecolor": "#333333",
            "axes.labelcolor": TEXT_GREY,
            "xtick.color": TEXT_GREY,
            "ytick.color": TEXT_GREY,
            "text.color": TEXT_GREY,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": True,
            "axes.grid.axis": "y",
            "axes.axisbelow": True,
            "grid.color": LIGHT_GRID,
            "grid.linewidth": 0.4,
            "lines.linewidth": 1.0,
            "lines.markersize": 3.0,
            "errorbar.capsize": 2.0,
            "legend.frameon": False,
            "figure.dpi": 150,
            "savefig.dpi": cfg.dpi,
            "savefig.facecolor": "white",
            "savefig.edgecolor": "white",
            "savefig.bbox": None,
            "svg.fonttype": "path",
            "svg.hashsalt": "goodgraph",
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "axes.unicode_minus": False,
            "axes.titlelocation": "left",
        }
    )
    mpl.rcParams["axes.prop_cycle"] = mpl.cycler(color=okabe_ito(6))
    return cfg


def export_journal(
    fig: plt.Figure,
    stem: str,
    *,
    outdir: str | Path = IMAGES_DIR,
    formats: tuple[str, ...] = ("svg", "pdf", "png", "tiff"),
    dpi: int | None = None,
) -> list[Path]:
    """Экспортировать рисунок в журнальных форматах без обрезки полей."""
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for fmt in formats:
        path = outdir / f"{stem}.{fmt}"
        metadata = None
        if fmt == "svg":
            metadata = {"Creator": "GoodGraph", "Date": None}
        elif fmt == "pdf":
            metadata = {"Creator": "GoodGraph", "CreationDate": None}
        kwargs = {}
        if fmt == "tiff":
            kwargs["pil_kwargs"] = {"compression": "tiff_lzw"}
        fig.savefig(
            path,
            format=fmt,
            dpi=dpi or mpl.rcParams["savefig.dpi"],
            facecolor="white",
            bbox_inches=None,
            pad_inches=0,
            metadata=metadata,
            **kwargs,
        )
        written.append(path)
    return written


def web_figsize(width_px: int = 960, height_px: int = 540, dpi: int = 160) -> tuple[float, float]:
    """Размер figure в дюймах для веб-канвы заданного размера в px."""
    return width_px / dpi, height_px / dpi


def apply_web_style(base_px: int = 16, dpi: int = 160) -> None:
    """Настройки под HTML: px-ориентированные кегли, sRGB, PNG/SVG."""
    base_pt = base_px * 72.0 / dpi
    mpl.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Inter", "Arial", "Helvetica", "DejaVu Sans"],
            "font.size": base_pt,
            "axes.labelsize": base_pt,
            "xtick.labelsize": base_pt - 1,
            "ytick.labelsize": base_pt - 1,
            "legend.fontsize": base_pt - 1,
            "axes.linewidth": 0.8,
            "lines.linewidth": 1.6,
            "lines.markersize": 4.0,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": True,
            "axes.grid.axis": "y",
            "grid.color": LIGHT_GRID,
            "grid.linewidth": 0.6,
            "figure.dpi": 100,
            "savefig.dpi": dpi,
            "savefig.bbox": None,
            "savefig.facecolor": "white",
            "svg.fonttype": "path",
            "svg.hashsalt": "goodgraph",
            "axes.unicode_minus": False,
        }
    )
    mpl.rcParams["axes.prop_cycle"] = mpl.cycler(color=okabe_ito(6))


def export_web(fig: plt.Figure, stem: str, *, outdir: str | Path = IMAGES_DIR,
               dpi: int = 160) -> list[Path]:
    """Сохранить PNG 1x и 2x для HTML (размер figure задаёт дизайнер)."""
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    written = []
    for suffix, scale in [("", 1), ("@2x", 2)]:
        path = outdir / f"{stem}{suffix}.png"
        fig.savefig(path, dpi=dpi * scale, facecolor="white", bbox_inches=None, pad_inches=0)
        written.append(path)
    return written
