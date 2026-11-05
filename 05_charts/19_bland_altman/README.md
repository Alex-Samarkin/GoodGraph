# 5.19 Bland–Altman

Девятнадцатый раздел: согласие лаборатории и глюкометра. Свой
генератор и свой датасет.

## Файлы

| Файл | Назначение |
|---|---|
| [`bland_altman.md`](bland_altman.md) | текст раздела в Markdown |
| [`bland_altman.typ`](bland_altman.typ) | Typst-дубликат |
| [`scripts/make_data.py`](scripts/make_data.py) | генерация → `data/19_dataset.csv` |
| [`scripts/bad_plot.py`](scripts/bad_plot.py) | плохой график → `images/05_19_bad_bland_altman.*` |
| [`scripts/good_plot.py`](scripts/good_plot.py) | правильный график → `images/05_19_good_bland_altman.*` |

## Данные

`data/19_dataset.csv` — 150 пациентов, глюкоза двумя методами.

| Колонка | Смысл | Единица |
|---|---|---|
| `patient_id` | идентификатор пациента | — |
| `lab_glucose` | лаборатория | ммоль/л |
| `meter_glucose` | глюкометр | ммоль/л |

## Рисунки

| Рисунок | Файлы | Что показывает |
|---|---|---|
| 5.19.1 | `images/05_19_bad_bland_altman.svg`, `.png` | один метод по X, нет bias/LoA, обрезанная ось |
| 5.19.2 | `images/05_19_good_bland_altman.svg`, `.png` | среднее по X, bias +0,35, LoA |

## Запуск

```bash
uv sync
uv run python 05_charts/19_bland_altman/scripts/make_data.py
uv run python 05_charts/19_bland_altman/scripts/bad_plot.py
uv run python 05_charts/19_bland_altman/scripts/good_plot.py
```

## На что смотреть

- по X — среднее двух методов;
- bias и 95 % LoA;
- не обрезайте разницы;
- LoA сравнивайте с клинической допустимостью;
- BA — не корреляция.

## Дальше

Следующий раздел — `20_stacked_bar`, состав целого.