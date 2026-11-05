// Раздел 5.11. Boxplot: сравнение распределений по группам.
// Сборка: typst compile --root . 05_charts/11_box/box.typ build/05_11_box.pdf

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

#heading(level: 1)[5.11 Boxplot: сравнение распределений по группам]

Boxplot — компактная сводка распределения: медиана, межквартильный
размах (IQR), усы и выбросы. Он хорош для сравнения 2–5 групп, но
*сам по себе скрывает форму* распределения и размер выборки.

Поэтому в этом разделе показаны четыре варианта:

+ плохой boxplot;
+ boxplot + отдельные точки;
+ violin + box + точки;
+ boxplot, совмещённый с гистограммой.

#heading(level: 2)[5.11.1 Сфера применения]

Boxplot отвечает на вопрос: *как различаются медианы и разброс
между группами?*

Где это пригодится:

- сравнение биомаркера по 2–5 группам (активность, тяжесть, центр);
- проверка сдвига и разброса до формального теста;
- поиск выбросов;
- компактная сводка в таблице рисунков;
- сравнение до/после (но для парных данных — 5.18).

Когда boxplot *не* достаточен:

- нужно увидеть форму/модальность — violin или histogram;
- групп много — small multiples;
- выборка маленькая — точки важнее коробки;
- нужны точные квантили — ECDF (5.10);
- данные цензурированы — Kaplan–Meier (5.27).

#heading(level: 2)[5.11.2 Данные]

Сценарий: 450 взрослых, три уровня физической активности —
низкая, умеренная, высокая. Показатель — BMI (кг/м²), по 150 человек
в группе.

#table(
  columns: (1.4fr, 2.8fr, 1.2fr),
  table.header([*Колонка*], [*Смысл*], [*Единица*]),
  [`patient_id`], [идентификатор пациента], [—],
  [`activity`], [уровень активности], [—],
  [`bmi_kg_m2`], [индекс массы тела], [кг/м²],
)

Медианы: низкая — 29,4; умеренная — 27,8; высокая — 24,4 кг/м².
Есть правый хвост и отдельные выбросы.

Генератор: `05_charts/11_box/scripts/make_data.py` →
`data/11_dataset.csv`.

#heading(level: 2)[5.11.3 Плохой график]

#block(breakable: false)[
  #align(center)[
    #image("../../images/05_11_bad_box.png", width: 84%)
  ]
  #v(2pt)
  #align(center)[
    #text(size: 8.5pt, style: "italic")[
      Рисунок 5.11.1. Плохой boxplot: обрезанная ось 22–32, радужные
      ящики, нет точек, тяжёлая сетка.
    ]
  ]
]

Код: `05_charts/11_box/scripts/bad_plot.py`.

Что не так:

+ *Ось Y обрезана до 22–32.* Выбросы и хвосты скрыты; высокая
  группа выглядит «обрезанной».
+ *Радужные ящики, красные медианы и выбросы.* Декор вместо
  данных; CVD-небезопасно.
+ *Нет отдельных точек.* Не видно формы, размера групп и того,
  что за пределами усов.
+ *Тяжёлая сетка, полная рамка, толстые линии.*
+ *Заголовок «BMI и активность».* Не сообщает направление
  и величину различий.
+ *Нет единиц и _n_.*

#heading(level: 2)[5.11.4 Boxplot + точки]

#block(breakable: false)[
  #align(center)[
    #image("../../images/05_11_good_box_points.png", width: 85mm)
  ]
  #v(2pt)
  #align(center)[
    #text(size: 8.5pt, style: "italic")[
      Рисунок 5.11.2. Правильный boxplot с точками: полный диапазон
      15–45, jitter, n = 150, единицы.
    ]
  ]
]

Код: `05_charts/11_box/scripts/good_box_points.py`.

Что изменилось:

+ *Полный диапазон 15–45 кг/м².* Видны хвосты и выбросы.
+ *Белые ящики с синим контуром, тёмная медиана.* Один цвет,
  без радуги.
+ *Все 450 точек с jitter.* Видна плотность, форма и размер
  групп; выбросы не прячутся.
+ *Единицы, _n_ = 150, заголовок-вывод.*
+ *Лёгкая сетка только по Y, 85 мм.*

Точки не заменяют boxplot: они показывают, что внутри коробки,
а коробка даёт сводку. Вместе они честнее, чем boxplot отдельно.

#heading(level: 2)[5.11.5 Violin + box + точки]

#block(breakable: false)[
  #align(center)[
    #image("../../images/05_11_good_violin_box.png", width: 85mm)
  ]
  #v(2pt)
  #align(center)[
    #text(size: 8.5pt, style: "italic")[
      Рисунок 5.11.3. Violin + box + точки: форма распределения,
      медиана и исходные наблюдения.
    ]
  ]
]

Код: `05_charts/11_box/scripts/good_violin_box.py`.

Что показывает:

