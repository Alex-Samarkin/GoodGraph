# 5.16 Forest

Шестнадцатый раздел: forest plot для OR по подгруппам. Свой генератор
и свой датасет.

## Файлы

| Файл | Назначение |
|---|---|
| [`forest.md`](forest.md) | текст раздела в Markdown |
| [`forest.typ`](forest.typ) | Typst-дубликат |
| [`scripts/make_data.py`](scripts/make_data.py) | генерация → `data/16_dataset.csv` |
| [`scripts/bad_plot.py`](scripts/bad_plot.py) | плохой график → `images/05_16_bad_forest.*` |
| [`scripts/good_plot.py`](scripts/good_plot.py) | правильный график → `images/05_16_good_forest.*` |

## Данные

`data/16_dataset.csv` — 800 пациентов, 8 подгрупп + общая оценка.

| Колонка | Смысл |
|---|---|
| `subgroup` | подгруппа |
| `n_treatment` | n в лечении |
| `events_treatment` | события в лечении |
| `n_control` | n в контроле |
| `events_control` | события в контроле |

## Рисунки

| Рисунок | Файлы | Что показывает |
|---|---|---|
| 5.16.1 | `images/05_16_bad_forest.svg`, `.png` | только точки OR, линейная ось, нет CI |
| 5.16.2 | `images/05_16_good_forest.svg`, `.png` | лог-ось, 95 % CI, ромб, таблица |

## Запуск

```bash
uv sync
uv run python 05_charts/16_forest/scripts/make_data.py
uv run python 05_charts/16_forest/scripts/bad_plot.py
uv run python 05_charts/16_forest/scripts/good_plot.py
```

## На что смотреть

- для OR/RR/HR — лог-ось;
- линия 1 обязательна;
- CI, а не только точки;
- размер по n, ромб общей оценки;
- не ранжировать подгруппы по p-value.

## Дальше

Следующий раздел — `17_slope`, slope plot.