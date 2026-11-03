# GoodGraph — методичка по научной графике на Python

Учебное пособие о том, как делать графики для научных статей, диссертаций и отчётов:
от принципов визуального мышления и нормативов оформления до готовых скриптов
на matplotlib, seaborn и plotnine.

## Что внутри

| Раздел | Папка | Содержание | Статус |
|---|---|---|---|
| 1 | [`01_principles/`](01_principles/) | Принципы качественной и правильной графики: смысл, честность, нормативы, оформление | ✅ готов |
| 2 | [`02_python/`](02_python/) | Экосистема Python: matplotlib, seaborn, plotnine; настройка среды через uv | ✅ готов |
| 3 | [`03_requirements/`](03_requirements/) | Требования: цветовые гаммы, шрифты, размеры, форматы | ✅ готов |
| 4 | [`04_overview/`](04_overview/) | Основные виды научных графиков и области применения | ✅ готов |
| 5 | [`05_charts/`](05_charts/) | Каждый график: данные → плохой пример → разбор → правильный пример | 🚧 01_line … 26_corr_matrix готовы |
| 6 | `06_conclusion/` | Общее заключение | ⏳ по запросу |
| 7 | `07_publication/` | Подготовка графиков к публикации в научном журнале | ⏳ по запросу |
| 8 | `08_sources/` | Источники и работы о визуализации данных и ПО для графиков | ⏳ по запросу |

## Структура репозитория

```
GoodGraph/
├── pyproject.toml          # зависимости и настройки проекта (uv)
├── uv.lock                 # зафиксированные версии пакетов
├── .python-version         # Python 3.12
├── src/goodgraph/          # общий стиль, палитры, сохранение рисунков
├── data/                   # все наборы данных (NN_dataset.csv)
├── images/                 # все рисунки (SVG + PNG)
├── 01_principles/          # раздел 1: текст, скрипты, typst-дубликат
├── 02_python/              # раздел 2: библиотеки, uv, сравнение
├── 03_requirements/        # раздел 3: цвет, шрифты, размеры, форматы
├── 04_overview/            # раздел 4: карта видов графиков
├── 05_charts/              # раздел 5: графики, по одному на папку
├── typst/                  # сборка всей методички в PDF
├── build/                  # готовый PDF
└── Makefile                # команды: данные, рисунки, PDF
```

Каждый раздел и каждый вид графика живёт в своей папке. Внутри — тексты
(`*.md` и `*.typ`), а у видов графиков ещё и самодостаточные скрипты:

```
05_charts/01_line/
├── README.md          # краткое описание раздела
├── line.md            # текст методички
├── line.typ           # тот же текст для Typst
└── scripts/
    ├── make_data.py   # генерация реалистичных данных → data/NN_dataset.csv
    ├── bad_plot.py    # неудачный график → images/05_NN_bad_*.{svg,png}
    └── good_plot.py   # правильный график → images/05_NN_good_*.{svg,png}
```

## Быстрый старт

