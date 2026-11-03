#!/usr/bin/env python3
"""Данные для раздела 5.05: связь BMI и глюкозы.

Сценарий
--------
180 взрослых пациентов на профилактическом осмотре. Измерены индекс массы
тела (BMI, кг/м²) и глюкоза натощак (ммоль/л). Связь положительная,
но не идеальная: есть разброс и выбросы.

Данные синтетические, но реалистичные:

* BMI — около 27,5 кг/м² (SD ≈ 4,2), диапазон 18–42;
* глюкоза — около 5,8 ммоль/л, диапазон 3,5–10;
* корреляция — умеренная, r ≈ 0,5–0,6;
* у части пациентов глюкоза выше, чем предсказывает BMI.

Файл: data/05_dataset.csv
Запуск: uv run python 05_charts/05_scatter/scripts/make_data.py
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR

SEED = 20240523
N = 180


def make_dataset(seed: int = SEED) -> pd.DataFrame:
    """Сгенерировать таблицу «пациент — BMI — глюкоза»."""
    rng = np.random.default_rng(seed)

    bmi = np.clip(rng.normal(27.5, 4.2, N), 18.0, 42.0)
    glucose = 2.2 + 0.13 * bmi + rng.normal(0.0, 0.9, N)
    glucose = np.clip(glucose, 3.2, 11.0)

    return pd.DataFrame(
        {
            "patient_id": [f"S{i:03d}" for i in range(1, N + 1)],
            "bmi_kg_m2": np.round(bmi, 1),
            "glucose_mmol_l": np.round(glucose, 1),
        }
    ).sample(frac=1, random_state=seed).reset_index(drop=True)


def main() -> None:
    df = make_dataset()
    out = DATA_DIR / "05_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")

    r = df["bmi_kg_m2"].corr(df["glucose_mmol_l"])
    print(f"Данные записаны: {out}")
    print(f"Строк: {len(df)}, пациентов: {df['patient_id'].nunique()}")
    print(f"BMI: {df['bmi_kg_m2'].mean():.1f} ± {df['bmi_kg_m2'].std(ddof=1):.1f} кг/м²")
    print(
        f"Глюкоза: {df['glucose_mmol_l'].mean():.1f} ± "
        f"{df['glucose_mmol_l'].std(ddof=1):.1f} ммоль/л"
    )
    print(f"Корреляция Пирсона: r = {r:.2f}")


if __name__ == "__main__":
    main()
