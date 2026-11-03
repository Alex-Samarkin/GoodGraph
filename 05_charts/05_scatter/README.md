# 5.05 Scatter

Пятый практический график: связь BMI и глюкозы. Свой генератор и свой
датасет.

## Файлы

| Файл | Назначение |
|---|---|
| [`scatter.md`](scatter.md) | текст раздела в Markdown |
| [`scatter.typ`](scatter.typ) | Typst-дубликат |
| [`scripts/make_data.py`](scripts/make_data.py) | генерация → `data/05_dataset.csv` |
| [`scripts/bad_plot.py`](scripts/bad_plot.py) | плохой график → `images/05_05_bad_scatter.*` |
| [`scripts/good_plot.py`](scripts/good_plot.py) | правильный график → `images/05_05_good_scatter.*` |

## Данные

`data/05_dataset.csv` — 180 пациентов, BMI и глюкоза натощак.

| Колонка | Смысл | Единица |
|---|---|---|
| `patient_id` | идентификатор пациента | — |
| `bmi_kg_m2` | индекс массы тела | кг/м² |
| `glucose_mmol_l` | глюкоза натощак | ммоль/л |

## Рисунки

| Рисунок | Файлы | Что показывает |
|---|---|---|
| 5.5.1 | `images/05_05_bad_scatter.svg`, `.png` | обрезанные оси, цвет по BMI, крупные точки |
| 5.5.2 | `images/05_05_good_scatter.svg`, `.png` | полный диапазон, alpha, линия регрессии, r и n |

## Запуск

```bash
uv sync
uv run python 05_charts/05_scatter/scripts/make_data.py
uv run python 05_charts/05_scatter/scripts/bad_plot.py
uv run python 05_charts/05_scatter/scripts/good_plot.py
```

## Что важно

- точки важнее линии;
- оси не обрезают данные;
- alpha/размер против overplotting;
- линия регрессии — только в диапазоне данных;
- указывайте r, n и единицы;
- корреляция ≠ причинность.

## Дальше

Следующий раздел — `06_hexbin`, плотность тысяч точек.
