// Раздел 5.15. Bar: сравнение величин.
// Сборка: typst compile --root . 05_charts/15_bar/bar.typ build/05_15_bar.pdf

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

#heading(level: 1)[5.15 Bar: сравнение величин]

Bar chart сравнивает *агрегированные величины* по категориям:
число госпитализаций, затраты, койко-дни, объём выборки. Это не график
распределения и не график тренда: для распределения — histogram/box,
для времени — line.

Главное: *нулевая база обязательна*. Длина столбца должна
быть пропорциональна величине; обрезанная ось превращает небольшую
разницу в «драму».

#heading(level: 2)[5.15.1 Сфера применения]

Bar отвечает на вопрос: *какая категория больше и насколько?*

Где это пригодится:

- число пациентов/госпитализаций по отделениям;
- затраты или койко-дни по программам;
- объём выборки по центрам;
- сравнение немногих категорий (2–8);
- рейтинг, где важна абсолютная величина.

Когда bar *не* нужен:

- нужно распределение — histogram/box/violin;
- динамика во времени — line;
- много категорий — horizontal bar или dot;
- важна точность оценки — dot + CI;
- части целого — stacked bar 100 % (5.21), не pie (5.22).

#heading(level: 2)[5.15.2 Данные]

Сценарий: пять отделений больницы, число госпитализаций за год.
Величины — счётчики, поэтому столбцы уместны.

#table(
  columns: (1.4fr, 2.8fr, 1.2fr),
  table.header([*Колонка*], [*Смысл*], [*Единица*]),
  [`department`], [отделение], [—],
  [`admissions`], [госпитализаций за год], [число],
)

Терапия — 1 240, хирургия — 980, кардиология — 860, урология — 540,
офтальмология — 420. Всего 4 040.

Генератор: `05_charts/15_bar/scripts/make_data.py` → `data/15_dataset.csv`.

#heading(level: 2)[5.15.3 Плохой график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_15_bad_bar.png", width: 84%)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.15.1. Плохой bar: обрезанная ось 800–1300, радужные
    столбцы, тени, нет значений.
  ]]
]

Код: `05_charts/15_bar/scripts/bad_plot.py`.

Что не так:

+ *Ось Y обрезана до 800–1300.* Нулевая база скрыта; столбцы
  540 и 420 вообще не видны, а разница между 980 и 1 240
  преувеличена.
+ *Радужные столбцы, чёрные края и тени.* Декор, CVD.
+ *Отделения не отсортированы.* Глаз не может ранжировать.
+ *Тяжёлая сетка по обеим осям и полная рамка.*
+ *Заголовок «Госпитализации».* Не сообщает вывод.
+ *Нет значений на столбцах, единиц и n.*

#heading(level: 2)[5.15.4 Правильный график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_15_good_bar.png", width: 85mm)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.15.2. Правильный bar: горизонтальные сортированные
    столбцы, нулевая база, значения, всего 4 040.
  ]]
]

Код: `05_charts/15_bar/scripts/good_plot.py`.

Что изменилось:

+ *Горизонтальные столбцы.* Длинные названия отделений
  читаются без поворота.
+ *Сортировка по величине.* Ранжирование очевидно.
+ *Нулевая база.* Ось X начинается с 0; длины пропорциональны.
+ *Значения подписаны* прямо у столбцов.
+ *Один цвет, без теней и 3D.*
+ *Единицы, общее число 4 040, заголовок-вывод, 85 мм.*

Bar — не «универсальный график». Если нужна форма распределения,
он её не покажет; если нужна динамика, он её скроет.

#heading(level: 2)[5.15.5 Было и стало]

#table(
  columns: (1.5fr, 2fr, 2fr),
  table.header([*Что было*], [*Почему плохо*], [*Что сделано*]),
  [ось Y 800–1300], [нулевая база скрыта], [0–1400],
  [радуга, тени], [декор], [один цвет],
  [без сортировки], [трудно ранжировать], [сортировка],
  [вертикально], [подписи наклонены], [горизонтально],
  [нет значений], [нужно оценивать на глаз], [подписи значений],
  [сетка по X и Y], [шум], [сетка только по X],
  [полная рамка], [визуальный шум], [только левая и нижняя оси],
  [«Госпитализации»], [нет вывода], [заголовок-вывод],
  [нет единиц и n], [непонятно, что считать], [«за год», всего 4 040],
)

#heading(level: 2)[5.15.6 Чек-лист bar]

- ☐ Ось начинается с нуля.
- ☐ Длина пропорциональна величине.
- ☐ Категории отсортированы, если нет смыслового порядка.
- ☐ Значения подписаны или легко читаются.
- ☐ Указаны единицы и период.
- ☐ Один цвет, без 3D/теней.
- ☐ Длинные подписи — горизонтально.
- ☐ Для распределения выбран histogram/box.
- ☐ Для тренда выбрана line.
- ☐ Рисунок проверен в конечном размере 85 мм.

#heading(level: 2)[5.15.7 Как воспроизвести]

```bash
uv sync
uv run python 05_charts/15_bar/scripts/make_data.py
uv run python 05_charts/15_bar/scripts/bad_plot.py
uv run python 05_charts/15_bar/scripts/good_plot.py
```

Вот как это выглядит в коде:

```python
df = pd.read_csv(...).sort_values("admissions")
bars = ax.barh(df["department"], df["admissions"], color=PRIMARY_BLUE)
for bar in bars:
    value = int(bar.get_width())
    ax.text(value + 25, bar.get_y() + bar.get_height() / 2, f"{value:,}")
ax.set_xlim(0, 1400)
```

`barh` удобнее для длинных названий; сортировка и подписи значений
делают график самодостаточным.

#heading(level: 2)[5.15.8 Что дальше]

Следующий график — *5.16 forest*: оценки эффектов и доверительные
интервалы для многих подгрупп. У него будет свой генератор и свой
`data/16_dataset.csv`.

#heading(level: 2)[Источники]

- Wilke C. O. _Fundamentals of Data Visualization_. 2019. —
  #link("https://clauswilke.com/dataviz/")[clauswilke.com/dataviz]
- Tufte E. R. _The Visual Display of Quantitative Information_. 1983. —
  #link("https://www.edwardtufte.com/tufte/books_vdqi")[edwardtufte.com]
- Matplotlib: `barh` —
  #link("https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html")[matplotlib.org]