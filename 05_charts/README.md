# Раздел 5. Графики: данные → плохо → хорошо

Практическая часть методички. **Каждый отдельный график** — своя папка,
свой генератор, свой датасет, свой разбор «плохо/хорошо».

Один «вид» на карте раздела 4 — это семейство. Внутри семейства несколько
графиков: например, «динамика» — это линия, step, area и small multiples;
«распределение» — гистограмма, ECDF, box, violin и strip. Все они получают
отдельные разделы.

## Полный индекс

| № | Семейство | График | Папка | Данные |
|---|---|---|---|---|
| 01 | Динамика | линейный график | `01_line/` | `data/01_dataset.csv` |
| 02 | Динамика | ступенчатый график (step) | `02_step/` | `data/02_dataset.csv` |
| 03 | Динамика | area chart | `03_area/` | `data/03_dataset.csv` |
| 04 | Динамика | малые кратные | `04_small_multiples/` | `data/04_dataset.csv` |
| 05 | Связь | диаграмма рассеяния | `05_scatter/` | `data/05_dataset.csv` |
| 06 | Связь | hexbin | `06_hexbin/` | `data/06_dataset.csv` |
| 07 | Связь | контурный график | `07_contour/` | `data/07_dataset.csv` |
| 08 | Связь | scatter + loess | `08_loess/` | `data/08_dataset.csv` |
| 09 | Распределение | гистограмма | `09_histogram/` | `data/09_dataset.csv` |
| 10 | Распределение | ECDF | `10_ecdf/` | `data/10_dataset.csv` |
| 11 | Распределение | box plot | `11_box/` | `data/11_dataset.csv` |
| 12 | Распределение | violin plot | `12_violin/` | `data/12_dataset.csv` |
| 13 | Распределение | strip / jitter | `13_strip/` | `data/13_dataset.csv` |
| 14 | Сравнение | точка + 95 % ДИ | `14_dot_ci/` | `data/14_dataset.csv` |
| 15 | Сравнение | столбцы/полосы | `15_bar/` | `data/15_dataset.csv` |
| 16 | Сравнение, эффекты | forest plot | `16_forest/` | `data/16_dataset.csv` |
| 17 | Сравнение, парные | slope chart | `17_slope/` | `data/17_dataset.csv` |
| 18 | Парные | paired dot plot | `18_paired_dot/` | `data/18_dataset.csv` |
| 19 | Парные | Bland–Altman | `19_bland_altman/` | `data/19_dataset.csv` |
| 20 | Состав | stacked bar | `20_stacked_bar/` | `data/20_dataset.csv` |
| 21 | Состав | 100 % stacked bar | `21_bar_100/` | `data/21_dataset.csv` |
| 22 | Состав | круговая диаграмма | `22_pie/` | `data/22_dataset.csv` |
| 23 | Состав | treemap | `23_treemap/` | `data/23_dataset.csv` |
| 24 | Матрица | heatmap | `24_heatmap/` | `data/24_dataset.csv` |
| 25 | Матрица | clustermap | `25_clustermap/` | `data/25_dataset.csv` |
| 26 | Матрица | correlation matrix | `26_corr_matrix/` | `data/26_dataset.csv` |
| 27 | Выживаемость | Kaplan–Meier | `27_kaplan_meier/` | `data/27_dataset.csv` |
| 28 | Выживаемость | cumulative incidence | `28_cumulative_incidence/` | `data/28_dataset.csv` |
| 29 | Диагностика | ROC-кривая | `29_roc/` | `data/29_dataset.csv` |
| 30 | Диагностика | precision–recall | `30_precision_recall/` | `data/30_dataset.csv` |
| 31 | Диагностика | calibration | `31_calibration/` | `data/31_dataset.csv` |
| 32 | Оценки эффекта | caterpillar plot | `32_caterpillar/` | `data/32_dataset.csv` |
| 33 | Оценки эффекта | funnel plot | `33_funnel/` | `data/33_dataset.csv` |

Порядок соответствует обучающей последовательности, а не порядку карточек
на карте. Полная карта с номерами — рисунок 4.1 раздела 4.

## Структура папки графика

```text
05_charts/01_line/
├── README.md
├── line.md              # текст раздела
├── line.typ             # дубликат для Typst
└── scripts/
    ├── make_data.py     # → data/01_dataset.csv
    ├── bad_plot.py      # → images/05_01_bad_line.*
    └── good_plot.py     # → images/05_01_good_line.*
```

## Правила

- у каждого графика — **свой** `make_data.py` и **свой**
  `data/NN_dataset.csv`; переиспользовать CSV другого графика нельзя;
- скрипты самодостаточны: данные пишутся в общий `data/`, рисунки — в общий
  `images/`;
- каждый рисунок сохраняется в SVG и PNG;
- плохой и правильный графики одного графика используют один и тот же CSV
  (это единственное допустимое совпадение);
- текст и Typst-дубликат правятся одновременно;
- дубли по смыслу (forest и slope встречаются в двух семействах) — это
  один раздел, а не два.

## Статус

| Раздел | Статус |
|---|---|
| 01_line | ✅ готов |
| 02_step … 33_funnel | ⏳ по запросу |
