#!/usr/bin/env python3
"""Данные для раздела 5.21: тяжесть по возрастным группам (100 %)."""

from __future__ import annotations

import pandas as pd

from goodgraph.paths import DATA_DIR

ROWS = [
    ("<40", "лёгкая", 120), ("<40", "средняя", 60), ("<40", "тяжёлая", 20),
    ("40–59", "лёгкая", 90), ("40–59", "средняя", 70), ("40–59", "тяжёлая", 40),
    ("60–74", "лёгкая", 60), ("60–74", "средняя", 70), ("60–74", "тяжёлая", 70),
    ("75+", "лёгкая", 30), ("75+", "средняя", 55), ("75+", "тяжёлая", 115),
]


def main() -> None:
    df = pd.DataFrame(ROWS, columns=["age_group", "severity", "patients"])
    out = DATA_DIR / "21_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")
    print(f"Данные записаны: {out}")
    print(df.pivot(index="age_group", columns="severity", values="patients").to_string())


if __name__ == "__main__":
    main()
