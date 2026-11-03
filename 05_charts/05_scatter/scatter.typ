// Раздел 5.05. Scatter: связь двух непрерывных величин.
// Сборка: typst compile --root . 05_charts/05_scatter/scatter.typ build/05_05_scatter.pdf

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

#heading(level: 1)[5.05 Scatter: связь двух непрерывных величин]

Scatter plot — базовая форма для связи двух непрерывных переменных. Он
показывает не только тренд, но и разброс, выбросы, гетерогенность и
плотность наблюдений. Именно поэтому scatter честнее коэффициента
корреляции: коэффициент сжимает всю картину в одно число.

Правило: *точки важнее линии.* Линия регрессии — дополнение к данным,
а не замена им. Если на графике видны только линия и _r_, читатель не
увидит ни формы, ни выбросов.

#heading(level: 2)[5.05.1 Сфера применения]

Scatter отвечает на вопрос: *связаны ли две непрерывные величины
и как выглядит эта связь?*

Типичные случаи:

- связь биомаркера и клинического показателя (BMI и глюкоза, CRP и тяжесть);
- корреляция двух методов измерения (но для согласия — Bland–Altman, 5.19);
- зависимость дозы и эффекта;
- поиск выбросов и гетерогенности;
- проверка линейности перед регрессией.

Когда scatter *не* подходит:

- одна из переменных категориальная — нужны точки/столбцы;
- время по X — нужна линия (5.01);
- точек слишком много — overplotting, нужны hexbin (5.06),
  contour (5.07) или плотность;
- нужно показать согласие методов, а не корреляцию — Bland–Altman (5.19);
- обе переменные — доли, сумма которых фиксирована (compositional data).

#heading(level: 2)[5.05.2 Данные]

Сценарий: 180 взрослых на профилактическом осмотре. Измерены BMI
(кг/м²) и глюкоза натощак (ммоль/л).

#table(
  columns: (1.4fr, 2.8fr, 1.2fr),
  table.header([*Колонка*], [*Смысл*], [*Единица*]),
  [`patient_id`], [идентификатор пациента], [—],
  [`bmi_kg_m2`], [индекс массы тела], [кг/м²],
  [`glucose_mmol_l`], [глюкоза натощак], [ммоль/л],
)

Средний BMI — 27,5 ± 4,1 кг/м²; глюкоза — 5,7 ± 1,0 ммоль/л;
корреляция Пирсона _r_ = 0,52 (_p_ \< 0,001). Связь положительная,
но не жёсткая: вокруг линии большой разброс.

Генератор: `05_charts/05_scatter/scripts/make_data.py` →
`data/05_dataset.csv`.

#heading(level: 2)[5.05.3 Плохой график]

#block(breakable: false)[
  #align(center)[
    #image("../../images/05_05_bad_scatter.png", width: 84%)
  ]
  #v(2pt)
  #align(center)[
    #text(size: 8.5pt, style: "italic")[
      Рисунок 5.5.1. Плохой scatter: обрезанные оси, точки окрашены по BMI,
      крупные маркеры, линия без статистики.
    ]
  ]
]

Код: `05_charts/05_scatter/scripts/bad_plot.py`.

Что с ним не так:

+ *Обрезанные оси (20–38 и 4–10).* Часть точек и хвосты скрыты;
  форма связи и выбросы искажены.
+ *Цвет точек по BMI.* BMI уже на оси X; цвет дублирует ось
  и добавляет радужную шкалу, которая не несёт новой информации.
+ *Крупные непрозрачные маркеры с чёрной обводкой.* Overplotting:
  в плотных областях точки сливаются, нельзя оценить плотность.
+ *Красная линия регрессии без доверительной полосы и статистики.*
  Не указаны _r_, _n_, наклон; линия выглядит как «истина».
+ *Тяжёлая сетка по обеим осям и полная рамка.* Шум, который
  конкурирует с точками.
+ *Заголовок «Связь BMI и глюкозы».* Не сообщает направление
  и силу связи.
+ *Нет единиц и _n_.* «BMI» и «Глюкоза» — в чём? Сколько людей?
+ *Цветовая шкала BMI* дублирует ось X и занимает место.

#heading(level: 2)[5.05.4 Правильный график]

#block(breakable: false)[
  #align(center)[
    #image("../../images/05_05_good_scatter.png", width: 85mm)
  ]
  #v(2pt)
  #align(center)[
    #text(size: 8.5pt, style: "italic")[
      Рисунок 5.5.2. Правильный scatter: полный диапазон, полупрозрачные
      точки, линия регрессии, r и n.
    ]
  ]
]

