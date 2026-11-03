# 5.20 Stacked bar

Двадцатый раздел: состав исходов по отделениям. Свой генератор
и свой датасет.

## Файлы

| Файл | Назначение |
|---|---|
| [`stacked_bar.md`](stacked_bar.md) | текст раздела в Markdown |
| [`stacked_bar.typ`](stacked_bar.typ) | Typst-дубликат |
| [`scripts/make_data.py`](scripts/make_data.py) | генерация → `data/20_dataset.csv` |
| [`scripts/bad_plot.py`](scripts/bad_plot.py) | плохой график → `images/05_20_bad_stacked_bar.*` |
| [`scripts/good_plot.py`](scripts/good_plot.py) | правильный график → `images/05_20_good_stacked_bar.*` |

## Данные

`data/20_dataset.csv` — 4 отделения × 3 исхода.

| Колонка | Смысл | Единица |
|---|---|---|
| `department` | отделение | — |
| `outcome` | исход | — |
| `patients` | пациентов | человек |

## Рисунки

| Рисунок | Файлы | Что показывает |
|---|---|---|
| 5.20.1 | `images/05_20_bad_stacked_bar.svg`, `.png` | обрезанная ось, радуга, тени |
| 5.20.2 | `images/05_20_good_stacked_bar.svg`, `.png` | горизонтально, сортировка, значения и итоги |

## Запуск

```bash
uv sync
uv run python 05_charts/20_stacked_bar/scripts/make_data.py
uv run python 05_charts/20_stacked_bar/scripts/bad_plot.py
uv run python 05_charts/20_stacked_bar/scripts/good_plot.py
```

## Что важно

- нулевая база;
- 2–4 сегмента;
- одинаковый порядок сегментов;
- значения и итоги;
- для долей — 100 % stacked/dot.

## Дальше

Следующий раздел — `21_bar_100`, нормированный состав.
