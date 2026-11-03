#!/usr/bin/env python3
"""Данные для раздела 5.19: согласие лаборатории и глюкометра.

Сценарий
--------
150 пациентов, глюкоза измерена лабораторным анализатором и глюкометром.
Bland–Altman показывает среднюю разницу (bias) и пределы согласия (LoA).

Данные синтетические, но реалистичные:

* лабораторная глюкоза — около 6,5 ммоль/л;
* глюкометр занижает в среднем на 0,35 ммоль/л;
* разброс разницы — около 0,7 ммоль/л;
* LoA — примерно от −1,0 до +1,7 ммоль/л.

Файл: data/19_dataset.csv
Запуск: uv run python 05_charts/19_bland_altman/scripts/make_data.py
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR

SEED = 20240604
N = 150


def make_dataset(seed: int = SEED) -> pd.DataFrame:
    """Сгенерировать парные измерения двумя методами."""
    rng = np.random.default_rng(seed)
    lab = np.clip(rng.normal(6.5, 1.6, N), 3.5, 12.0)
    meter = lab - 0.35 + rng.normal(0.0, 0.7, N)
    meter = np.clip(meter, 3.0, 12.5)

    return pd.DataFrame(
        {
            "patient_id": [f"G{i:03d}" for i in range(1, N + 1)],
            "lab_glucose": np.round(lab, 1),
            "meter_glucose": np.round(meter, 1),
        }
    )


def main() -> None:
    df = make_dataset()
    out = DATA_DIR / "19_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")

    diff = df["lab_glucose"] - df["meter_glucose"]
    bias = diff.mean()
    loa = 1.96 * diff.std(ddof=1)
    print(f"Данные записаны: {out}")
    print(f"Строк: {len(df)}")
    print(f"Bias: {bias:+.2f} ммоль/л")
    print(f"LoA: {bias - loa:+.2f} … {bias + loa:+.2f} ммоль/л")


if __name__ == "__main__":
    main()
