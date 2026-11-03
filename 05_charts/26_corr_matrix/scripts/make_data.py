#!/usr/bin/env python3
"""Данные для 5.26: корреляционная матрица биомаркеров."""

from __future__ import annotations

import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR

SEED = 20240607
N = 500
COLS = ["age", "bmi", "sbp", "glucose", "hba1c", "ldl", "crp", "egfr"]


def main() -> None:
    rng = np.random.default_rng(SEED)
    latent = rng.normal(size=(N, 3))
    data = {
        "age": 50 + 12 * latent[:, 0] + rng.normal(0, 5, N),
        "bmi": 27 + 4 * latent[:, 0] + rng.normal(0, 3, N),
        "sbp": 125 + 12 * latent[:, 0] + 6 * latent[:, 1] + rng.normal(0, 8, N),
        "glucose": 5.5 + 1.2 * latent[:, 1] + 0.4 * latent[:, 0] + rng.normal(0, 0.7, N),
        "hba1c": 6.0 + 0.8 * latent[:, 1] + 0.2 * latent[:, 0] + rng.normal(0, 0.5, N),
        "ldl": 3.2 + 0.7 * latent[:, 2] + rng.normal(0, 0.6, N),
        "crp": 3.0 + 1.5 * latent[:, 2] + rng.normal(0, 1.5, N),
        "egfr": 85 - 10 * latent[:, 0] - 4 * latent[:, 1] + rng.normal(0, 8, N),
    }
    df = pd.DataFrame(data).round(2)
    out = DATA_DIR / "26_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")
    print(f"Данные записаны: {out}; {df.shape}")
    print(df.corr().round(2).to_string())


if __name__ == "__main__":
    main()
