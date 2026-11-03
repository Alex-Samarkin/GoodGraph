// Раздел 5.09. Гистограмма: распределение одной величины.
// Сборка: typst compile --root . 05_charts/09_histogram/histogram.typ build/05_09_histogram.pdf

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

#heading(level: 1)[5.09 Гистограмма: распределение одной величины]

Гистограмма показывает, как распределена одна непрерывная величина:
центр, разброс, форму, скошенность и выбросы. Она отвечает на вопрос
«как устроена выборка», а не «как связаны две переменные».

Главная ловушка — *выбор ширины бина*. Слишком широкие бины скрывают
форму, слишком узкие — превращают шум в «структуру». Гистограмма — это
семейство изображений, а не одно «истинное».

#heading(level: 2)[5.09.1 Сфера применения]

Гистограмма отвечает на вопрос: *как распределена величина и где
её центр, разброс, хвосты?*

Типичные случаи:

- распределение биомаркера (витамин D, CRP, глюкоза);
- проверка нормальности/скошенности перед тестом;
- поиск выбросов и многомодальности;
- описание выборки до сравнения групп;
- контроль качества измерений.

Когда гистограмма *не* подходит:

- наблюдений мало (десятки) — лучше точки/strip;
- нужно точное значение или квантиль — ECDF (5.10);
- несколько групп — box/violin/small multiples;
- важна форма хвоста, а бины её огрубляют;
- ось X обрезана и хвост скрыт.

#heading(level: 2)[5.09.2 Данные]

Сценарий: 1 200 взрослых, уровень 25(OH)D (нг/мл). Распределение
сдвинуто влево и имеет правый хвост.

#table(
  columns: (1.4fr, 2.8fr, 1.2fr),
  table.header([*Колонка*], [*Смысл*], [*Единица*]),
  [`patient_id`], [идентификатор пациента], [—],
  [`vitamin_d_ng_ml`], [25(OH)D], [нг/мл],
)

Медиана — 23,4 нг/мл; IQR — 16,5–32,5; дефицит (< 20 нг/мл) —
у 38 %; диапазон 3–70 нг/мл.

Генератор: `05_charts/09_histogram/scripts/make_data.py` →
`data/09_dataset.csv`.

#heading(level: 2)[5.09.3 Плохой график]

#block(breakable: false)[
  #align(center)[
    #image("../../images/05_09_bad_histogram.png", width: 84%)
  ]
  #v(2pt)
  #align(center)[
    #text(size: 8.5pt, style: "italic")[
      Рисунок 5.9.1. Плохая гистограмма: пять бинов, обрезанная ось 10–40,
      радужные столбцы, тени, нет единиц и порога.
    ]
  ]
]

Код: `05_charts/09_histogram/scripts/bad_plot.py`.

Что с ним не так:

+ *Пять бинов.* Форма распределения и правый хвост исчезли;
  осталось три столбца.
+ *Обрезанная ось X (10–40).* Низкие и высокие значения
  не видны.
+ *Радужные столбцы, чёрные края и тени.* Декор, который
  не кодирует данные.
+ *Тяжёлая сетка по обеим осям и полная рамка.*
+ *Заголовок «Витамин D».* Не сообщает, что важно:
  дефицит, медиана, форма.
+ *Нет единиц, n, медианы и порога 20.* Гистограмма
  не читается как клинический результат.

#heading(level: 2)[5.09.4 Правильный график]

#block(breakable: false)[
  #align(center)[
    #image("../../images/05_09_good_histogram.png", width: 85mm)
  ]
  #v(2pt)
  #align(center)[
    #text(size: 8.5pt, style: "italic")[
      Рисунок 5.9.2. Правильная гистограмма: бины по 2 нг/мл, полный
      диапазон, порог 20, медиана, n и доля дефицита.
    ]
  ]
]

Код: `05_charts/09_histogram/scripts/good_plot.py`.

Что улучшено:

+ *Ширина бина 2 нг/мл.* Видна форма, правый хвост и мода
  около 18–24 нг/мл.
