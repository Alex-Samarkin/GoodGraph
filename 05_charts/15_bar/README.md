# 5.15 Bar

Пятнадцатый раздел: столбцы для агрегированных величин. Свой генератор
и свой датасет.

## Файлы

| Файл | Назначение |
|---|---|
| [`bar.md`](bar.md) | текст раздела в Markdown |
| [`bar.typ`](bar.typ) | Typst-дубликат |
| [`scripts/make_data.py`](scripts/make_data.py) | генерация → `data/15_dataset.csv` |
| [`scripts/bad_plot.py`](scripts/bad_plot.py) | плохой график → `images/05_15_bad_bar.*` |
| [`scripts/good_plot.py`](scripts/good_plot.py) | правильный график → `images/05_15_good_bar.*` |

## Данные

`data/15_dataset.csv` — 5 отделений, госпитализации за год.

| Колонка | Смысл | Единица |
|---|---|---|
| `department` | отделение | — |
| `admissions` | госпитализаций за год | число |

## Рисунки

| Рисунок | Файлы | Что показывает |
|---|---|---|
| 5.15.1 | `images/05_15_bad_bar.svg`, `.png` | обрезанная ось 800–1300, радуга, тени |
| 5.15.2 | `images/05_15_good_bar.svg`, `.png` | горизонтальные сортированные столбцы, значения |

## Запуск

```bash
uv sync
uv run python 05_charts/15_bar/scripts/make_data.py
uv run python 05_charts/15_bar/scripts/bad_plot.py
uv run python 05_charts/15_bar/scripts/good_plot.py
```

## Что важно

- нулевая база обязательна;
- горизонтально для длинных подписей;
- сортировка и подписи значений;
- один цвет;
- bar — не для распределений и трендов.

## Дальше

Следующий раздел — `16_forest`, forest plot.
