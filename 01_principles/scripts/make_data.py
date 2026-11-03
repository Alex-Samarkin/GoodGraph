#!/usr/bin/env python3
"""Данные для раздела 1 «Принципы качественной научной графики».

Сценарий
--------
Гипотетическое рандомизированное исследование: 148 пациентов с
артериальной гипертензией, три группы, 12 недель терапии. Первичная
конечная точка — изменение систолического артериального давления (САД)
от исходного уровня, мм рт. ст.

Данные синтетические, но правдоподобные по единицам, разбросу и
клинически значимым величинам:

* исходное САД — около 152 мм рт. ст. (SD ≈ 11);
* среднее снижение — от 4,2 (плацебо) до 8,9 мм рт. ст. (препарат B);
* индивидуальный разброс — SD ≈ 6–7 мм рт. ст., поэтому у части
  пациентов САД может даже немного вырасти;
* n ≈ 50 в группе — типично для пилотного исследования.

Файл: data/00_dataset.csv
Запуск: uv run python 01_principles/scripts/make_data.py
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR

# Фиксируем зерно: любой читатель получит те же самые данные.
SEED = 20240517

# Параметры групп: среднее изменение, SD изменения, число пациентов.
GROUP_SPECS = [
    {"group": "Плацебо", "mean_change": 4.2, "sd_change": 6.0, "n": 48},
    {"group": "Препарат A 10 мг", "mean_change": 7.1, "sd_change": 6.5, "n": 51},
    {"group": "Препарат B 20 мг", "mean_change": 8.9, "sd_change": 6.8, "n": 49},
]

BASELINE_MEAN = 152.0
BASELINE_SD = 11.0


def make_dataset(seed: int = SEED) -> pd.DataFrame:
    """Сгенерировать таблицу «пациент — группа — САД до/после»."""
    rng = np.random.default_rng(seed)
    frames: list[pd.DataFrame] = []

    for spec in GROUP_SPECS:
        n = spec["n"]

        # Исходное САД: целые значения, физиологически правдоподобный диапазон.
        baseline = rng.normal(BASELINE_MEAN, BASELINE_SD, n)
        baseline = np.clip(np.rint(baseline), 125, 190).astype(int)

        # Изменение: центрируем выборку на заданном среднем, чтобы
        # иллюстративные средние совпадали с задуманными.
        change = rng.normal(spec["mean_change"], spec["sd_change"], n)
        change = change - change.mean() + spec["mean_change"]
        change = np.rint(change).astype(int)

        followup = np.clip(baseline - change, 85, 210).astype(int)
        # После клиппинга пересчитываем фактическое изменение.
        change = baseline - followup

        frames.append(
            pd.DataFrame(
                {
                    "group": spec["group"],
                    "baseline_sbp_mm_hg": baseline,
                    "followup_sbp_mm_hg": followup,
                    "change_sbp_mm_hg": change,
                }
            )
        )

    df = pd.concat(frames, ignore_index=True)
    # Уникальные идентификаторы на всё исследование, затем перемешиваем
    # строки: в реальной выгрузке порядок не сгруппирован по группам.
    df.insert(0, "patient_id", [f"P{i:03d}" for i in range(1, len(df) + 1)])
    return df.sample(frac=1, random_state=seed).reset_index(drop=True)


def main() -> None:
    df = make_dataset()
    out = DATA_DIR / "00_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")

    summary = (
        df.groupby("group", sort=False)["change_sbp_mm_hg"]
        .agg(["count", "mean", "std", "min", "max"])
        .round(1)
    )
    print(f"Данные записаны: {out}")
    print(f"Строк: {len(df)}, пациентов: {df['patient_id'].nunique()}")
    print("\nСводка по изменению САД, мм рт. ст.:")
    print(summary.to_string())


if __name__ == "__main__":
    main()
