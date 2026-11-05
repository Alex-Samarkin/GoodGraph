# 5.12 Violin

Двенадцатый раздел: violin с квартильными линиями и с внутренней
коробкой. Свой генератор и свой датасет.

## Файлы

| Файл | Назначение |
|---|---|
| [`violin.md`](violin.md) | текст раздела в Markdown |
| [`violin.typ`](violin.typ) | Typst-дубликат |
| [`scripts/make_data.py`](scripts/make_data.py) | генерация → `data/12_dataset.csv` |
| [`scripts/bad_plot.py`](scripts/bad_plot.py) | плохой график → `images/05_12_bad_violin.*` |
| [`scripts/good_violin_quart.py`](scripts/good_violin_quart.py) | violin + квартили → `images/05_12_good_violin_quart.*` |
| [`scripts/good_violin_box.py`](scripts/good_violin_box.py) | violin + коробка → `images/05_12_good_violin_box.*` |

## Данные

`data/12_dataset.csv` — 600 пациентов, три стадии ХБП.

| Колонка | Смысл | Единица |
|---|---|---|
| `patient_id` | идентификатор пациента | — |
| `ckd_stage` | стадия ХБП | — |
| `sex` | пол | — |
| `egfr_ml_min_1_73m2` | СКФ | мл/мин/1,73 м² |

## Рисунки

| Рисунок | Файлы | Что показывает |
|---|---|---|
| 5.12.1 | `images/05_12_bad_violin.svg`, `.png` | обрезанная ось, радуга, нет медиан |
| 5.12.2 | `images/05_12_good_violin_quart.svg`, `.png` | violin + квартильные линии + точки |
| 5.12.3 | `images/05_12_good_violin_box.svg`, `.png` | violin + внутренняя коробка (rectangles) |

## Запуск

```bash
uv sync
uv run python 05_charts/12_violin/scripts/make_data.py
uv run python 05_charts/12_violin/scripts/bad_plot.py
uv run python 05_charts/12_violin/scripts/good_violin_quart.py
uv run python 05_charts/12_violin/scripts/good_violin_box.py
```

## На что смотреть

- violin показывает форму, но не заменяет сводку;
- внутри — квартили или коробка;
- при малых n — точки важнее контура;
- не обрезайте хвосты;
- bandwidth/trim — параметры, а не истина.

## Дальше

Следующий раздел — `13_strip`, отдельные точки по группам.