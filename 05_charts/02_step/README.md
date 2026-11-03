# 5.02 Ступенчатый график

Второй практический график: доза варфарина на визитах, три пациента.
Свой генератор и свой датасет.

## Файлы

| Файл | Назначение |
|---|---|
| [`step.md`](step.md) | текст раздела в Markdown |
| [`step.typ`](step.typ) | Typst-дубликат |
| [`scripts/make_data.py`](scripts/make_data.py) | генерация → `data/02_dataset.csv` |
| [`scripts/bad_plot.py`](scripts/bad_plot.py) | плохой график → `images/05_02_bad_step.*` |
| [`scripts/good_plot.py`](scripts/good_plot.py) | правильный график → `images/05_02_good_step.*` |

## Данные

`data/02_dataset.csv` — 3 пациента, 13 визитов (0–12 недель), 39 строк.

| Колонка | Смысл | Единица |
|---|---|---|
| `patient_id` | идентификатор пациента | — |
| `week` | неделя визита | недели |
| `dose_mg` | доза варфарина | мг/сут |
| `inr` | международное нормализованное отношение | — |

## Рисунки

| Рисунок | Файлы | Что показывает |
|---|---|---|
| 5.2.1 | `images/05_02_bad_step.svg`, `.png` | наклонные линии вместо ступеней, обрезанная ось, тени |
| 5.2.2 | `images/05_02_good_step.svg`, `.png` | `steps-post`, маркеры визитов, прямые подписи |

## Запуск

```bash
uv sync
uv run python 05_charts/02_step/scripts/make_data.py
uv run python 05_charts/02_step/scripts/bad_plot.py
uv run python 05_charts/02_step/scripts/good_plot.py
```

## Что важно

- ступень — для величины, постоянной между событиями;
- `ax.step(..., where="post")`, а не `ax.plot`;
- маркеры в моменты визитов;
- ось Y 0–8 мг/сут, единицы;
- прямые подписи, без легенды;
- никаких двух осей Y для INR.

## Дальше

Следующий раздел — `03_area`, область под линией.
