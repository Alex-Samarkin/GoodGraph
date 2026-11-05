// Раздел 5.13. Strip: все точки по группам.
// Сборка: typst compile --root . 05_charts/13_strip/strip.typ build/05_13_strip.pdf

#set page(
  paper: "a4",
  margin: (x: 21mm, y: 20mm),
  numbering: "1",
)
#set text(
  font: ("Liberation Serif", "DejaVu Serif"),
  size: 10.5pt,
  lang: "ru",
  hyphenate: true,
)
#set par(justify: true, leading: 0.64em, spacing: 1.05em)
#set heading(numbering: none)
#show heading: set text(font: ("Liberation Sans", "DejaVu Sans"), weight: "bold")
#show heading: set text(hyphenate: false)
#show heading.where(level: 1): set text(size: 17pt)
#show heading.where(level: 2): set text(size: 13.5pt)
#show heading.where(level: 3): set text(size: 11.5pt)
#show heading: it => block(above: 1.15em, below: 0.55em, it)
#set list(indent: 1.2em, spacing: 0.5em)
#set enum(indent: 1.2em, spacing: 0.5em)
#set table(stroke: 0.5pt + luma(190), inset: (x: 5pt, y: 4pt))
#show table: set text(size: 9pt)
#show raw: set text(font: "DejaVu Sans Mono", size: 8.2pt)
#show raw.where(block: true): it => block(
  fill: luma(247),
  inset: 8pt,
  radius: 2pt,
  width: 100%,
  stroke: 0.5pt + luma(220),
  breakable: false,
  it,
)

#heading(level: 1)[5.13 Strip: все точки по группам]

Strip plot (jitter plot) показывает каждое наблюдение: точки
располагаются по группам, а небольшой случайный сдвиг по X не даёт им
слиться. Это самый честный способ сравнить небольшие выборки: видны
разброс, выбросы и форма, а не только медиана.

Jitter — не декор и не «шум». Он должен быть случайным, но
воспроизводимым (seed), и не настолько большим, чтобы точки уходили
в соседнюю группу.

#heading(level: 2)[5.13.1 Сфера применения]

Strip отвечает на вопрос: *как выглядят все наблюдения в группах
и где медиана?*

Где это пригодится:

- небольшие выборки (10–50 на группу);
- сравнение 2–5 групп без коробки;
- показ выбросов и гетерогенности;
- замена bar/box, когда важны отдельные пациенты;
- проверка, не скрывает ли среднее бимодальность.

Когда strip *не* нужен:

- точек тысячи — overplotting, нужны hexbin/contour;
- нужны точные квантили — ECDF;
- важна только сводка — box/dot;
- группы сильно разного размера — точки могут перегрузить ось;
- jitter скрывает реальную структуру (например, дискретные значения).

#heading(level: 2)[5.13.2 Данные]

Сценарий: 90 пациентов, три схемы обезболивания — НПВС, опиоид,
комбинация. Через 24 часа — боль по ВАШ (0–100 мм), по 30 человек
в группе.

#table(
  columns: (1.4fr, 2.8fr, 1.2fr),
  table.header([*Колонка*], [*Смысл*], [*Единица*]),
  [`patient_id`], [идентификатор пациента], [—],
  [`analgesia`], [схема обезболивания], [—],
  [`vas_mm`], [боль по ВАШ], [мм],
)

Медианы: НПВС — 56, опиоид — 45,5, комбинация — 32,5 мм.

Генератор: `05_charts/13_strip/scripts/make_data.py` →
`data/13_dataset.csv`.

#heading(level: 2)[5.13.3 Плохой график]

#block(breakable: false)[
  #align(center)[
    #image("../../images/05_13_bad_strip.png", width: 84%)
  ]
  #v(2pt)
  #align(center)[
    #text(size: 8.5pt, style: "italic")[
      Рисунок 5.13.1. Плохой strip: точки без jitter, радуга,
      обрезанная ось 30–70, нет медиан и n.
    ]
  ]
]

Код: `05_charts/13_strip/scripts/bad_plot.py`.

Что не так:

+ *Нет jitter.* 30 точек в каждой группе стоят строго по одной
  вертикали и сливаются; видно не распределение, а плотность
  наложения.
+ *Радужные точки по группам.* Цвет дублирует ось X, CVD.
+ *Обрезанная ось Y (30–70).* Низкие и высокие значения скрыты.
+ *Крупные непрозрачные точки, тяжёлая сетка, полная рамка.*
+ *Заголовок «Боль по группам».* Не сообщает, какая схема лучше.
+ *Нет медиан, единиц и n.*

