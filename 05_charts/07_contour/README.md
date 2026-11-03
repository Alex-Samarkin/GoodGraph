# 5.07 Contour

Седьмой практический график: контурная плотность возраста и САД.
Свой генератор и свой датасет.

## Файлы

| Файл | Назначение |
|---|---|
| [`contour.md`](contour.md) | текст раздела в Markdown |
| [`contour.typ`](contour.typ) | Typst-дубликат |
| [`scripts/make_data.py`](scripts/make_data.py) | генерация → `data/07_dataset.csv` |
| [`scripts/bad_plot.py`](scripts/bad_plot.py) | плохой график → `images/05_07_bad_contour.*` |
| [`scripts/good_plot.py`](scripts/good_plot.py) | правильный график → `images/05_07_good_contour.*` |

## Данные

`data/07_dataset.csv` — 10 000 взрослых, возраст и САД.

| Колонка | Смысл | Единица |
|---|---|---|
| `patient_id` | идентификатор пациента | — |
| `age_years` | возраст | лет |
| `sbp_mm_hg` | систолическое АД | мм рт. ст. |

## Рисунки

| Рисунок | Файлы | Что показывает |
|---|---|---|
| 5.7.1 | `images/05_07_bad_contour.svg`, `.png` | jet, 20 уровней, налезающие подписи, обрезанные оси |
| 5.7.2 | `images/05_07_good_contour.svg`, `.png` | сглаженная плотность, cividis, colorbar, порог 140 |

## Запуск

```bash
uv sync
uv run python 05_charts/07_contour/scripts/make_data.py
uv run python 05_charts/07_contour/scripts/bad_plot.py
uv run python 05_charts/07_contour/scripts/good_plot.py
```

## Что важно

- contour — оценка плотности, а не «истина»;
- сглаживание и число уровней — параметры;
- cividis, colorbar, единицы, n;
- порог 140 мм рт. ст. — клинический контекст;
- для локальной структуры — hexbin.

## Дальше

Следующий раздел — `08_loess`, нелинейный тренд.
