# 5.04 Small multiples

Четвёртый практический график: шесть отделений, 12 месяцев, малые кратные.
Свой генератор и свой датасет.

## Файлы

| Файл | Назначение |
|---|---|
| [`small_multiples.md`](small_multiples.md) | текст раздела в Markdown |
| [`small_multiples.typ`](small_multiples.typ) | Typst-дубликат |
| [`scripts/make_data.py`](scripts/make_data.py) | генерация → `data/04_dataset.csv` |
| [`scripts/bad_plot.py`](scripts/bad_plot.py) | плохой график → `images/05_04_bad_small_multiples.*` |
| [`scripts/good_plot.py`](scripts/good_plot.py) | правильный график → `images/05_04_good_small_multiples.*` |

## Данные

`data/04_dataset.csv` — 6 отделений × 12 месяцев, 72 строки.

| Колонка | Смысл | Единица |
|---|---|---|
| `department` | отделение | — |
| `month` | месяц (1–12) | — |
| `ddd_per_100_bed_days` | потребление антибиотиков | DDD/100 койко-дней |

## Рисунки

| Рисунок | Файлы | Что показывает |
|---|---|---|
| 5.4.1 | `images/05_04_bad_small_multiples.svg`, `.png` | шесть линий на одной оси, радуга, обрезанная ось |
| 5.4.2 | `images/05_04_good_small_multiples.svg`, `.png` | 2×3 панели, общая ось 0–150, один цвет |

## Запуск

```bash
uv sync
uv run python 05_charts/04_small_multiples/scripts/make_data.py
uv run python 05_charts/04_small_multiples/scripts/bad_plot.py
uv run python 05_charts/04_small_multiples/scripts/good_plot.py
```

## На что смотреть

- одна панель — одна серия;
- общая шкала X и Y — контракт сравнения;
- один цвет, подписи панелей вместо легенды;
- подписи осей только по краям сетки;
- 170 мм, панели не сжаты;
- если серий 2–3, обычная линия лучше.

## Дальше

Следующий раздел — `05_scatter`, связь двух непрерывных величин.