Нужны [uv](https://docs.astral.sh/uv/) и [Typst](https://typst.app/) (для PDF).

```bash
# 1. Окружение и зависимости
uv sync

# 2. Данные и рисунки разделов 1–5
uv run python 01_principles/scripts/make_data.py
uv run python 01_principles/scripts/bad_plot.py
uv run python 01_principles/scripts/good_plot.py
uv run python 02_python/scripts/make_data.py
uv run python 02_python/scripts/compare_libraries.py
uv run python 03_requirements/scripts/plot_palettes.py
uv run python 03_requirements/scripts/plot_cvd.py
uv run python 03_requirements/scripts/plot_fonts.py
uv run python 04_overview/scripts/plot_chart_map.py
uv run python 05_charts/01_line/scripts/make_data.py
uv run python 05_charts/01_line/scripts/bad_plot.py
uv run python 05_charts/01_line/scripts/good_plot.py
uv run python 05_charts/02_step/scripts/make_data.py
uv run python 05_charts/02_step/scripts/bad_plot.py
uv run python 05_charts/02_step/scripts/good_plot.py
uv run python 05_charts/03_area/scripts/make_data.py
uv run python 05_charts/03_area/scripts/bad_plot.py
uv run python 05_charts/03_area/scripts/good_plot.py
uv run python 05_charts/04_small_multiples/scripts/make_data.py
uv run python 05_charts/04_small_multiples/scripts/bad_plot.py
uv run python 05_charts/04_small_multiples/scripts/good_plot.py
uv run python 05_charts/05_scatter/scripts/make_data.py
uv run python 05_charts/05_scatter/scripts/bad_plot.py
uv run python 05_charts/05_scatter/scripts/good_plot.py
uv run python 05_charts/06_hexbin/scripts/make_data.py
uv run python 05_charts/06_hexbin/scripts/bad_plot.py
uv run python 05_charts/06_hexbin/scripts/good_plot.py
uv run python 05_charts/07_contour/scripts/make_data.py
uv run python 05_charts/07_contour/scripts/bad_plot.py
uv run python 05_charts/07_contour/scripts/good_plot.py
uv run python 05_charts/08_loess/scripts/make_data.py
uv run python 05_charts/08_loess/scripts/bad_plot.py
uv run python 05_charts/08_loess/scripts/good_plot.py
uv run python 05_charts/09_histogram/scripts/make_data.py
uv run python 05_charts/09_histogram/scripts/bad_plot.py
uv run python 05_charts/09_histogram/scripts/good_plot.py
uv run python 05_charts/10_ecdf/scripts/make_data.py
uv run python 05_charts/10_ecdf/scripts/bad_plot.py
uv run python 05_charts/10_ecdf/scripts/good_plot.py
uv run python 05_charts/11_box/scripts/make_data.py
uv run python 05_charts/11_box/scripts/bad_plot.py
uv run python 05_charts/11_box/scripts/good_box_points.py
uv run python 05_charts/11_box/scripts/good_violin_box.py
uv run python 05_charts/11_box/scripts/good_box_hist.py
uv run python 05_charts/12_violin/scripts/make_data.py
uv run python 05_charts/12_violin/scripts/bad_plot.py
uv run python 05_charts/12_violin/scripts/good_violin_quart.py
uv run python 05_charts/12_violin/scripts/good_violin_box.py
uv run python 05_charts/13_strip/scripts/make_data.py
uv run python 05_charts/13_strip/scripts/bad_plot.py
uv run python 05_charts/13_strip/scripts/good_plot.py
uv run python 05_charts/14_dot_ci/scripts/make_data.py
uv run python 05_charts/14_dot_ci/scripts/bad_plot.py
uv run python 05_charts/14_dot_ci/scripts/good_plot.py
uv run python 05_charts/15_bar/scripts/make_data.py
uv run python 05_charts/15_bar/scripts/bad_plot.py
uv run python 05_charts/15_bar/scripts/good_plot.py
uv run python 05_charts/16_forest/scripts/make_data.py
uv run python 05_charts/16_forest/scripts/bad_plot.py
uv run python 05_charts/16_forest/scripts/good_plot.py
uv run python 05_charts/17_slope/scripts/make_data.py
uv run python 05_charts/17_slope/scripts/bad_plot.py
uv run python 05_charts/17_slope/scripts/good_plot.py
uv run python 05_charts/18_paired_dot/scripts/make_data.py
uv run python 05_charts/18_paired_dot/scripts/bad_plot.py
uv run python 05_charts/18_paired_dot/scripts/good_plot.py
uv run python 05_charts/19_bland_altman/scripts/make_data.py
uv run python 05_charts/19_bland_altman/scripts/bad_plot.py
uv run python 05_charts/19_bland_altman/scripts/good_plot.py
uv run python 05_charts/20_stacked_bar/scripts/make_data.py
uv run python 05_charts/20_stacked_bar/scripts/bad_plot.py
uv run python 05_charts/20_stacked_bar/scripts/good_plot.py
uv run python 05_charts/21_bar_100/scripts/make_data.py
uv run python 05_charts/21_bar_100/scripts/bad_plot.py
uv run python 05_charts/21_bar_100/scripts/good_plot.py
uv run python 05_charts/22_pie/scripts/make_data.py
uv run python 05_charts/22_pie/scripts/bad_plot.py
uv run python 05_charts/22_pie/scripts/good_plot.py
uv run python 05_charts/23_treemap/scripts/make_data.py
uv run python 05_charts/23_treemap/scripts/bad_plot.py
uv run python 05_charts/23_treemap/scripts/good_plot.py
uv run python 05_charts/24_heatmap/scripts/make_data.py
uv run python 05_charts/24_heatmap/scripts/bad_plot.py
uv run python 05_charts/24_heatmap/scripts/good_plot.py
uv run python 05_charts/25_clustermap/scripts/make_data.py
uv run python 05_charts/25_clustermap/scripts/bad_plot.py
uv run python 05_charts/25_clustermap/scripts/good_plot.py
uv run python 05_charts/26_corr_matrix/scripts/make_data.py
uv run python 05_charts/26_corr_matrix/scripts/bad_plot.py
uv run python 05_charts/26_corr_matrix/scripts/good_plot.py

# 3. PDF всей методички
make pdf          # → build/metodichka.pdf
```

Если `uv` не может писать в домашний кеш (например, в песочнице),
задайте локальные каталоги:

```bash
export UV_CACHE_DIR="$PWD/.uv-cache"
export UV_PYTHON_INSTALL_DIR="$PWD/.uv-python"
uv sync
```

## Принципы оформления репозитория

- **Один вид графика — одна папка, свой генератор и свой датасет.**
  Скрипты не зависят от других скриптов: `make_data.py` пишет свой
  `data/NN_dataset.csv`, `bad_plot.py` и `good_plot.py` читают только его.
- **Данные — в `data/`, рисунки — в `images/`.** Данные: `NN_dataset.csv`;
  рисунки: `SS_<...>` для разделов и `05_NN_<...>` для видов графиков.
- **Все рисунки сохраняются в SVG и PNG** (вектор + растр для просмотра).
- **Текст и Typst синхронны.** При правке `.md` обязательно правится парный `.typ`.
- **Комментарии и подписи — по-русски**, код — по [PEP 8](https://peps.python.org/pep-0008/),
  проверка: `uv run ruff check .`.

## Лицензия

MIT. Данные в `data/` синтетические и не описывают реальных пациентов.
