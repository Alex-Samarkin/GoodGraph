# Раздел 1. Принципы качественной научной графики

Первый раздел методички: смысловые принципы, нормативы оформления и разбор
одного и того же результата в «плохой» и «правильной» версиях.

## Файлы

| Файл | Назначение |
|---|---|
| [`principles.md`](principles.md) | основной текст раздела в Markdown |
| [`principles.typ`](principles.typ) | тот же текст для сборки PDF через Typst |
| [`scripts/make_data.py`](scripts/make_data.py) | генерация данных → `data/00_dataset.csv` |
| [`scripts/bad_plot.py`](scripts/bad_plot.py) | неудачный график → `images/01_bad_bar_truncated.*` |
| [`scripts/good_plot.py`](scripts/good_plot.py) | правильный график → `images/01_good_dot_ci.*` |

## Данные

`data/00_dataset.csv` — 148 синтетических пациентов, три группы, 12 недель
терапии. Колонки:

| Колонка | Смысл | Единица |
|---|---|---|
| `patient_id` | идентификатор пациента | — |
| `group` | группа терапии | — |
| `baseline_sbp_mm_hg` | САД до лечения | мм рт. ст. |
| `followup_sbp_mm_hg` | САД через 12 недель | мм рт. ст. |
| `change_sbp_mm_hg` | изменение САД (baseline − followup) | мм рт. ст. |

Данные не описывают реальных пациентов и созданы только для иллюстрации
приёмов визуализации.

## Запуск

```bash
# из корня репозитория
uv sync

uv run python 01_principles/scripts/make_data.py
uv run python 01_principles/scripts/bad_plot.py
uv run python 01_principles/scripts/good_plot.py
```

Или одной командой:

```bash
make figures
```

## Рисунки

| Рисунок | Файлы | Что показывает |
|---|---|---|
| 1.1 | `images/01_bad_bar_truncated.svg`, `.png` | обрезанная ось, светофорная палитра, тени, тяжёлая сетка |
| 1.2 | `images/01_good_dot_ci.svg`, `.png` | точки + среднее + 95 % ДИ, нулевая линия, Okabe–Ito |

Оба рисунка сохраняются в SVG (вектор) и PNG (растр 600 dpi для «хорошего»
и 300 dpi для «плохого» — намеренно разных, чтобы показать разницу подходов).

## Сборка PDF

```bash
typst compile --root . typst/main.typ build/metodichka.pdf
```

Флаг `--root .` обязателен: иначе Typst не пустит файл из `01_principles/`
к картинкам в `../images/`.

## Связь с другими разделами

- Подробная теория цвета и шрифтов — раздел 3.
- Обзор видов графиков — раздел 4.
- Полные примеры «данные → плохо → хорошо» — раздел 5.
- Требования журналов и чек-лист отправки — раздел 7.
