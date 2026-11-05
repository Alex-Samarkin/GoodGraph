// Раздел 5.16. Forest: эффект по подгруппам.
// Сборка: typst compile --root . 05_charts/16_forest/forest.typ build/05_16_forest.pdf

#set page(paper: "a4", margin: (x: 21mm, y: 20mm), numbering: "1")
#set text(font: ("Liberation Serif", "DejaVu Serif"), size: 10.5pt, lang: "ru", hyphenate: true)
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
#show raw.where(block: true): it => block(fill: luma(247), inset: 8pt, radius: 2pt, width: 100%, stroke: 0.5pt + luma(220), breakable: false, it)

#heading(level: 1)[5.16 Forest: эффект по подгруппам]

Forest plot — это ряд оценок эффекта с доверительными интервалами,
выстроенных по вертикали. Он показывает не только «где эффект»,
но и «насколько он точен» в каждой подгруппе.

Для отношений (OR, RR, HR) ось *обязательно логарифмическая*:
только тогда OR = 0,5 и OR = 2 симметричны относительно 1.
Линия «нет эффекта» — OR = 1 — обязательна.

#heading(level: 2)[5.16.1 Сфера применения]

Forest отвечает на вопрос: *каков эффект в подгруппах и перекрывают
ли интервалы единицу?*

Где это пригодится:

- подгрупповой анализ RCT;
- мета-анализ нескольких исследований;
- OR/RR/HR по центрам и стратам;
- проверка гетерогенности эффекта;
- честное представление неопределённости.

Когда forest *не* нужен:

- одна оценка — dot + CI;
- нужны исходные распределения — box/strip;
- нет общего эффекта и осмысленной группировки;
- подгруппы выбраны post hoc без поправки;
- эффект выражен в абсолютных единицах без лог-шкалы.

#heading(level: 2)[5.16.2 Данные]

Сценарий: RCT, 800 пациентов (400 лечение / 400 контроль), исход —
осложнение. Эффект — OR с 95 % CI Уолфа; восемь подгрупп и общая оценка.

#table(
  columns: (1.7fr, 2.2fr, 1.2fr),
  table.header([*Колонка*], [*Смысл*], [*Единица*]),
  [`subgroup`], [подгруппа], [—],
  [`n_treatment`], [n в группе лечения], [—],
  [`events_treatment`], [события в лечении], [—],
  [`n_control`], [n в контроле], [—],
  [`events_control`], [события в контроле], [—],
)

Общая OR — 0,62 (95 % ДИ 0,46–0,84). В подгруппах — 0,56–0,67;
у женщин, ≥65 лет и ХБП интервал пересекает 1.

Генератор: `05_charts/16_forest/scripts/make_data.py` → `data/16_dataset.csv`.

#heading(level: 2)[5.16.3 Плохой график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_16_bad_forest.png", width: 84%)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.16.1. Плохой forest: только точки OR, линейная ось,
    нет ДИ, линии 1 и общей оценки.
  ]]
]

Код: `05_charts/16_forest/scripts/bad_plot.py`.

Что не так:

+ *Нет доверительных интервалов.* Точка без CI не показывает
  неопределённость; подгруппы выглядят точнее, чем есть.
+ *Линейная ось OR.* Расстояния между 0,5 и 0,7 и между
  1,0 и 1,2 не сопоставимы; лог-шкала обязательна.
+ *Нет линии OR = 1.* Непонятно, где «нет эффекта».
+ *Радужные точки, тяжёлая сетка, полная рамка.*
+ *Нет общей оценки и n.*
+ *Заголовок «Эффект лечения».* Не сообщает направление
  и неопределённость.

#heading(level: 2)[5.16.4 Правильный график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_16_good_forest.png", width: 100%)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.16.2. Правильный forest: лог-ось 0,3–2, 95 % ДИ,
    линия 1, размер по n, ромб общей оценки.
  ]]
]

Код: `05_charts/16_forest/scripts/good_plot.py`.

Что изменилось:

+ *95 % ДИ для каждой подгруппы.*
+ *Логарифмическая ось 0,3–2,0.* OR симметричны
  относительно 1.
+ *Линия OR = 1* — референс «нет эффекта».
+ *Размер квадрата пропорционален n.* Видно, где оценка
  точнее.
+ *Ромб общей оценки* внизу; OR 0,62 (0,46–0,84).
+ *Справа — OR (95 % ДИ), слева — подгруппы.*
+ *Один цвет, лёгкая сетка, 170 мм.*

CI, пересекающие 1, — не «отсутствие эффекта», а недостаток
точности. Не ранжируйте подгруппы по p-value и не делайте
причинных выводов из подгруппового анализа.

#heading(level: 2)[5.16.5 Было и стало]

#table(
  columns: (1.5fr, 2fr, 2fr),
  table.header([*Что было*], [*Почему плохо*], [*Что сделано*]),
  [нет CI], [не видна неопределённость], [95 % ДИ],
  [линейная ось], [OR искажены], [лог-ось 0,3–2],
  [нет линии 1], [нет референса], [пунктир OR = 1],
  [радуга], [CVD, декор], [один цвет],
  [нет размера по n], [не видна точность], [размер квадрата],
  [нет общей оценки], [нет итога], [ромб],
  [нет таблицы справа], [нужно считать в уме], [OR (95 % ДИ)],
  [«Эффект лечения»], [нет сообщения], [заголовок о подгруппах],
  [нет n], [непонятна точность], [n в данных],
)

#heading(level: 2)[5.16.6 Чек-лист forest]

- ☐ Для OR/RR/HR — логарифмическая ось.
- ☐ Есть линия «нет эффекта» (1).
- ☐ Показаны 95 % ДИ, а не только точки.
- ☐ Размер маркера отражает вес/n.
- ☐ Есть общая оценка (ромб/линия).
- ☐ Подгруппы не ранжированы по значимости.
- ☐ Указаны n и единицы эффекта.
- ☐ CI, пересекающие 1, не поданы как «нет эффекта».
- ☐ Подгрупповой анализ не подан как причинный.
- ☐ Рисунок проверен в конечном размере.

#heading(level: 2)[5.16.7 Как воспроизвести]

```bash
uv sync
uv run python 05_charts/16_forest/scripts/make_data.py
uv run python 05_charts/16_forest/scripts/bad_plot.py
uv run python 05_charts/16_forest/scripts/good_plot.py
```

Вот как это выглядит в коде:

```python
odds = (a / b) / (c / d)
se = np.sqrt(1/a + 1/b + 1/c + 1/d)
low = np.exp(np.log(odds) - 1.96 * se)
high = np.exp(np.log(odds) + 1.96 * se)

ax.set_xscale("log")
ax.axvline(1, color="#777777", linestyle="--")
ax.hlines(y, low, high, color=PRIMARY_BLUE)
ax.scatter(odds, y, s=n_total / 3, color=PRIMARY_BLUE)
```

Для мета-анализа вместо OR Уолфа используйте модель
с фиксированным/случайным эффектом и вес исследований.

#heading(level: 2)[5.16.8 Что дальше]

Следующий график — *5.17 slope*: изменение показателя между двумя
точками для многих групп. У него будет свой генератор и свой
`data/17_dataset.csv`.

#heading(level: 2)[Источники]

- Cumming G. _Understanding the New Statistics_. Routledge, 2012. —
  #link("https://www.routledge.com/Understanding-the-New-Statistics-Effect-Sizes-Confidence-Intervals-and-Meta-Analysis/Cumming/p/book/9780415879682")[routledge.com]
- Cochrane Handbook, Chapter 10 —
  #link("https://training.cochrane.org/handbook")[training.cochrane.org]
- Wilke C. O. _Fundamentals of Data Visualization_. 2019. —
  #link("https://clauswilke.com/dataviz/")[clauswilke.com/dataviz]
- Matplotlib: `hlines` —
  #link("https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hlines.html")[matplotlib.org]