#heading(level: 2)[5.13.4 Правильный график]

#block(breakable: false)[
  #align(center)[
    #image("../../images/05_13_good_strip.png", width: 85mm)
  ]
  #v(2pt)
  #align(center)[
    #text(size: 8.5pt, style: "italic")[
      Рисунок 5.13.2. Правильный strip: jitter, один цвет, полный
      диапазон 0–100, медианы, n = 30.
    ]
  ]
]

Код: `05_charts/13_strip/scripts/good_plot.py`.

Что изменилось:

+ *Jitter по X.* Все 30 точек видны отдельно; jitter
  воспроизводимый.
+ *Один цвет, alpha = 0,65.* Нет двойного кодирования.
+ *Полный диапазон 0–100 мм.*
+ *Медиана — горизонтальная линия* в каждой группе.
+ *n = 30, единицы, заголовок-вывод.*
+ *Лёгкая сетка только по Y, 85 мм.*

Strip особенно хорош, когда _n_ небольшое: читатель видит каждого
пациента, а не только сводку. При больших _n_ точки всё равно
сливаются — тогда нужны box/violin/hexbin.

#heading(level: 2)[5.13.5 Было и стало]

#table(
  columns: (1.5fr, 2fr, 2fr),
  table.header([*Что было*], [*Почему плохо*], [*Что сделано*]),
  [нет jitter], [точки сливаются], [jitter 0,09],
  [радуга], [CVD, двойное кодирование], [один цвет],
  [ось Y 30–70], [хвосты скрыты], [0–100],
  [крупные точки], [шум], [s=18, alpha=0,65],
  [нет медиан], [нет сводки], [горизонтальные медианы],
  [сетка по X и Y], [шум], [сетка только по Y],
  [полная рамка], [визуальный шум], [только левая и нижняя оси],
  [«Боль по группам»], [нет сообщения], [заголовок-вывод],
  [нет единиц и n], [невозможно прочитать], [«мм», n = 30],
)

#heading(level: 2)[5.13.6 Чек-лист strip]

- ☐ Jitter есть и он воспроизводимый.
- ☐ Jitter не переносит точки в чужую группу.
- ☐ Ось Y не обрезает хвосты.
- ☐ Указаны единицы и _n_.
- ☐ Медиана/среднее показаны, если нужна сводка.
- ☐ Цвет не дублирует ось X.
- ☐ Точек не слишком много; иначе box/hexbin.
- ☐ Дискретные значения не «размазаны» jitter’ом.
- ☐ Группы одинаково читаемы.
- ☐ Рисунок проверен в конечном размере 85 мм.

#heading(level: 2)[5.13.7 Как воспроизвести]

```bash
uv sync
uv run python 05_charts/13_strip/scripts/make_data.py
uv run python 05_charts/13_strip/scripts/bad_plot.py
uv run python 05_charts/13_strip/scripts/good_plot.py
```

Вот как это выглядит в коде:

```python
for position, group in enumerate(GROUPS, start=1):
    values = df.loc[df["analgesia"] == group, "vas_mm"].to_numpy()
    jitter = rng.normal(0.0, 0.09, len(values))
    ax.scatter(position + jitter, values,
               s=18, color=PRIMARY_BLUE, alpha=0.65, linewidths=0)
    ax.hlines(np.median(values), position - 0.18, position + 0.18,
              color="#333333", linewidth=1.5)
```

`rng.normal(0, 0.09)` — компромисс: достаточно, чтобы развести точки,
но не настолько, чтобы смешать группы. Seed фиксируйте в подписи
или коде.

#heading(level: 2)[5.13.8 Что дальше]

Следующий график — *5.14 dot + CI*: точка оценки и доверительный
интервал. У него будет свой генератор и свой `data/14_dataset.csv`.

#heading(level: 2)[Источники]

- Wilke C. O. _Fundamentals of Data Visualization_. 2019. —
  #link("https://clauswilke.com/dataviz/")[clauswilke.com/dataviz]
- Weissgerber T. L. et al. Beyond Bar and Line Graphs #text("//") _PLoS Biology_.
  2015. — #link("https://doi.org/10.1371/journal.pbio.1002128")[doi:10.1371/journal.pbio.1002128]
- Matplotlib: `scatter` —
  #link("https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html")[matplotlib.org]
- Tufte E. R. _The Visual Display of Quantitative Information_. 1983. —
  #link("https://www.edwardtufte.com/tufte/books_vdqi")[edwardtufte.com]