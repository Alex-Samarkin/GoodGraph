#!/usr/bin/env python3
"""Данные для раздела 5.03: area chart концентрации препарата.

Сценарий
--------
40 пациентов получают условный препарат внутрь в дозе 500 мг. Концентрацию
в плазме измеряют через 0, 1, 2, 4, 6, 8, 12 и 24 часа. Площадь под
кривой концентрация–время (AUC) — интегральная экспозиция препарата.

Данные синтетические, но реалистичные:

* пик концентрации — около 8–9 мг/л через 1–2 часа;
* к 24 часам концентрация снижается до 1–2 мг/л;
* AUC0–24 — около 80 мг·ч/л;
* между пациентами есть вариабельность всасывания и клиренса.

Формат — long: одна строка = пациент × время.
Файл: data/03_dataset.csv
Запуск: uv run python 05_charts/03_area/scripts/make_data.py
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR

SEED = 20240521
TIMES = [0, 1, 2, 4, 6, 8, 12, 24]
N_PATIENTS = 40
DOSE_MG = 500.0
BIOAVAILABILITY = 0.8


def make_dataset(seed: int = SEED) -> pd.DataFrame:
    """Сгенерировать концентрации по одной камере с всасыванием."""
    rng = np.random.default_rng(seed)
    rows = []

    for i in range(1, N_PATIENTS + 1):
        # Межпациентная вариабельность всасывания и объёма распределения.
        ka = 1.4 * np.exp(rng.normal(0.0, 0.25))
        ke = 0.14 * np.exp(rng.normal(0.0, 0.18))
        volume = 35.0 * np.exp(rng.normal(0.0, 0.18))

        for time in TIMES:
            if time == 0:
                conc = 0.0
            else:
                conc = (
                    BIOAVAILABILITY
                    * DOSE_MG
                    * ka
                    / (volume * (ka - ke))
                    * (np.exp(-ke * time) - np.exp(-ka * time))
                )
                conc *= np.exp(rng.normal(0.0, 0.12))  # остаточная ошибка
            rows.append(
                {
                    "patient_id": f"A{i:03d}",
                    "time_h": time,
                    "conc_mg_l": round(float(np.clip(conc, 0.0, 20.0)), 2),
                }
            )

    return pd.DataFrame(rows)


def main() -> None:
    df = make_dataset()
    out = DATA_DIR / "03_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")

    auc = (
        df.groupby("patient_id")
        .apply(
            lambda part: np.trapezoid(
                part.sort_values("time_h")["conc_mg_l"].to_numpy(),
                part.sort_values("time_h")["time_h"].to_numpy(),
            ),
            include_groups=False,
        )
        .rename("auc")
    )
    print(f"Данные записаны: {out}")
    print(f"Строк: {len(df)}, пациентов: {df['patient_id'].nunique()}")
    print(f"AUC0–24: {auc.mean():.1f} ± {auc.std(ddof=1):.1f} мг·ч/л")
    mean_curve = df.groupby("time_h")["conc_mg_l"].mean()
    print(f"Средний пик по времени: {mean_curve.max():.2f} мг/л")
    print("\nСредняя концентрация по времени:")
    print(df.groupby("time_h")["conc_mg_l"].mean().round(2).to_string())


if __name__ == "__main__":
    main()
