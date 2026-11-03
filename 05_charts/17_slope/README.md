# 5.17 Slope

Семнадцатый раздел: изменение веса до/после по клиникам. Свой
генератор и свой датасет.

## Файлы

| Файл | Назначение |
|---|---|
| [`slope.md`](slope.md) | текст раздела в Markdown |
| [`slope.typ`](slope.typ) | Typst-дубликат |
| [`scripts/make_data.py`](scripts/make_data.py) | генерация → `data/17_dataset.csv` |
| [`scripts/bad_plot.py`](scripts/bad_plot.py) | плохой график → `images/05_17_bad_slope.*` |
| [`scripts/good_plot.py`](scripts/good_plot.py) | правильный график → `images/05_17_good_slope.*` |

## Данные

`data/17_dataset.csv` — 360 пациентов, 6 клиник, вес до/после.

| Колонка | Смысл | Единица |
|---|---|---|
| `patient_id` | идентификатор пациента | — |
| `clinic` | клиника | — |
| `weight_before_kg` | вес до | кг |
| `weight_after_kg` | вес после | кг |

## Рисунки

| Рисунок | Файлы | Что показывает |
|---|---|---|
| 5.17.1 | `images/05_17_bad_slope.svg`, `.png` | радуга, нет подписей, обрезанная ось |
| 5.17.2 | `images/05_17_good_slope.svg`, `.png` | серые линии, акцент, подписи до/после |

## Запуск

```bash
uv sync
uv run python 05_charts/17_slope/scripts/make_data.py
uv run python 05_charts/17_slope/scripts/bad_plot.py
uv run python 05_charts/17_slope/scripts/good_plot.py
```

## Что важно

- slope — для парных агрегатов, не для сотен траекторий;
- подписи групп и значений;
- акцент только на лидере/аутлайере;
- не обрезайте диапазон;
- не путайте изменение с причинностью.

## Дальше

Следующий раздел — `18_paired_dot`, индивидуальные парные изменения.
