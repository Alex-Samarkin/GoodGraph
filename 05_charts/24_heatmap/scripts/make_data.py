#!/usr/bin/env python3
"""Данные для 5.24: время ожидания по отделениям и часам."""

from __future__ import annotations

import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR

SEED = 20240605
DEPTS = ["Терапия", "Хирургия", "Кардиология", "ОРИТ", "Пульмонология"]
HOURS = [8, 10, 12, 14, 16, 18]
BASE = {"Терапия": 25, "Хирургия": 35, "Кардиология": 30, "ОРИТ": 15, "Пульмонология": 22}


def main() -> None:
    rng = np.random.default_rng(SEED)
    rows = []
    for dept in DEPTS:
        for hour in HOURS:
            peak = 18 if hour in (10, 12) else (10 if hour in (14, 16) else 0)
            value = BASE[dept] + peak + rng.normal(0, 5)
            rows.append({"department": dept, "hour": hour, "wait_min": int(np.clip(value, 5, 90))})
    df = pd.DataFrame(rows)
    out = DATA_DIR / "24_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")
    print(f"Данные записаны: {out}")
    print(df.pivot(index="department", columns="hour", values="wait_min").to_string())


if __name__ == "__main__":
    main()
