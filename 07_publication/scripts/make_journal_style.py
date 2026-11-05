#!/usr/bin/env python3
"""Генератор журнальных настроек — в диалоге или из пресета.

Примеры
-------
Интерактивно (отвечать Enter — принять значение по умолчанию):

    uv run python 07_publication/scripts/make_journal_style.py --interactive

Без диалога:

    uv run python 07_publication/scripts/make_journal_style.py \
        --preset nature --output build/journal_style_generated.py

Результат — готовый Python-модуль с `JOURNAL` и `apply()` плюс JSON.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from journal_style import PRESETS

FORMAT_CHOICES = ("svg", "pdf", "png", "tiff")


def ask(prompt: str, default: str) -> str:
    value = input(f"{prompt} [{default}]: ").strip()
    return value or default


def ask_int(prompt: str, default: int) -> int:
    while True:
        raw = ask(prompt, str(default))
        try:
            return int(raw)
        except ValueError:
            print("  Нужно целое число.")


def build_config(args: argparse.Namespace) -> dict:
    preset = PRESETS[args.preset]
    cfg = {
        "name": args.preset,
        "label": preset.name,
        "single_mm": preset.single_mm,
        "double_mm": preset.double_mm,
        "font": "Arial",
        "base_pt": preset.base_pt,
        "dpi": preset.dpi,
        "formats": list(preset.formats),
        "palette": "okabe",
        "web_width_px": 960,
        "web_base_px": 16,
    }

    if args.interactive:
        print("\nГенератор журнальных настроек GoodGraph")
        print("Доступные пресеты:")
        for key, item in PRESETS.items():
            print(f"  {key:9s} — {item.note}")
        cfg["name"] = ask("Пресет", args.preset)
        if cfg["name"] not in PRESETS:
            print("  Неизвестный пресет, беру nature.")
            cfg["name"] = "nature"
        chosen = PRESETS[cfg["name"]]
        cfg["label"] = chosen.name
        cfg["single_mm"] = float(ask("Ширина одной колонки, мм", str(chosen.single_mm)))
        cfg["double_mm"] = float(ask("Ширина двух колонок, мм", str(chosen.double_mm)))
        cfg["font"] = ask("Шрифт", "Arial")
        cfg["base_pt"] = float(ask("Базовый кегль, pt", str(chosen.base_pt)))
        cfg["dpi"] = ask_int("DPI для растра", chosen.dpi)
        raw_formats = ask("Форматы через запятую", ",".join(chosen.formats))
        cfg["formats"] = [f.strip().lower() for f in raw_formats.split(",") if f.strip()]
        cfg["palette"] = ask("Палитра (okabe/tol/grey)", "okabe")
        cfg["web_width_px"] = ask_int("Ширина web-канвы, px", 960)
        cfg["web_base_px"] = ask_int("Базовый кегль web, px", 16)

    invalid = [f for f in cfg["formats"] if f not in FORMAT_CHOICES]
    if invalid:
        raise SystemExit(f"Неизвестные форматы: {invalid}; допустимы {FORMAT_CHOICES}")
    return cfg


def make_module(cfg: dict) -> str:
    palette = {
        "okabe": ["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00"],
        "tol": ["#4477AA", "#EE6677", "#228833", "#CCBB44", "#66CCEE", "#AA3377"],
        "grey": ["#333333", "#666666", "#999999", "#BBBBBB", "#DDDDDD", "#F0F0F0"],
    }.get(cfg["palette"], ["#0072B2"])
    return f'''"""Сгенерированные журнальные настройки GoodGraph.

Файл создан `make_journal_style.py`; правьте значения и используйте
`apply()` перед построением рисунка или скопируйте блок в свой модуль.
"""

from __future__ import annotations

import matplotlib as mpl

JOURNAL = {cfg!r}
PALETTE = {palette!r}


def apply() -> None:
    """Применить настройки к текущему matplotlib."""
    mpl.rcParams.update({{
        "font.family": "sans-serif",
        "font.sans-serif": [JOURNAL["font"], "Arial", "Liberation Sans", "DejaVu Sans"],
        "font.size": JOURNAL["base_pt"],
        "axes.labelsize": JOURNAL["base_pt"],
        "xtick.labelsize": JOURNAL["base_pt"] - 1,
        "ytick.labelsize": JOURNAL["base_pt"] - 1,
        "legend.fontsize": JOURNAL["base_pt"] - 1,
        "axes.linewidth": 0.6,
        "lines.linewidth": 1.0,
        "lines.markersize": 3.0,
        "savefig.dpi": JOURNAL["dpi"],
        "savefig.bbox": None,
        "savefig.facecolor": "white",
        "svg.fonttype": "path",
        "pdf.fonttype": 42,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.unicode_minus": False,
    }})
    mpl.rcParams["axes.prop_cycle"] = mpl.cycler(color=PALETTE)
'''


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preset", choices=sorted(PRESETS), default="nature")
    parser.add_argument("--interactive", action="store_true", help="задавать параметры в диалоге")
    parser.add_argument("--output", type=Path, default=Path("build/journal_style_generated.py"))
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()

    cfg = build_config(args)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(make_module(cfg), encoding="utf-8")
    json_path = args.json or args.output.with_suffix(".json")
    json_path.write_text(json.dumps(cfg, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\nГотово: {args.output}")
    print(f"JSON:   {json_path}")
    print(f"Пресет: {cfg['label']}; {cfg['single_mm']} / {cfg['double_mm']} мм; "
          f"{cfg['base_pt']} pt; {cfg['dpi']} dpi")
    print(f"Форматы: {', '.join(cfg['formats'])}; web {cfg['web_width_px']} px, "
          f"{cfg['web_base_px']} px base")


if __name__ == "__main__":
    main()
