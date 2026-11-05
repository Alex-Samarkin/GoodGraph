// Раздел 5.23. Treemap: иерархический состав.
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

#heading(level: 1)[5.23 Treemap: иерархический состав]

Treemap кодирует величину *площадью* прямоугольников. Он хорош для
иерархического состава (программы → подпрограммы), но плохо подходит
для точного сравнения: человек слабо оценивает площади.

#heading(level: 2)[5.23.1 Сфера применения]

- 5–20 категорий, составляющих целое;
- иерархия (программа → направление);
- акцент на крупнейших вкладчиках;
- презентация структуры затрат.

Не подходит: мало категорий (bar), точное сравнение, отрицательные
значения, динамика.

#heading(level: 2)[5.23.2 Данные]

Затраты по шести программам, всего 1 200 млн руб.

#table(
  columns: (2fr, 1fr),
  table.header([*Программа*], [*Млн руб.*]),
  [Кардиология], [320],
  [Онкология], [280],
  [Терапия], [210],
  [Хирургия], [180],
  [Педиатрия], [120],
  [Прочее], [90],
)

Кардиология и онкология — 50 % затрат.

Генератор: `05_charts/23_treemap/scripts/make_data.py` → `data/23_dataset.csv`.

#heading(level: 2)[5.23.3 Плохой график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_23_bad_treemap.png", width: 84%)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.23.1. Плохой treemap: радуга, толстые границы, тени,
    нет значений.
  ]]
]

Код: `05_charts/23_treemap/scripts/bad_plot.py`.

Ошибки: радуга, толстые чёрные границы, тени, только названия без
значений, нет процентов и итога.

#heading(level: 2)[5.23.4 Правильный график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_23_good_treemap.png", width: 85mm)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.23.2. Правильный treemap: последовательная палитра,
    подписи с млн руб., без границ.
  ]]
]

Код: `05_charts/23_treemap/scripts/good_plot.py`.

Улучшения: сортировка, последовательная палитра, подписи «программа
+ млн руб.», без границ и теней, заголовок-вывод, 85 мм.

#heading(level: 2)[5.23.5 Было и стало]

#table(
  columns: (2fr, 2fr),
  table.header([*Было*], [*Стало*]),
  [радуга], [последовательная палитра],
  [толстые границы], [без границ],
  [тени], [плоско],
  [нет значений], [подписи с млн],
  [нет вывода], [«50 % затрат»],
)

#heading(level: 2)[5.23.6 Чек-лист]

- ☐ Площадь пропорциональна величине.
- ☐ 5–20 категорий.
- ☐ Подписи с значениями.
- ☐ Последовательная палитра.
- ☐ Нет 3D/теней.
- ☐ Крупнейшие видны.
- ☐ Заголовок-вывод.
- ☐ Проверено в 85 мм.

#heading(level: 2)[5.23.7 Как воспроизвести]

```bash
uv sync
uv run python 05_charts/23_treemap/scripts/make_data.py
uv run python 05_charts/23_treemap/scripts/bad_plot.py
uv run python 05_charts/23_treemap/scripts/good_plot.py
```

```python
squarify.plot(sizes=df["cost_mln_rub"], label=labels,
              color=COLORS, ax=ax, pad=True)
```

#heading(level: 2)[5.23.8 Что дальше]

5.24 Heatmap: матрица значений.

#heading(level: 2)[Источники]

- Wilke C. O. _Fundamentals of Data Visualization_. 2019. —
  #link("https://clauswilke.com/dataviz/")[clauswilke.com/dataviz]
- Squarify —
  #link("https://github.com/laserson/squarify")[github.com/laserson/squarify]