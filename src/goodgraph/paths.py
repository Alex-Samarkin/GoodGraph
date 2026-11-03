"""Пути проекта.

Все скрипты обращаются к данным и рисункам через эти константы, а не через
хрупкие относительные пути вида ``../../data``. Это позволяет запускать
скрипты из любой рабочей директории.
"""

from __future__ import annotations

from pathlib import Path

# src/goodgraph/paths.py → parents[2] = корень репозитория
ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "data"
IMAGES_DIR = ROOT_DIR / "images"

# Создаём каталоги при импорте: скриптам не нужно об этом думать.
DATA_DIR.mkdir(parents=True, exist_ok=True)
IMAGES_DIR.mkdir(parents=True, exist_ok=True)
