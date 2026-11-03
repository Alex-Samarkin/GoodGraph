#!/usr/bin/env python3
"""Данные для раздела 5.09: распределение витамина D.

Сценарий
--------
1 200 взрослых, уровень 25(OH)D (нг/мл). Распределение сдвинуто влево
и имеет правый хвост: у части пациентов уровень низкий, у немногих —
очень высокий.

Данные синтетические, но реалистичные:

* медиана — около 24 нг/мл;
* IQR — примерно 17–33 нг/мл;
* дефицит (< 20 нг/мл) — примерно у трети;
* правый хвост до 60–70 нг/мл.

Файл: data/09_dataset.csv
Запуск: uv run python 05_charts/09_histogram/scripts/make_data.py
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR

SEED = 20240527
N = 1200


def make_dataset(seed: int = SEED) -> pd.DataFrame:
    """Сгенерировать гамма-распределение витамина D."""
    rng = np.random.default_rng(seed)
    values = rng.gamma(shape=4.0, scale=6.5, size=N)
    values = np.clip(values, 3.0, 70.0)

    return pd.DataFrame(
        {
            "patient_id": [f"V{i:04d}" for i in range(1, N + 1)],
            "vitamin_d_ng_ml": np.round(values, 1),
        }
    )


def main() -> None:
    df = make_dataset()
    out = DATA_DIR / "09_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")

    values = df["vitamin_d_ng_ml"]
    median = values.median()
    q1, q3 = values.quantile([0.25, 0.75])
    deficient = (values < 20).mean() * 100

    print(f"Данные записаны: {out}")
    print(f"Строк: {len(df)}")
    print(f"Медиана: {median:.1f} нг/мл; IQR: {q1:.1f}–{q3:.1f}")
    print(f"Дефицит (<20 нг/мл): {deficient:.1f} %")
    print(f"Минимум/максимум: {values.min():.1f} / {values.max():.1f}")


if __name__ == "__main__":
    main()
