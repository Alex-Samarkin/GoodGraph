#!/usr/bin/env python3
"""Данные для раздела 5.07: контурная плотность возраста и САД.

Сценарий
--------
10 000 взрослых, возраст (лет) и систолическое АД (мм рт. ст.). САД растёт
с возрастом, но разброс большой. Контурная карта плотности показывает,
где наблюдений много, а где мало.

Данные синтетические, но реалистичные:

* возраст — около 52 лет (SD ≈ 15), диапазон 18–85;
* САД — около 125 мм рт. ст., диапазон 90–200;
* связь положительная, r ≈ 0,5;
* гетероскедастичность: с возрастом разброс САД растёт.

Файл: data/07_dataset.csv
Запуск: uv run python 05_charts/07_contour/scripts/make_data.py
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR

SEED = 20240525
N = 10_000


def make_dataset(seed: int = SEED) -> pd.DataFrame:
    """Сгенерировать таблицу «пациент — возраст — САД»."""
    rng = np.random.default_rng(seed)

    age = np.clip(rng.normal(52.0, 15.0, N), 18.0, 85.0)
    sbp = 95.0 + 0.58 * age + rng.normal(0.0, 10.0 + 0.10 * age, N)
    sbp = np.clip(sbp, 90.0, 200.0)

    return pd.DataFrame(
        {
            "patient_id": [f"C{i:05d}" for i in range(1, N + 1)],
            "age_years": np.round(age, 0).astype(int),
            "sbp_mm_hg": np.round(sbp, 0).astype(int),
        }
    )


def main() -> None:
    df = make_dataset()
    out = DATA_DIR / "07_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")

    r = df["age_years"].corr(df["sbp_mm_hg"])
    print(f"Данные записаны: {out}")
    print(f"Строк: {len(df)}")
    print(f"Возраст: {df['age_years'].mean():.1f} ± {df['age_years'].std(ddof=1):.1f} лет")
    print(f"САД: {df['sbp_mm_hg'].mean():.1f} ± {df['sbp_mm_hg'].std(ddof=1):.1f} мм рт. ст.")
    print(f"Корреляция: r = {r:.2f}")


if __name__ == "__main__":
    main()
