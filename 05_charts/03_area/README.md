# 5.03 Area chart

Третий практический график: концентрация препарата и площадь под кривой
(AUC). Свой генератор и свой датасет.

## Файлы

| Файл | Назначение |
|---|---|
| [`area.md`](area.md) | текст раздела в Markdown |
| [`area.typ`](area.typ) | Typst-дубликат |
| [`scripts/make_data.py`](scripts/make_data.py) | генерация → `data/03_dataset.csv` |
| [`scripts/bad_plot.py`](scripts/bad_plot.py) | плохой график → `images/05_03_bad_area.*` |
| [`scripts/good_plot.py`](scripts/good_plot.py) | правильный график → `images/05_03_good_area.*` |

## Данные

`data/03_dataset.csv` — 40 пациентов, 8 моментов (0–24 ч), 320 строк.

| Колонка | Смысл | Единица |
|---|---|---|
| `patient_id` | идентификатор пациента | — |
| `time_h` | время после приёма | часы |
| `conc_mg_l` | концентрация в плазме | мг/л |

Средний AUC0–24 — 80,7 ± 18,2 мг·ч/л.

## Рисунки

| Рисунок | Файлы | Что показывает |
|---|---|---|
| 5.3.1 | `images/05_03_bad_area.svg`, `.png` | заливка от 4, обрезанная ось, красная заливка и зелёная линия |
| 5.3.2 | `images/05_03_good_area.svg`, `.png` | заливка от 0, подпись AUC, среднее ± SD |

## Запуск

```bash
uv sync
uv run python 05_charts/03_area/scripts/make_data.py
uv run python 05_charts/03_area/scripts/bad_plot.py
uv run python 05_charts/03_area/scripts/good_plot.py
```

## На что смотреть

- area chart оправдан, когда площадь — смысл (AUC, накопление);
- заливка обязательно от нуля;
- площадь нужно подписать числом;
- если площадь не нужна — используйте линию;
- 85 мм, единицы, среднее ± SD.

## Дальше

Следующий раздел — `04_small_multiples`, малые кратные.