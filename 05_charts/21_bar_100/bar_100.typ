// Раздел 5.21. Bar 100 %: нормированный состав.
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

#heading(level: 1)[5.21 Bar 100 %: нормированный состав]

100 % stacked bar показывает *доли*, а не абсолютные числа: каждый
столбец нормирован к 100 %. Он хорош, когда нужно сравнить состав
групп разного размера, но скрывает общий объём — поэтому _n_ нужно
указывать рядом.

#heading(level: 2)[5.21.1 Сфера применения]

- сравнение структуры по группам разного размера;
- доли исходов, степеней тяжести, возрастных групп;
- 2–4 категории;
- когда абсолютные итоги не важны.

Не подходит, если нужны абсолютные объёмы, частей больше 5 или
разница долей мала.

#heading(level: 2)[5.21.2 Данные]

4 возрастные группы × 3 степени тяжести, по 200 пациентов.

#table(
  columns: (1.5fr, 2fr, 1.2fr),
  table.header([*Колонка*], [*Смысл*], [*Единица*]),
  [`age_group`], [возрастная группа], [—],
  [`severity`], [лёгкая/средняя/тяжёлая], [—],
  [`patients`], [число пациентов], [человек],
)

Доля тяжёлой степени: 10 % (\<40), 20 % (40–59), 35 % (60–74),
57 % (75+).

Генератор: `05_charts/21_bar_100/scripts/make_data.py` → `data/21_dataset.csv`.

#heading(level: 2)[5.21.3 Плохой график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_21_bad_bar_100.png", width: 84%)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.21.1. Плохой 100 % bar: радуга, тени, нет подписей и n.
  ]]
]

Код: `05_charts/21_bar_100/scripts/bad_plot.py`.

Ошибки: радужные сегменты, тени, нет процентов внутри, нет _n_,
тяжёлая сетка, заголовок «Тяжесть по возрасту» без вывода.

#heading(level: 2)[5.21.4 Правильный график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_21_good_bar_100.png", width: 85mm)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.21.2. Правильный 100 % bar: доли подписаны, n справа,
    палитра Okabe–Ito.
  ]]
]

Код: `05_charts/21_bar_100/scripts/good_plot.py`.

Улучшения: горизонтально, порядок возрастов, палитра Okabe–Ito,
проценты внутри сегментов, _n_ = 200 справа, заголовок-вывод,
85 мм.

#heading(level: 2)[5.21.5 Сопоставление]

#table(
  columns: (2fr, 2fr),
  table.header([*Было*], [*Стало*]),
  [радуга, тени], [Okabe–Ito],
  [нет процентов], [подписи долей],
  [нет n], [n = 200],
  [нет вывода], [«Тяжёлая степень растёт с возрастом»],
)

#heading(level: 2)[5.21.6 Чек-лист]

- ☐ Столбцы нормированы к 100 %.
- ☐ Указаны доли и _n_.
- ☐ 2–4 сегмента.
- ☐ Порядок сегментов одинаков.
- ☐ Палитра CVD-безопасна.
- ☐ Нет 3D/теней.
- ☐ Заголовок-вывод.
- ☐ Проверено в 85 мм.

#heading(level: 2)[5.21.7 Как воспроизвести]

```bash
uv sync
uv run python 05_charts/21_bar_100/scripts/make_data.py
uv run python 05_charts/21_bar_100/scripts/bad_plot.py
uv run python 05_charts/21_bar_100/scripts/good_plot.py
```

```python
share = pivot.div(pivot.sum(axis=1), axis=0) * 100
ax.barh(share.index, share["тяжёлая"], left=..., color="#D55E00")
```

#heading(level: 2)[5.21.8 Что дальше]

5.22 Pie: части целого и почему pie редко бывает лучшим выбором.

#heading(level: 2)[Источники]

- Wilke C. O. _Fundamentals of Data Visualization_. 2019. —
  #link("https://clauswilke.com/dataviz/")[clauswilke.com/dataviz]
- Matplotlib: `barh` —
  #link("https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html")[matplotlib.org]
