# 5.09 Гистограмма

Девятый практический график: распределение витамина D. Свой генератор
и свой датасет.

## Файлы

| Файл | Назначение |
|---|---|
| [`histogram.md`](histogram.md) | текст раздела в Markdown |
| [`histogram.typ`](histogram.typ) | Typst-дубликат |
| [`scripts/make_data.py`](scripts/make_data.py) | генерация → `data/09_dataset.csv` |
| [`scripts/bad_plot.py`](scripts/bad_plot.py) | плохой график → `images/05_09_bad_histogram.*` |
| [`scripts/good_plot.py`](scripts/good_plot.py) | правильный график → `images/05_09_good_histogram.*` |

## Данные

`data/09_dataset.csv` — 1 200 взрослых, 25(OH)D.

| Колонка | Смысл | Единица |
|---|---|---|
| `patient_id` | идентификатор пациента | — |
| `vitamin_d_ng_ml` | 25(OH)D | нг/мл |

## Рисунки

| Рисунок | Файлы | Что показывает |
|---|---|---|
| 5.9.1 | `images/05_09_bad_histogram.svg`, `.png` | 5 бинов, обрезанная ось, радуга, тени |
| 5.9.2 | `images/05_09_good_histogram.svg`, `.png` | бины по 2 нг/мл, порог 20, медиана, n |

## Запуск

```bash
uv sync
uv run python 05_charts/09_histogram/scripts/make_data.py
uv run python 05_charts/09_histogram/scripts/bad_plot.py
uv run python 05_charts/09_histogram/scripts/good_plot.py
```

## На что смотреть

- ширина бина — главный параметр;
- не обрезайте хвосты;
- указывайте единицы, n, медиану/IQR;
- клинический порог — на графике;
- проверяйте устойчивость к выбору бинов.

## Дальше

Следующий раздел — `10_ecdf`, эмпирическая функция распределения.