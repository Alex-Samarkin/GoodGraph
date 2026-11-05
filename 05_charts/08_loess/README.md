# 5.08 LOESS

Восьмой практический график: доза статина и снижение ЛПНП, нелинейный
тренд. Свой генератор и свой датасет.

## Файлы

| Файл | Назначение |
|---|---|
| [`loess.md`](loess.md) | текст раздела в Markdown |
| [`loess.typ`](loess.typ) | Typst-дубликат |
| [`scripts/make_data.py`](scripts/make_data.py) | генерация → `data/08_dataset.csv` |
| [`scripts/bad_plot.py`](scripts/bad_plot.py) | плохой график → `images/05_08_bad_loess.*` |
| [`scripts/good_plot.py`](scripts/good_plot.py) | правильный график → `images/05_08_good_loess.*` |

## Данные

`data/08_dataset.csv` — 300 пациентов, дозы 0/5/10/20/40/80 мг/сут.

| Колонка | Смысл | Единица |
|---|---|---|
| `patient_id` | идентификатор пациента | — |
| `dose_mg` | доза статина | мг/сут |
| `ldl_reduction_pct` | снижение ЛПНП | % |

## Рисунки

| Рисунок | Файлы | Что показывает |
|---|---|---|
| 5.8.1 | `images/05_08_bad_loess.svg`, `.png` | линейная прямая на данных с насыщением |
| 5.8.2 | `images/05_08_good_loess.svg`, `.png` | LOESS + bootstrap 95 % |

## Запуск

```bash
uv sync
uv run python 05_charts/08_loess/scripts/make_data.py
uv run python 05_charts/08_loess/scripts/bad_plot.py
uv run python 05_charts/08_loess/scripts/good_plot.py
```

## На что смотреть

- LOESS показывает тренд, а не причинность;
- указывайте `frac` и n;
- bootstrap-полоса показывает неопределённость кривой;
- не экстраполируйте за пределы данных;
- сравнивайте с параметрической моделью, если нужен вывод.

## Дальше

Следующий раздел — `09_histogram`, распределение одной величины.