Код: `05_charts/05_scatter/scripts/good_plot.py`.

Что улучшено:

+ *Полный диапазон осей.* 15–45 кг/м² и 3–12 ммоль/л; все точки
  видны, включая хвосты.
+ *Полупрозрачные точки одного цвета.* `alpha=0.35`, размер 12:
  видна плотность и не теряются отдельные наблюдения.
+ *Линия регрессии только в диапазоне данных.* Без экстраполяции
  за пределы наблюдений.
+ *Подпись _r_ = 0,52; _n_ = 180.* Связь quantified; читатель
  видит и форму, и число.
+ *Единицы на осях.* «BMI, кг/м²», «Глюкоза, ммоль/л».
+ *Заголовок-вывод.* «Глюкоза растёт с BMI» задаёт направление.
+ *Лёгкая сетка только по Y, без верхней и правой рамок.*
+ *85 мм.* Рисунок спроектирован в конечном размере.

Корреляция не равна причинности: BMI и глюкоза могут быть связаны
через возраст, питание, физическую активность. Scatter показывает
ассоциацию, а не механизм.

#heading(level: 2)[5.05.5 Сопоставление]

#table(
  columns: (1.5fr, 2fr, 2fr),
  table.header([*Что было*], [*Почему плохо*], [*Что сделано*]),
  [оси 20–38 / 4–10], [точки и хвосты обрезаны], [15–45 / 3–12],
  [цвет по BMI], [двойное кодирование, радуга], [один синий цвет],
  [крупные непрозрачные точки], [overplotting], [s=12, alpha=0,35],
  [линия без статистики], [не quantifies связь], [r, n, линия в диапазоне],
  [сетка по X и Y], [шум], [сетка только по Y],
  [полная рамка], [визуальный шум], [только левая и нижняя оси],
  [«Связь BMI и глюкозы»], [нет сообщения], [заголовок-вывод],
  [нет единиц и _n_], [невозможно прочитать], [единицы, _n_],
  [colorbar BMI], [дублирует ось], [без colorbar],
)

#heading(level: 2)[5.05.6 Чек-лист scatter]

- ☐ Обе переменные непрерывные.
- ☐ Оси не обрезают данные без объяснения.
- ☐ Есть _n_ и единицы.
- ☐ Точки не сливаются: alpha/размер/hexbin.
- ☐ Линия регрессии не выходит за диапазон данных.
- ☐ Указаны _r_ (или наклон) и неопределённость.
- ☐ Цвет не дублирует ось без смысла.
- ☐ Выбросы видны, а не скрыты.
- ☐ Корреляция не подана как причинность.
- ☐ Рисунок проверен в конечном размере 85 мм.

#heading(level: 2)[5.05.7 Как воспроизвести]

```bash
uv sync
uv run python 05_charts/05_scatter/scripts/make_data.py
uv run python 05_charts/05_scatter/scripts/bad_plot.py
uv run python 05_charts/05_scatter/scripts/good_plot.py
```

Ключевой фрагмент:

```python
ax.scatter(x, y, s=12, color=PRIMARY_BLUE, alpha=0.35, linewidths=0)
slope, intercept, r_value, p_value, _ = stats.linregress(x, y)
line_x = np.array([x.min(), x.max()])
ax.plot(line_x, intercept + slope * line_x, color="#333333", linewidth=1.4)
```

Если точек станет больше нескольких тысяч, scatter превратится
в сплошное пятно; тогда нужны hexbin или contour.

#heading(level: 2)[5.05.8 Что дальше]

Следующий график — *5.06 hexbin*: плотность тысяч точек без
overplotting. У него будет свой генератор и свой `data/06_dataset.csv`.

#heading(level: 2)[Источники]

- Wilke C. O. _Fundamentals of Data Visualization_. 2019. —
  #link("https://clauswilke.com/dataviz/")[clauswilke.com/dataviz]
- Cleveland W. S., McGill R. Graphical Perception #text("//") _JASA_. 1984. —
  #link("https://doi.org/10.1080/01621459.1984.10478080")[doi:10.1080/01621459.1984.10478080]
- Tufte E. R. _The Visual Display of Quantitative Information_. 1983. —
  #link("https://www.edwardtufte.com/tufte/books_vdqi")[edwardtufte.com]
- Matplotlib: `scatter` —
  #link("https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html")[matplotlib.org]
