// Раздел 5.25. Clustermap: heatmap с кластеризацией.
#set page(paper: "a4", margin: (x: 21mm, y: 20mm), numbering: "1")
#set text(font: ("Liberation Serif", "DejaVu Serif"), size: 10.5pt, lang: "ru", hyphenate: true)
#set par(justify: true, leading: 0.64em, spacing: 1.05em)
#show heading: set text(font: ("Liberation Sans", "DejaVu Sans"), weight: "bold")
#show heading: set text(hyphenate: false)
#show heading.where(level: 1): set text(size: 17pt)
#show heading.where(level: 2): set text(size: 13.5pt)
#show heading: it => block(above: 1.15em, below: 0.55em, it)
#set list(indent: 1.2em, spacing: 0.5em)
#set enum(indent: 1.2em, spacing: 0.5em)
#set table(stroke: 0.5pt + luma(190), inset: (x: 5pt, y: 4pt))
#show table: set text(size: 9pt)
#show raw: set text(font: "DejaVu Sans Mono", size: 8.2pt)
#show raw.where(block: true): it => block(fill: luma(247), inset: 8pt, radius: 2pt, width: 100%, breakable: false, it)

#heading(level: 1)[5.25 Clustermap: heatmap с кластеризацией]

Clustermap — это heatmap, у которого строки и столбцы переставлены
иерархической кластеризацией. Он показывает блоки/кластеры, но
*не доказывает* их существование: дендрограмма — результат
выбранной метрики и linkage.

#heading(level: 2)[5.25.1 Сфера применения]

- экспрессия генов;
- биомаркеры по пациентам;
- матрицы расстояний;
- поиск блоков в больших матрицах.

Не подходит: малые матрицы, точное сравнение, данные без смысла
кластеризации.

#heading(level: 2)[5.25.2 Данные]

10 генов × 12 пациентов, экспрессия. Два кластера: G01–G05 выше
у S01–S06, G06–G10 — у S07–S12.

Генератор: `05_charts/25_clustermap/scripts/make_data.py` → `data/25_dataset.csv`.

#heading(level: 2)[5.25.3 Плохой график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_25_bad_clustermap.png", width: 84%)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.25.1. Плохой clustermap: без кластеризации и z-score, jet.
  ]]
]

Код: `05_charts/25_clustermap/scripts/bad_plot.py`.

Ошибки: нет кластеризации, нет z-score, `jet`, нет дендрограмм,
цвет не отражает отклонение от среднего.

#heading(level: 2)[5.25.4 Правильный график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_25_good_clustermap.png", width: 100%)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.25.2. Правильный clustermap: z-score, дендрограммы,
    diverging RdBu_r.
  ]]
]

Код: `05_charts/25_clustermap/scripts/good_plot.py`.

Улучшения: z-score по генам, `RdBu_r` с центром 0, дендрограммы,
подписи, заголовок, 120 мм. Цвет — отклонение от среднего гена.

#heading(level: 2)[5.25.5 Чек-лист]

- ☐ Понятно, что кластеризация — метод, а не истина.
- ☐ Указаны метрика/linkage или значение по умолчанию.
- ☐ z-score/нормировка осознанны.
- ☐ Палитра diverging с центром 0.
- ☐ Дендрограммы и подписи читаются.
- ☐ Нет `jet`.
- ☐ Указаны n и единицы.
- ☐ Проверено в 120 мм.

#heading(level: 2)[5.25.6 Как воспроизвести]

```bash
uv sync
uv run python 05_charts/25_clustermap/scripts/make_data.py
uv run python 05_charts/25_clustermap/scripts/bad_plot.py
uv run python 05_charts/25_clustermap/scripts/good_plot.py
```

#heading(level: 2)[5.25.7 Что дальше]

5.26 Corr matrix: корреляции.

#heading(level: 2)[Источники]

- Wilke C. O. _Fundamentals of Data Visualization_. 2019. —
  #link("https://clauswilke.com/dataviz/")[clauswilke.com/dataviz]
- Seaborn: `clustermap` —
  #link("https://seaborn.pydata.org/generated/seaborn.clustermap.html")[seaborn.pydata.org]