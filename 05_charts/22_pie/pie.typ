// Раздел 5.22. Pie: части целого.
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

#heading(level: 1)[5.22 Pie: части целого]

Pie показывает доли целого. Он уместен только для *3–4 частей*,
когда нужно подчеркнуть «примерно половина/четверть», а не сравнивать
близкие значения. Для точного сравнения лучше bar/dot.

#heading(level: 2)[5.22.1 Сфера применения]

- 3–4 части целого;
- одна аудитория, один вывод;
- доли, которые легко узнать (50 %, 25 %);
- презентация, а не анализ.

Не подходит: много частей, близкие доли, отрицательные значения,
несколько кругов, точное сравнение.

#heading(level: 2)[5.22.2 Данные]

400 повторных госпитализаций, 4 причины.

#table(
  columns: (2.4fr, 0.8fr, 0.8fr),
  table.header([*Причина*], [*n*], [*Доля*]),
  [Сердечная недостаточность], [160], [40 %],
  [Инфекции], [100], [25 %],
  [Кровотечения], [80], [20 %],
  [Прочее], [60], [15 %],
)

Генератор: `05_charts/22_pie/scripts/make_data.py` → `data/22_dataset.csv`.

#heading(level: 2)[5.22.3 Плохой график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_22_bad_pie.png", width: 84%)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.22.1. Плохая pie: 3D-тени, explode, радуга, легенда.
  ]]
]

Код: `05_charts/22_pie/scripts/bad_plot.py`.

Ошибки: 3D-тени и explode искажают площадь, радуга, легенда вместо
подписей, нет процентов, заголовок «Причины».

#heading(level: 2)[5.22.4 Правильный график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_22_good_pie.png", width: 95mm)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.22.2. Правильная pie: 4 доли, подписи с n и %, без 3D.
  ]]
]

Код: `05_charts/22_pie/scripts/good_plot.py`.

Улучшения: 4 доли, старт на 12 часах, подписи «причина, n (%)»,
белые границы, без 3D, заголовок-вывод, 95 мм.

#heading(level: 2)[5.22.5 Было и стало]

#table(
  columns: (2fr, 2fr),
  table.header([*Было*], [*Стало*]),
  [3D, explode], [плоские доли],
  [радуга], [палитра Okabe–Ito],
  [легенда], [прямые подписи],
  [нет %], [n и %],
  [«Причины»], [«40 % — сердечная недостаточность»],
)

#heading(level: 2)[5.22.6 Чек-лист]

- ☐ 3–4 доли, сумма 100 %.
- ☐ Подписи с n и %.
- ☐ Нет 3D, explode, теней.
- ☐ Палитра различима.
- ☐ Старт на 12 часах, по часовой.
- ☐ Для сравнения предложен bar.
- ☐ Заголовок-вывод.
- ☐ Проверено в 95 мм.

#heading(level: 2)[5.22.7 Как воспроизвести]

```bash
uv sync
uv run python 05_charts/22_pie/scripts/make_data.py
uv run python 05_charts/22_pie/scripts/bad_plot.py
uv run python 05_charts/22_pie/scripts/good_plot.py
```

```python
ax.pie(values, labels=labels, colors=COLORS, startangle=90,
       counterclock=False, wedgeprops={"edgecolor": "white"})
```

#heading(level: 2)[5.22.8 Что дальше]

5.23 Treemap: иерархический состав.

#heading(level: 2)[Источники]

- Wilke C. O. _Fundamentals of Data Visualization_. 2019. —
  #link("https://clauswilke.com/dataviz/")[clauswilke.com/dataviz]
- Tufte E. R. _The Visual Display of Quantitative Information_. 1983. —
  #link("https://www.edwardtufte.com/tufte/books_vdqi")[edwardtufte.com]