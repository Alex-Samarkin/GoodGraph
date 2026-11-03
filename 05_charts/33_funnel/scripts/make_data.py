#!/usr/bin/env python3
"""Данные для 5.33: funnel plot, 25 исследований."""

from __future__ import annotations

import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR

SEED = 20240614
N = 25


def main() -> None:
    rng = np.random.default_rng(SEED)
    se = rng.uniform(0.08, 0.75, N)
    log_or = -0.30 - 0.28 * (se - 0.08) + rng.normal(0, 0.10, N)
    df = pd.DataFrame({"study": [f"S{i:02d}" for i in range(1, N + 1)],
                       "log_or": np.round(log_or, 3), "se": np.round(se, 3)})
    out = DATA_DIR / "33_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")
    print(f"Данные записаны: {out}; {len(df)} исследований")


if __name__ == "__main__":
    main()
