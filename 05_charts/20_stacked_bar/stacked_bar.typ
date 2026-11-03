// Раздел 5.20. Stacked bar: состав целого.
// Сборка: typst compile --root . 05_charts/20_stacked_bar/stacked_bar.typ build/05_20_stacked_bar.pdf

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

#heading(level: 1)[5.20 Stacked bar: состав целого]

Stacked bar показывает не только общий объём, но и вклад категорий.
Он отвечает на вопрос: *из чего состоит целое и как состав меняется
между группами?*

Главное ограничение: сравнивать сегменты, которые начинаются не от
нуля, трудно. Поэтому stacked bar хорош для *2–4 категорий*, а для
точного сравнения долей лучше 100 % stacked bar (5.21) или dot.

#heading(level: 2)[5.20.1 Сфера применения]

Stacked bar отвечает на вопрос: *каков общий объём и из каких частей
он состоит?*

Типичные случаи:

- исходы госпитализации (выписан/переведён/умер);
- структура затрат по программам;
- возрастные группы в когорте;
- степени тяжести по отделениям;
- состав выборки по центрам.

Когда stacked bar *не* нужен:

- нужно сравнить отдельные сегменты — grouped bar/dot;
- частей много (5+) — 100 % stacked или таблица;
- важна динамика — line;
- части не складываются в целое;
- нулевая база недоступна.

#heading(level: 2)[5.20.2 Данные]

Сценарий: четыре отделения, три исхода — выписан, переведён, умер.

#table(
  columns: (1.6fr, 2.6fr, 1.2fr),
  table.header([*Колонка*], [*Смысл*], [*Единица*]),
  [`department`], [отделение], [—],
  [`outcome`], [исход], [—],
  [`patients`], [число пациентов], [человек],
)

Всего 3 180 пациентов. В ОРИТ переведены 44 % — больше, чем в других
отделениях.

Генератор: `05_charts/20_stacked_bar/scripts/make_data.py` → `data/20_dataset.csv`.

#heading(level: 2)[5.20.3 Плохой график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_20_bad_stacked_bar.png", width: 84%)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.20.1. Плохой stacked bar: обрезанная ось 700, радужные
    сегменты, тени, нет значений.
  ]]
]

Код: `05_charts/20_stacked_bar/scripts/bad_plot.py`.

Что с ним не так:

+ *Ось Y обрезана до 700.* Столбцы Терапии и Кардиологии
  обрезаны; общий объём не виден.
+ *Радужные сегменты, чёрные края, тени, «3D».*
+ *Нет подписей значений и общего числа.*
+ *Тяжёлая сетка, полная рамка.*
+ *Заголовок «Исходы».* Не сообщает вывод.
+ *Нет единиц и n.*

#heading(level: 2)[5.20.4 Правильный график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_20_good_stacked_bar.png", width: 85mm)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.20.2. Правильный stacked bar: горизонтальные столбцы,
    сортировка, палитра Okabe–Ito, значения и итоги.
  ]]
]

Код: `05_charts/20_stacked_bar/scripts/good_plot.py`.

Что улучшено:

+ *Горизонтально и отсортировано по общему числу.*
+ *Нулевая база и полный масштаб 0–1150.*
+ *Палитра Okabe–Ito* — различима при CVD.
+ *Значения внутри сегментов, итоги справа.*
+ *Легенда сверху, единицы, всего 3 180.*
+ *Заголовок-вывод:* в ОРИТ 44 % переведены.

Stacked bar показывает состав, но не заменяет сравнение долей:
для этого используйте 100 % stacked bar или dot + CI.

#heading(level: 2)[5.20.5 Сопоставление]

#table(
  columns: (1.5fr, 2fr, 2fr),
  table.header([*Что было*], [*Почему плохо*], [*Что сделано*]),
  [ось Y 0–700], [столбцы обрезаны], [0–1150],
  [радуга, тени], [декор, CVD], [Okabe–Ito],
  [без сортировки], [трудно читать], [сортировка по итогу],
  [нет значений], [оценка на глаз], [подписи сегментов],
  [нет итогов], [не виден объём], [итоги справа],
  [сетка по X и Y], [шум], [сетка только по X],
  [полная рамка], [визуальный шум], [только левая и нижняя оси],
  [«Исходы»], [нет вывода], [заголовок-вывод],
  [нет n], [непонятен масштаб], [всего 3 180],
)

#heading(level: 2)[5.20.6 Чек-лист stacked bar]

- ☐ Нулевая база.
- ☐ Частей 2–4, иначе 100 % stacked/таблица.
- ☐ Палитра различима при CVD.
- ☐ Значения/итоги подписаны.
- ☐ Указаны единицы и общее _n_.
- ☐ Порядок сегментов одинаков во всех столбцах.
- ☐ Сортировка по итогу или смыслу.
- ☐ Нет 3D и теней.
- ☐ Для сравнения долей — 100 % stacked/dot.
- ☐ Рисунок проверен в конечном размере 85 мм.

#heading(level: 2)[5.20.7 Как воспроизвести]

```bash
uv sync
uv run python 05_charts/20_stacked_bar/scripts/make_data.py
uv run python 05_charts/20_stacked_bar/scripts/bad_plot.py
uv run python 05_charts/20_stacked_bar/scripts/good_plot.py
```

Ключевой фрагмент:

```python
left = np.zeros(len(pivot))
for outcome, color in zip(OUTCOMES, COLORS, strict=True):
    ax.barh(pivot.index, pivot[outcome], left=left,
            color=color, label=outcome)
    left += pivot[outcome].to_numpy()
```

Сегменты должны идти в одном порядке; иначе сравнение столбцов
становится ловушкой.

#heading(level: 2)[5.20.8 Что дальше]

Следующий график — *5.21 bar 100 %*: нормированный состав.
У него будет свой генератор и свой `data/21_dataset.csv`.

#heading(level: 2)[Источники]

- Wilke C. O. _Fundamentals of Data Visualization_. 2019. —
  #link("https://clauswilke.com/dataviz/")[clauswilke.com/dataviz]
- Tufte E. R. _The Visual Display of Quantitative Information_. 1983. —
  #link("https://www.edwardtufte.com/tufte/books_vdqi")[edwardtufte.com]
- Matplotlib: `barh` —
  #link("https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html")[matplotlib.org]
