// Раздел 5.12. Violin: форма распределения.
// Сборка: typst compile --root . 05_charts/12_violin/violin.typ build/05_12_violin.pdf

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

#heading(level: 1)[5.12 Violin: форма распределения]

Violin plot — это зеркальная оценка плотности (KDE). Ширина скрипки
показывает, как часто встречаются значения; форма — модальность,
скошенность, хвосты. В отличие от boxplot, violin не прячет форму
за коробкой.

Но violin — это *оценка*, а не исходные данные. Ширина зависит от
bandwidth, хвосты могут выходить за реальный диапазон, а при малых _n_
контур становится фантазией. Поэтому внутри скрипки нужна сводка:
квартильные линии или коробка.

#heading(level: 2)[5.12.1 Сфера применения]

Violin отвечает на вопрос: *как выглядит форма распределения
в каждой группе?*

Где это пригодится:

- сравнение 2–5 групп по непрерывной величине;
- поиск модальности/двугорбости;
- проверка формы перед выбором теста;
- замена boxplot, когда форма важна;
- презентация распределений в больших выборках.

Когда violin *не* нужен:

- _n_ меньше ~20 — лучше точки/strip;
- нужны точные квантили — ECDF;
- групп много — small multiples;
- данные цензурированы — Kaplan–Meier;
- важна только медиана/IQR — boxplot.

#heading(level: 2)[5.12.2 Данные]

Сценарий: 600 пациентов, три стадии ХБП (1–2, 3, 4–5). Показатель —
eGFR (мл/мин/1,73 м²), по 200 человек в группе.

#table(
  columns: (1.8fr, 2.4fr, 1.2fr),
  table.header([*Колонка*], [*Смысл*], [*Единица*]),
  [`patient_id`], [идентификатор пациента], [—],
  [`ckd_stage`], [стадия ХБП], [—],
  [`sex`], [пол], [—],
  [`egfr_ml_min_1_73m2`], [СКФ], [мл/мин/1,73 м²],
)

Медианы: 88,2; 44,0; 20,8 мл/мин/1,73 м². Распределения сдвигаются
вниз, форма меняется.

Генератор: `05_charts/12_violin/scripts/make_data.py` →
`data/12_dataset.csv`.

#heading(level: 2)[5.12.3 Плохой график]

#block(breakable: false)[
  #align(center)[
    #image("../../images/05_12_bad_violin.png", width: 84%)
  ]
  #v(2pt)
  #align(center)[
    #text(size: 8.5pt, style: "italic")[
      Рисунок 5.12.1. Плохой violin: обрезанная ось 25–100, радужные
      тела, нет медиан и точек.
    ]
  ]
]

Код: `05_charts/12_violin/scripts/bad_plot.py`.

Что не так:

+ *Ось Y обрезана до 25–100.* Стадия 4–5 и верхний хвост
  стадии 1–2 скрыты; форма искажена.
+ *Радужные тела и толстые чёрные контуры.* Декор, CVD.
+ *Нет медианы, квартилей и точек.* Видна форма, но нет сводки
  и исходных наблюдений.
+ *Тяжёлая сетка, полная рамка.*
+ *Заголовок «eGFR и стадия ХБП».* Не сообщает направление.
+ *Нет единиц и _n_.*

#heading(level: 2)[5.12.4 Violin с квартильными линиями]

#block(breakable: false)[
  #align(center)[
    #image("../../images/05_12_good_violin_quart.png", width: 85mm)
  ]
  #v(2pt)
  #align(center)[
    #text(size: 8.5pt, style: "italic")[
      Рисунок 5.12.2. Правильный violin: полный диапазон 0–130,
      квартильные линии, точки, n = 200.
    ]
  ]
]

Код: `05_charts/12_violin/scripts/good_violin_quart.py`.

Что изменилось:

+ *Полный диапазон 0–130.* Все стадии и хвосты видны.
+ *Один цвет, без радуги.*
+ *Квартили и медиана — горизонтальными линиями.*
  Медиана толще, Q1/Q3 тоньше.
+ *Точки с jitter.* Видны наблюдения и размер групп.
+ *Единицы, _n_ = 200, заголовок-вывод.*
+ *Лёгкая сетка по Y, 85 мм.*

#heading(level: 2)[5.12.5 Violin с внутренней коробкой]

