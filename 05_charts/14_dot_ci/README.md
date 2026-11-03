# 5.14 Dot + CI

Четырнадцатый раздел: точка оценки и 95 % доверительный интервал.
Свой генератор и свой датасет.

## Файлы

| Файл | Назначение |
|---|---|
| [`dot_ci.md`](dot_ci.md) | текст раздела в Markdown |
| [`dot_ci.typ`](dot_ci.typ) | Typst-дубликат |
| [`scripts/make_data.py`](scripts/make_data.py) | генерация → `data/14_dataset.csv` |
| [`scripts/bad_plot.py`](scripts/bad_plot.py) | плохой график → `images/05_14_bad_dot_ci.*` |
| [`scripts/good_plot.py`](scripts/good_plot.py) | правильный график → `images/05_14_good_dot_ci.*` |

## Данные

`data/14_dataset.csv` — 600 пациентов, шесть центров, осложнение 1/0.

| Колонка | Смысл | Единица |
|---|---|---|
| `patient_id` | идентификатор пациента | — |
| `center` | центр | — |
| `complication` | осложнение (1/0) | — |

## Рисунки

| Рисунок | Файлы | Что показывает |
|---|---|---|
| 5.14.1 | `images/05_14_bad_dot_ci.svg`, `.png` | SD вместо CI, обрезанная ось, радуга |
| 5.14.2 | `images/05_14_good_dot_ci.svg`, `.png` | 95 % ДИ Уилсона, общая доля, n = 100 |

## Запуск

```bash
uv sync
uv run python 05_charts/14_dot_ci/scripts/make_data.py
uv run python 05_charts/14_dot_ci/scripts/bad_plot.py
uv run python 05_charts/14_dot_ci/scripts/good_plot.py
```

## Что важно

- CI ≠ SD;
- для долей — Уилсон;
- не обрезайте интервалы;
- указывайте n;
- пересечение CI — не повод ранжировать.

## Дальше

Следующий раздел — `15_bar`, столбцы и их ошибки.
