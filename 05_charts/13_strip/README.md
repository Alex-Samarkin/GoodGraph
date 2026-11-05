# 5.13 Strip

Тринадцатый раздел: все точки по группам, jitter. Свой генератор
и свой датасет.

## Файлы

| Файл | Назначение |
|---|---|
| [`strip.md`](strip.md) | текст раздела в Markdown |
| [`strip.typ`](strip.typ) | Typst-дубликат |
| [`scripts/make_data.py`](scripts/make_data.py) | генерация → `data/13_dataset.csv` |
| [`scripts/bad_plot.py`](scripts/bad_plot.py) | плохой график → `images/05_13_bad_strip.*` |
| [`scripts/good_plot.py`](scripts/good_plot.py) | правильный график → `images/05_13_good_strip.*` |

## Данные

`data/13_dataset.csv` — 90 пациентов, три схемы обезболивания, ВАШ.

| Колонка | Смысл | Единица |
|---|---|---|
| `patient_id` | идентификатор пациента | — |
| `analgesia` | НПВС/опиоид/комбинация | — |
| `vas_mm` | боль по ВАШ | мм |

## Рисунки

| Рисунок | Файлы | Что показывает |
|---|---|---|
| 5.13.1 | `images/05_13_bad_strip.svg`, `.png` | нет jitter, радуга, обрезанная ось |
| 5.13.2 | `images/05_13_good_strip.svg`, `.png` | jitter, один цвет, медианы, n = 30 |

## Запуск

```bash
uv sync
uv run python 05_charts/13_strip/scripts/make_data.py
uv run python 05_charts/13_strip/scripts/bad_plot.py
uv run python 05_charts/13_strip/scripts/good_plot.py
```

## На что смотреть

- strip — для небольших выборок;
- jitter воспроизводимый и умеренный;
- показывайте медиану;
- не обрезайте хвосты;
- при тысячах точек — box/hexbin.

## Дальше

Следующий раздел — `14_dot_ci`, точка и доверительный интервал.