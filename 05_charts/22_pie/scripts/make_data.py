#!/usr/bin/env python3
"""Данные для раздела 5.22: причины повторной госпитализации."""

from __future__ import annotations

import pandas as pd

from goodgraph.paths import DATA_DIR

ROWS = [
    ("Сердечная недостаточность", 160),
    ("Инфекции", 100),
    ("Кровотечения", 80),
    ("Прочее", 60),
]


def main() -> None:
    df = pd.DataFrame(ROWS, columns=["cause", "patients"])
    out = DATA_DIR / "22_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")
    print(f"Данные записаны: {out}")
    print(f"Всего: {df['patients'].sum()}")
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()
