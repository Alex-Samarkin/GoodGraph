# 5.18 Paired dot

Восемнадцатый раздел: индивидуальные парные изменения гемоглобина.
Свой генератор и свой датасет.

## Файлы

| Файл | Назначение |
|---|---|
| [`paired_dot.md`](paired_dot.md) | текст раздела в Markdown |
| [`paired_dot.typ`](paired_dot.typ) | Typst-дубликат |
| [`scripts/make_data.py`](scripts/make_data.py) | генерация → `data/18_dataset.csv` |
| [`scripts/bad_plot.py`](scripts/bad_plot.py) | плохой график → `images/05_18_bad_paired_dot.*` |
| [`scripts/good_plot.py`](scripts/good_plot.py) | правильный график → `images/05_18_good_paired_dot.*` |

## Данные

`data/18_dataset.csv` — 30 пациентов, гемоглобин до/после.

| Колонка | Смысл | Единица |
|---|---|---|
| `patient_id` | идентификатор пациента | — |
| `hemoglobin_before` | гемоглобин до | г/л |
| `hemoglobin_after` | гемоглобин после | г/л |

## Рисунки

| Рисунок | Файлы | Что показывает |
|---|---|---|
| 5.18.1 | `images/05_18_bad_paired_dot.svg`, `.png` | радужные линии, нет точек/средних, обрезанная ось |
| 5.18.2 | `images/05_18_good_paired_dot.svg`, `.png` | серые линии, точки, среднее +12,4 г/л |

## Запуск

```bash
uv sync
uv run python 05_charts/18_paired_dot/scripts/make_data.py
uv run python 05_charts/18_paired_dot/scripts/bad_plot.py
uv run python 05_charts/18_paired_dot/scripts/good_plot.py
```

## Что важно

- paired dot — для 10–50 пар;
- видны линии и точки;
- среднее изменение подписано;
- не обрезайте диапазон;
- для вывода нужен парный тест.

## Дальше

Следующий раздел — `19_bland_altman`, согласие методов.
