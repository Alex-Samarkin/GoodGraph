# 5.10 ECDF

Десятый практический график: длительность госпитализации, ECDF.
Свой генератор и свой датасет.

## Файлы

| Файл | Назначение |
|---|---|
| [`ecdf.md`](ecdf.md) | текст раздела в Markdown |
| [`ecdf.typ`](ecdf.typ) | Typst-дубликат |
| [`scripts/make_data.py`](scripts/make_data.py) | генерация → `data/10_dataset.csv` |
| [`scripts/bad_plot.py`](scripts/bad_plot.py) | плохой график → `images/05_10_bad_ecdf.*` |
| [`scripts/good_plot.py`](scripts/good_plot.py) | правильный график → `images/05_10_good_ecdf.*` |

## Данные

`data/10_dataset.csv` — 1 200 госпитализаций, плановые и экстренные.

| Колонка | Смысл | Единица |
|---|---|---|
| `patient_id` | идентификатор пациента | — |
| `admission_type` | плановое/экстренное | — |
| `los_days` | длительность госпитализации | дни |

## Рисунки

| Рисунок | Файлы | Что показывает |
|---|---|---|
| 5.10.1 | `images/05_10_bad_ecdf.svg`, `.png` | обрезанная ось, красно-зелёные ступени, легенда |
| 5.10.2 | `images/05_10_good_ecdf.svg`, `.png` | полный диапазон, медианы, прямые подписи, n |

## Запуск

```bash
uv sync
uv run python 05_charts/10_ecdf/scripts/make_data.py
uv run python 05_charts/10_ecdf/scripts/bad_plot.py
uv run python 05_charts/10_ecdf/scripts/good_plot.py
```

## На что смотреть

- ECDF не требует бинов;
- ось X не обрезает хвост;
- медианы/квартили отмечайте;
- прямые подписи лучше легенды;
- для цензурированных данных — Kaplan–Meier.

## Дальше

Следующий раздел — `11_box`, сравнение распределений по группам.