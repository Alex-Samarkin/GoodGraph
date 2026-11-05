// Раздел 5.24. Heatmap: матрица значений.
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

#heading(level: 1)[5.24 Heatmap: матрица значений]

Heatmap кодирует значение цветом в сетке «строка × столбец». Он хорош
для матриц 5×5–50×50, но требует *упорядочивания*, *подписей* и
*colorbar*: иначе цвет не читается.

#heading(level: 2)[5.24.1 Сфера применения]

- время ожидания по отделениям и часам;
- показатели по центрам и месяцам;
- матрица различий/ошибок;
- тепловая карта загрузки.

Не подходит: мало значений (bar), точное сравнение (таблица),
непрерывные двумерные данные (hexbin/contour).

#heading(level: 2)[5.24.2 Данные]

5 отделений × 6 часов, среднее время ожидания (мин).

#table(
  columns: (1.5fr, 2fr, 1.2fr),
  table.header([*Колонка*], [*Смысл*], [*Единица*]),
  [`department`], [отделение], [—],
  [`hour`], [час], [ч],
  [`wait_min`], [ожидание], [мин],
)

Хирургия — самое долгое ожидание; пик — 10–12 часов.

Генератор: `05_charts/24_heatmap/scripts/make_data.py` → `data/24_dataset.csv`.

#heading(level: 2)[5.24.3 Плохой график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_24_bad_heatmap.png", width: 84%)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.24.1. Плохая heatmap: jet, нет значений и единиц,
    без сортировки.
  ]]
]

Код: `05_charts/24_heatmap/scripts/bad_plot.py`.

Ошибки: `jet`, нет чисел в ячейках, нет единиц у colorbar, строки не
упорядочены, заголовок «Время ожидания» без вывода.

#heading(level: 2)[5.24.4 Правильный график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_24_good_heatmap.png", width: 85mm)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.24.2. Правильная heatmap: cividis, значения в ячейках,
    colorbar «Минуты», сортировка.
  ]]
]

Код: `05_charts/24_heatmap/scripts/good_plot.py`.

Улучшения: `cividis`, значения в ячейках, colorbar «Минуты», строки
отсортированы по среднему, подписи часов, заголовок-вывод, 85 мм.

#heading(level: 2)[5.24.5 Чек-лист]

- ☐ Строки/столбцы упорядочены осмысленно.
- ☐ Значения подписаны или есть colorbar с единицами.
- ☐ Палитра последовательная/дивергентная по смыслу.
- ☐ Нет `jet`.
- ☐ Указаны единицы и _n_.
- ☐ Ячейки не искажены (aspect auto/equal осознанно).
- ☐ Заголовок-вывод.
- ☐ Проверено в 85 мм.

#heading(level: 2)[5.24.6 Как воспроизвести]

```bash
uv sync
uv run python 05_charts/24_heatmap/scripts/make_data.py
uv run python 05_charts/24_heatmap/scripts/bad_plot.py
uv run python 05_charts/24_heatmap/scripts/good_plot.py
```

#heading(level: 2)[5.24.7 Что дальше]

5.25 Clustermap: heatmap с кластеризацией.

#heading(level: 2)[Источники]

- Wilke C. O. _Fundamentals of Data Visualization_. 2019. —
  #link("https://clauswilke.com/dataviz/")[clauswilke.com/dataviz]
- Matplotlib: `imshow` —
  #link("https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html")[matplotlib.org]