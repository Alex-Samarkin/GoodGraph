#!/usr/bin/env python3
"""Данные для раздела 5.06: hexbin HbA1c и глюкозы.

Сценарий
--------
8 000 пациентов, HbA1c (%) и глюкоза натощак (ммоль/л). Связь сильная,
но с разбросом; при таком числе точек обычный scatter превращается
в сплошное пятно, поэтому нужен hexbin.

Данные синтетические, но реалистичные:

* HbA1c — около 6,3 % (SD ≈ 1,0), диапазон 4,8–12;
* глюкоза связана с HbA1c приблизительно линейно;
* остаточный разброс — около 1 ммоль/л;
* корреляция — сильная, r ≈ 0,8.

Файл: data/06_dataset.csv
Запуск: uv run python 05_charts/06_hexbin/scripts/make_data.py
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR

SEED = 20240524
N = 8000


def make_dataset(seed: int = SEED) -> pd.DataFrame:
    """Сгенерировать таблицу «пациент — HbA1c — глюкоза»."""
    rng = np.random.default_rng(seed)

    hba1c = np.clip(rng.normal(6.3, 1.0, N), 4.8, 12.0)
    glucose = 1.594 * hba1c - 2.59 + rng.normal(0.0, 1.0, N)
    glucose = np.clip(glucose, 3.0, 20.0)

    return pd.DataFrame(
        {
            "patient_id": [f"H{i:05d}" for i in range(1, N + 1)],
            "hba1c_pct": np.round(hba1c, 1),
            "glucose_mmol_l": np.round(glucose, 1),
        }
    )


def main() -> None:
    df = make_dataset()
    out = DATA_DIR / "06_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")

    r = df["hba1c_pct"].corr(df["glucose_mmol_l"])
    print(f"Данные записаны: {out}")
    print(f"Строк: {len(df)}")
    print(f"HbA1c: {df['hba1c_pct'].mean():.1f} ± {df['hba1c_pct'].std(ddof=1):.1f} %")
    print(
        f"Глюкоза: {df['glucose_mmol_l'].mean():.1f} ± "
        f"{df['glucose_mmol_l'].std(ddof=1):.1f} ммоль/л"
    )
    print(f"Корреляция Пирсона: r = {r:.2f}")


if __name__ == "__main__":
    main()
