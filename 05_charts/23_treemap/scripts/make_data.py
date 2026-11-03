#!/usr/bin/env python3
"""Данные для раздела 5.23: затраты по программам."""

from __future__ import annotations

import pandas as pd

from goodgraph.paths import DATA_DIR

ROWS = [
    ("Кардиология", 320),
    ("Онкология", 280),
    ("Терапия", 210),
    ("Хирургия", 180),
    ("Педиатрия", 120),
    ("Прочее", 90),
]


def main() -> None:
    df = pd.DataFrame(ROWS, columns=["program", "cost_mln_rub"])
    out = DATA_DIR / "23_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")
    print(f"Данные записаны: {out}")
    print(f"Всего: {df['cost_mln_rub'].sum()} млн руб.")
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()