+ *Violin* — оценку плотности: где значения встречаются чаще.
+ *Box* — медиану, IQR и усы.
+ *Точки* — исходные наблюдения.

Это «raincloud»-подход: форма, сводка и данные одновременно. Он хорош
для 3 групп и умеренных выборок. Но violin — это KDE: она может
«продлить» хвост за пределы реальных данных и создать ложную
плавность. При малых _n_ доверяйте точкам больше, чем контуру.

#heading(level: 2)[5.11.6 Boxplot + гистограмма]

#block(breakable: false)[
  #align(center)[
    #image("../../images/05_11_good_box_hist.png", width: 85mm)
  ]
  #v(2pt)
  #align(center)[
    #text(size: 8.5pt, style: "italic")[
      Рисунок 5.11.4. Совмещённый график: гистограмма сверху,
      горизонтальный boxplot снизу, общая ось BMI.
    ]
  ]
]

Код: `05_charts/11_box/scripts/good_box_hist.py`.

Что показывает:

+ *Гистограмма сверху* — форму распределения (бины по 2 кг/м²).
+ *Boxplot снизу* — медиану, IQR, усы и выбросы.
+ *Общая ось X* — гистограмма и коробка выровнены.

Этот вариант полезен, когда нужно показать и форму, и сводку для одной
переменной или одной группы. Медиана 29,4 кг/м² подписана прямо над
коробкой.

#heading(level: 2)[5.11.7 Было и стало]

#table(
  columns: (1.5fr, 2fr, 2fr),
  table.header([*Что было*], [*Почему плохо*], [*Что сделано*]),
  [ось Y 22–32], [выбросы и хвосты скрыты], [15–45],
  [радуга, красные медианы], [декор, CVD], [один синий цвет],
  [нет точек], [не видна форма], [jitter-точки],
  [толстые линии], [шум], [0,8–1,2 pt],
  [сетка по X и Y], [шум], [сетка только по Y],
  [полная рамка], [визуальный шум], [только левая и нижняя оси],
  [«BMI и активность»], [нет сообщения], [заголовок-вывод],
  [нет единиц и n], [невозможно прочитать], [единицы, n = 150],
  [только коробка], [форма скрыта], [+ violin / histogram],
)

#heading(level: 2)[5.11.8 Чек-лист boxplot]

- ☐ Ось Y не обрезает усы и выбросы.
- ☐ Указаны единицы и _n_ (по группам).
- ☐ Медиана и IQR читаются; усы объяснены.
- ☐ Точки показаны, если _n_ небольшое или важна форма.
- ☐ Для формы добавлен violin или histogram.
- ☐ Цвет не дублирует группы без смысла.
- ☐ Нет 3D, теней и радуги.
- ☐ Сетка не конкурирует с данными.
- ☐ Для многих групп — small multiples.
- ☐ Рисунок проверен в конечном размере.

#heading(level: 2)[5.11.9 Как воспроизвести]

```bash
uv sync
uv run python 05_charts/11_box/scripts/make_data.py
uv run python 05_charts/11_box/scripts/bad_plot.py
uv run python 05_charts/11_box/scripts/good_box_points.py
uv run python 05_charts/11_box/scripts/good_violin_box.py
uv run python 05_charts/11_box/scripts/good_box_hist.py
```

Ключевые фрагменты:

```python
# boxplot + точки
ax.boxplot(data, positions=[1, 2, 3], widths=0.5, patch_artist=True,
           showfliers=False, boxprops={"facecolor": "white"})
for position, values in zip([1, 2, 3], data, strict=True):
    ax.scatter(position + rng.normal(0, 0.06, len(values)), values,
               s=5, alpha=0.18, linewidths=0)

# violin + box
ax.violinplot(data, positions=[1, 2, 3], widths=0.8, showextrema=False)

# histogram + horizontal box
fig, (ax_hist, ax_box) = plt.subplots(2, 1, sharex=True,
                                      gridspec_kw={"height_ratios": [3, 1]})
ax_box.boxplot([values], orientation="horizontal", positions=[0.5])
```

#heading(level: 2)[5.11.10 Что дальше]

Следующий график — *5.12 violin*: отдельный разбор скрипичной
диаграммы, её преимуществ и ловушек. У него будет свой генератор
и свой `data/12_dataset.csv`.

#heading(level: 2)[Источники]

- Wilke C. O. _Fundamentals of Data Visualization_. 2019. —
  #link("https://clauswilke.com/dataviz/")[clauswilke.com/dataviz]
- Weissgerber T. L. et al. Beyond Bar and Line Graphs #text("//") _PLoS Biology_.
  2015. — #link("https://doi.org/10.1371/journal.pbio.1002128")[doi:10.1371/journal.pbio.1002128]
- Matplotlib: `boxplot` —
  #link("https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html")[matplotlib.org]
- Matplotlib: `violinplot` —
  #link("https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.violinplot.html")[matplotlib.org]