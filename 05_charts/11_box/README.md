# 5.11 Boxplot

Одиннадцатый раздел: boxplot, точки, violin и гистограмма вместе.
Свой генератор и свой датасет.

## Файлы

| Файл | Назначение |
|---|---|
| [`box.md`](box.md) | текст раздела в Markdown |
| [`box.typ`](box.typ) | Typst-дубликат |
| [`scripts/make_data.py`](scripts/make_data.py) | генерация → `data/11_dataset.csv` |
| [`scripts/bad_plot.py`](scripts/bad_plot.py) | плохой boxplot → `images/05_11_bad_box.*` |
| [`scripts/good_box_points.py`](scripts/good_box_points.py) | box + точки → `images/05_11_good_box_points.*` |
| [`scripts/good_violin_box.py`](scripts/good_violin_box.py) | violin + box + точки → `images/05_11_good_violin_box.*` |
| [`scripts/good_box_hist.py`](scripts/good_box_hist.py) | histogram + box → `images/05_11_good_box_hist.*` |

## Данные

`data/11_dataset.csv` — 450 взрослых, три группы активности.

| Колонка | Смысл | Единица |
|---|---|---|
| `patient_id` | идентификатор пациента | — |
| `activity` | низкая/умеренная/высокая | — |
| `bmi_kg_m2` | индекс массы тела | кг/м² |

## Рисунки

| Рисунок | Файлы | Что показывает |
|---|---|---|
| 5.11.1 | `images/05_11_bad_box.svg`, `.png` | обрезанная ось, радуга, нет точек |
| 5.11.2 | `images/05_11_good_box_points.svg`, `.png` | boxplot + jitter-точки |
| 5.11.3 | `images/05_11_good_violin_box.svg`, `.png` | violin + box + точки |
| 5.11.4 | `images/05_11_good_box_hist.svg`, `.png` | гистограмма + горизонтальный boxplot |

## Запуск

```bash
uv sync
uv run python 05_charts/11_box/scripts/make_data.py
uv run python 05_charts/11_box/scripts/bad_plot.py
uv run python 05_charts/11_box/scripts/good_box_points.py
uv run python 05_charts/11_box/scripts/good_violin_box.py
uv run python 05_charts/11_box/scripts/good_box_hist.py
```

## Что важно

- boxplot скрывает форму — добавляйте точки/ violin / histogram;
- не обрезайте усы и выбросы;
- указывайте n по группам;
- violin — это KDE, а не «истинная» плотность;
- 3 группы — удобный максимум для одного графика.

## Дальше

Следующий раздел — `12_violin`, отдельный разбор violin.
