#!/usr/bin/env python3
"""Данные для раздела 5.15: госпитализации по отделениям за год.

Сценарий
--------
Пять отделений больницы, число госпитализаций за год. Величины —
счётчики, поэтому столбцы уместны: сравниваются абсолютные объёмы.

Данные синтетические, но реалистичные:

* терапия — 1 240;
* хирургия — 980;
* кардиология — 860;
* урология — 540;
* офтальмология — 420.

Файл: data/15_dataset.csv
Запуск: uv run python 05_charts/15_bar/scripts/make_data.py
"""

from __future__ import annotations

import pandas as pd

from goodgraph.paths import DATA_DIR

ROWS = [
    ("Терапия", 1240),
    ("Хирургия", 980),
    ("Кардиология", 860),
    ("Урология", 540),
    ("Офтальмология", 420),
]


def main() -> None:
    df = pd.DataFrame(ROWS, columns=["department", "admissions"])
    out = DATA_DIR / "15_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")

    print(f"Данные записаны: {out}")
    print(f"Строк: {len(df)}; всего госпитализаций: {df['admissions'].sum()}")
    print(df.sort_values("admissions", ascending=False).to_string(index=False))


if __name__ == "__main__":
    main()