#block(breakable: false)[
  #align(center)[
    #image("../../images/05_12_good_violin_box.png", width: 85mm)
  ]
  #v(2pt)
  #align(center)[
    #text(size: 8.5pt, style: "italic")[
      Рисунок 5.12.3. Violin с прямоугольной коробкой внутри:
      медиана, IQR, усы и точки.
    ]
  ]
]

Код: `05_charts/12_violin/scripts/good_violin_box.py`.

Это версия «violin + прямоугольники»: внутри каждой скрипки —
мини-коробка с медианой, IQR и усами. Она полезна, когда нужно
одновременно показать форму (violin) и классическую сводку (box).

На что смотреть: коробка внутри должна быть узкой, иначе она закрывает
скрипку. Усы и выбросы можно не показывать, если точки уже нанесены;
но тогда это нужно указать в подписи.

#heading(level: 2)[5.12.6 Было и стало]

#table(
  columns: (1.5fr, 2fr, 2fr),
  table.header([*Что было*], [*Почему плохо*], [*Что сделано*]),
  [ось Y 25–100], [стадия 4–5 обрезана], [0–130],
  [радуга, толстые контуры], [декор, CVD], [один синий цвет],
  [нет медиан], [нет сводки], [квартильные линии / коробка],
  [нет точек], [не видно наблюдений], [jitter-точки],
  [сетка по X и Y], [шум], [сетка только по Y],
  [полная рамка], [визуальный шум], [только левая и нижняя оси],
  [«eGFR и стадия ХБП»], [нет сообщения], [заголовок-вывод],
  [нет единиц и n], [невозможно прочитать], [единицы, n = 200],
  [только violin], [нет сводки], [violin + quart / box],
)

#heading(level: 2)[5.12.7 Чек-лист violin]

- ☐ Ось Y не обрезает хвосты.
- ☐ Указаны единицы и _n_.
- ☐ Внутри есть медиана/IQR (линии или коробка).
- ☐ Точки показаны, если _n_ небольшое.
- ☐ Bandwidth/trim не скрывают структуру.
- ☐ Нет радуги и тяжёлых контуров.
- ☐ Для малых _n_ выбран strip/dot.
- ☐ Для многих групп — small multiples.
- ☐ Форма не интерпретируется как «точная» плотность.
- ☐ Рисунок проверен в конечном размере 85 мм.

#heading(level: 2)[5.12.8 Как воспроизвести]

```bash
uv sync
uv run python 05_charts/12_violin/scripts/make_data.py
uv run python 05_charts/12_violin/scripts/bad_plot.py
uv run python 05_charts/12_violin/scripts/good_violin_quart.py
uv run python 05_charts/12_violin/scripts/good_violin_box.py
```

Ключевые фрагменты:

```python
violins = ax.violinplot(data, positions=[1, 2, 3], widths=0.8,
                        showextrema=False, points=100)
for body in violins["bodies"]:
    body.set_facecolor(PRIMARY_BLUE)
    body.set_alpha(0.15)

# квартильные линии
q1, median, q3 = np.percentile(values, [25, 50, 75])
ax.hlines([q1, q3], position - 0.1, position + 0.1, color=PRIMARY_BLUE)
ax.hlines(median, position - 0.12, position + 0.12, color="#333333", linewidth=1.3)

# коробка внутри
ax.boxplot(data, positions=[1, 2, 3], widths=0.16, patch_artist=True,
           showfliers=False, boxprops={"facecolor": "white"})
```

#heading(level: 2)[5.12.9 Что дальше]

Следующий график — *5.13 strip*: отдельные точки по группам без
коробки. У него будет свой генератор и свой `data/13_dataset.csv`.

#heading(level: 2)[Источники]

- Wilke C. O. _Fundamentals of Data Visualization_. 2019. —
  #link("https://clauswilke.com/dataviz/")[clauswilke.com/dataviz]
- Hintze J. L., Nelson R. D. Violin Plots: A Box Plot-Density Trace
  Synergism #text("//") _The American Statistician_. 1998. —
  #link("https://doi.org/10.1080/00031305.1998.10480559")[doi:10.1080/00031305.1998.10480559]
- Matplotlib: `violinplot` —
  #link("https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.violinplot.html")[matplotlib.org]
- Weissgerber T. L. et al. Beyond Bar and Line Graphs #text("//") _PLoS Biology_.
  2015. — #link("https://doi.org/10.1371/journal.pbio.1002128")[doi:10.1371/journal.pbio.1002128]