+ *Полный диапазон 0–70 нг/мл.* Ничего не обрезано.
+ *Один цвет, белые края, без теней.*
+ *Порог дефицита 20 нг/мл* выделен пунктиром.
+ *Медиана 23,4 нг/мл* отмечена и подписана.
+ *n = 1200 и доля дефицита 38 %* в заголовке.
+ *Единицы, лёгкая сетка только по Y, без верхней и правой рамок.*
+ *85 мм.* Рисунок спроектирован в конечном размере.

Проверьте устойчивость: постройте гистограмму с шириной 1, 2 и 5 нг/мл.
Если вывод меняется, он не должен держаться на одном выборе бинов.

#heading(level: 2)[5.09.5 Сопоставление]

#table(
  columns: (1.5fr, 2fr, 2fr),
  table.header([*Что было*], [*Почему плохо*], [*Что сделано*]),
  [5 бинов], [форма и хвост скрыты], [бины по 2 нг/мл],
  [ось X 10–40], [хвосты обрезаны], [0–70],
  [радуга, тени], [декор], [один цвет],
  [сетка по X и Y], [шум], [сетка только по Y],
  [полная рамка], [визуальный шум], [только левая и нижняя оси],
  [«Витамин D»], [нет сообщения], [заголовок о дефиците],
  [нет единиц и n], [невозможно прочитать], [единицы, n],
  [нет порога и медианы], [клинический контекст потерян], [порог 20, медиана],
  [counts без подписи], [непонятно, что такое Y], [«Пациенты»],
)

#heading(level: 2)[5.09.6 Чек-лист гистограммы]

- ☐ Указана единица измерения.
- ☐ Ось X не обрезает хвосты.
- ☐ Ширина бина осмысленна; проверена устойчивость.
- ☐ Указаны _n_ и, если важно, медиана/IQR.
- ☐ Есть клинический порог, если он существенен.
- ☐ Один цвет, без 3D и теней.
- ☐ Сетка не конкурирует с данными.
- ☐ Понятно, что по Y: пациенты или плотность.
- ☐ Для малых _n_ рассмотрены точки/ECDF.
- ☐ Рисунок проверен в конечном размере 85 мм.

#heading(level: 2)[5.09.7 Как воспроизвести]

```bash
uv sync
uv run python 05_charts/09_histogram/scripts/make_data.py
uv run python 05_charts/09_histogram/scripts/bad_plot.py
uv run python 05_charts/09_histogram/scripts/good_plot.py
```

Ключевой фрагмент:

```python
bins = np.arange(0, 72, 2)
counts, _, _ = ax.hist(
    values, bins=bins,
    color=PRIMARY_BLUE, alpha=0.8,
    edgecolor="white", linewidth=0.4,
)
ax.axvline(20, color=ACCENT_VERMILLION, linestyle="--", linewidth=0.9)
ax.axvline(np.median(values), color="#333333", linestyle=":", linewidth=0.9)
```

`bins` можно задать числом или массивом границ. Массив границ
предпочтительнее: он фиксирует ширину и облегчает сравнение
нескольких выборок.

#heading(level: 2)[5.09.8 Что дальше]

Следующий график — *5.10 ECDF*: эмпирическая функция распределения,
точное чтение квантилей. У него будет свой генератор и свой
`data/10_dataset.csv`.

#heading(level: 2)[Источники]

- Wilke C. O. _Fundamentals of Data Visualization_. 2019. —
  #link("https://clauswilke.com/dataviz/")[clauswilke.com/dataviz]
- Matplotlib: `hist` —
  #link("https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html")[matplotlib.org]
- Tufte E. R. _The Visual Display of Quantitative Information_. 1983. —
  #link("https://www.edwardtufte.com/tufte/books_vdqi")[edwardtufte.com]
- Weissgerber T. L. et al. Beyond Bar and Line Graphs #text("//") _PLoS Biology_.
  2015. — #link("https://doi.org/10.1371/journal.pbio.1002128")[doi:10.1371/journal.pbio.1002128]
