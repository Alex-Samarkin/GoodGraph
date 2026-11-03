# 5.06 Hexbin

Шестой практический график: плотность 8 000 точек HbA1c–глюкоза.
Свой генератор и свой датасет.

## Файлы

| Файл | Назначение |
|---|---|
| [`hexbin.md`](hexbin.md) | текст раздела в Markdown |
| [`hexbin.typ`](hexbin.typ) | Typst-дубликат |
| [`scripts/make_data.py`](scripts/make_data.py) | генерация → `data/06_dataset.csv` |
| [`scripts/bad_plot.py`](scripts/bad_plot.py) | плохой график → `images/05_06_bad_hexbin.*` |
| [`scripts/good_plot.py`](scripts/good_plot.py) | правильный график → `images/05_06_good_hexbin.*` |

## Данные

`data/06_dataset.csv` — 8 000 пациентов, HbA1c и глюкоза натощак.

| Колонка | Смысл | Единица |
|---|---|---|
| `patient_id` | идентификатор пациента | — |
| `hba1c_pct` | гликированный гемоглобин | % |
| `glucose_mmol_l` | глюкоза натощак | ммоль/л |

## Рисунки

| Рисунок | Файлы | Что показывает |
|---|---|---|
| 5.6.1 | `images/05_06_bad_hexbin.svg`, `.png` | 8 000 точек scatter, overplotting, обрезанные оси |
| 5.6.2 | `images/05_06_good_hexbin.svg`, `.png` | hexbin, лог. плотность, colorbar 1–100 |

## Запуск

```bash
uv sync
uv run python 05_charts/06_hexbin/scripts/make_data.py
uv run python 05_charts/06_hexbin/scripts/bad_plot.py
uv run python 05_charts/06_hexbin/scripts/good_plot.py
```

## Что важно

- hexbin — для больших n, не для отдельных наблюдений;
- цвет = число пациентов в бине, а не значение;
- `mincnt=1`, логарифмическая шкала плотности;
- подписанный colorbar;
- полный диапазон осей и n.

## Дальше

Следующий раздел — `07_contour`, изолинии плотности.
