#!/usr/bin/env python3
"""Данные для 5.32: осложнения по 30 центрам."""

from __future__ import annotations

import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR

SEED = 20240613
N_CENTERS = 30
N_PATIENTS = 80


def main() -> None:
    rng = np.random.default_rng(SEED)
    base = rng.normal(0.12, 0.05, N_CENTERS).clip(0.03, 0.28)
    events = rng.binomial(N_PATIENTS, base)
    df = pd.DataFrame({"center": [f"Ц{i:02d}" for i in range(1, N_CENTERS + 1)],
                       "n": N_PATIENTS, "events": events})
    out = DATA_DIR / "32_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")
    print(f"Данные записаны: {out}; {len(df)} центров")


if __name__ == "__main__":
    main()
