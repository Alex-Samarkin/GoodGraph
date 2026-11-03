#!/usr/bin/env python3
"""Данные для 5.25: экспрессия генов у 12 пациентов."""

from __future__ import annotations

import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR

SEED = 20240606
GENES = [f"G{i:02d}" for i in range(1, 11)]
SAMPLES = [f"S{i:02d}" for i in range(1, 13)]


def main() -> None:
    rng = np.random.default_rng(SEED)
    rows = []
    for gene in GENES:
        cluster = 1 if int(gene[1:]) <= 5 else 2
        values = []
        for sample in SAMPLES:
            sample_n = int(sample[1:])
            is_cluster = (cluster == 1 and sample_n <= 6) or (cluster == 2 and sample_n > 6)
            base = 8.0 if cluster == 1 else 4.0
            values.append(round(float(base + (3.5 if is_cluster else 0) + rng.normal(0, 0.6)), 2))
        rows.append({"gene": gene, **dict(zip(SAMPLES, values, strict=True))})
    df = pd.DataFrame(rows)
    out = DATA_DIR / "25_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")
    print(f"Данные записаны: {out}")
    print(f"Матрица: {df.shape[0]} генов × {df.shape[1]-1} пациентов")


if __name__ == "__main__":
    main()
