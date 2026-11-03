// Раздел 5.10. ECDF: функция распределения.
// Сборка: typst compile --root . 05_charts/10_ecdf/ecdf.typ build/05_10_ecdf.pdf

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

#heading(level: 1)[5.10 ECDF: функция распределения]

ECDF (empirical cumulative distribution function) показывает, какая
доля наблюдений не превышает каждое значение X. В отличие от
гистограммы, здесь нет бинов: кривая строится по всем точкам и позволяет
точно прочитать медиану, квартили и любой перцентиль.

ECDF — это ступенчатая функция. Каждый скачок — одно или несколько
наблюдений; высота ступени — накопленная доля.

#heading(level: 2)[5.10.1 Сфера применения]

ECDF отвечает на вопрос: *какая доля пациентов имеет значение ≤ x
и где проходят квантили?*

Типичные случаи:

- распределение длительности госпитализации, времени до выписки;
- сравнение двух групп по всей кривой, а не только по средним;
- чтение медианы, IQR и перцентилей;
- проверка сдвига распределения;
- малые и средние выборки, где гистограмма капризна.

Когда ECDF *не* подходит:

- время до события с цензурированием — Kaplan–Meier (5.27);
- нужно показать плотность/форму — histogram/KDE;
- групп слишком много — кривые перекрываются (нужны small multiples);
- нужна одна сводка, а не распределение — dot/box.

#heading(level: 2)[5.10.2 Данные]

Сценарий: 1 200 госпитализаций, 600 плановых и 600 экстренных.
Длительность — дни; распределение скошено вправо.

#table(
  columns: (1.4fr, 2.8fr, 1.2fr),
  table.header([*Колонка*], [*Смысл*], [*Единица*]),
  [`patient_id`], [идентификатор пациента], [—],
  [`admission_type`], [плановое/экстренное], [—],
  [`los_days`], [длительность госпитализации], [дни],
)

Медиана: плановые — 6 дней, экстренные — 8,5 дня. Средние: 6,2 и 9,4.
Правый хвост — до 20–25 дней.

Генератор: `05_charts/10_ecdf/scripts/make_data.py` →
`data/10_dataset.csv`.

#heading(level: 2)[5.10.3 Плохой график]

#block(breakable: false)[
  #align(center)[
    #image("../../images/05_10_bad_ecdf.png", width: 84%)
  ]
  #v(2pt)
  #align(center)[
    #text(size: 8.5pt, style: "italic")[
      Рисунок 5.10.1. Плохая ECDF: обрезанная ось 0–12, красно-зелёные
      ступени, легенда, нет медиан и n.
    ]
  ]
]

Код: `05_charts/10_ecdf/scripts/bad_plot.py`.

Что с ним не так:

+ *Ось X обрезана до 12 дней.* Правый хвост и половина кривой
  скрыты; экстренные госпитализации выглядят короче, чем есть.
+ *Красно-зелёная пара.* Неразличима при протанопии/дейтеранопии.
+ *Легенда.* Заставляет переводить взгляд; для двух групп лучше
  прямые подписи.
+ *Толстые ступени, тяжёлая сетка, полная рамка.*
+ *Нет медиан, квартилей, единиц и n.*
+ *Заголовок «Длительность госпитализации».* Не сообщает,
  что экстренные длиннее.

#heading(level: 2)[5.10.4 Правильный график]

#block(breakable: false)[
  #align(center)[
    #image("../../images/05_10_good_ecdf.png", width: 85mm)
  ]
  #v(2pt)
  #align(center)[
    #text(size: 8.5pt, style: "italic")[
      Рисунок 5.10.2. Правильная ECDF: полный диапазон 0–25, синий
      и вермиллион, медианы, прямые подписи, n.
    ]
  ]
]

Код: `05_charts/10_ecdf/scripts/good_plot.py`.

Что улучшено:

+ *Полный диапазон 0–25 дней.* Обе кривые видны целиком,
  включая хвост.
+ *Синий и вермиллион.* Различимы при CVD; без легенды,
  с прямыми подписями.
+ *Медианы отмечены пунктиром.* 6 и 8,5 дня; разница видна
  на уровне 50 %.
+ *Ось Y в процентах.* «Доля пациентов, %» читается
  без пересчёта.
+ *n = 600 + 600.* Понятно, сколько наблюдений в группах.
+ *Заголовок-вывод.* «Экстренные: медиана 8,5 vs 6 дней».
+ *Лёгкая сетка только по Y, без верхней и правой рамок.*
+ *85 мм.* Рисунок спроектирован в конечном размере.

ECDF читается так: найдите на оси X интересующий срок, поднимитесь
до кривой и посмотрите долю на оси Y. Медиана — точка, где кривая
пересекает 50 %.

#heading(level: 2)[5.10.5 Сопоставление]

#table(
  columns: (1.5fr, 2fr, 2fr),
  table.header([*Что было*], [*Почему плохо*], [*Что сделано*]),
  [ось X 0–12], [хвост обрезан], [0–25],
  [красный/зелёный], [CVD], [синий/вермиллион],
  [легенда], [лишний поиск], [прямые подписи],
  [толстые ступени], [шум], [1,7 pt],
  [нет медиан], [не читаются квантили], [пунктирные медианы],
  [нет единиц и n], [невозможно прочитать], [«дни», n = 600 + 600],
  [«Длительность…»], [нет сообщения], [заголовок с медианами],
  [сетка по X и Y], [шум], [сетка только по Y],
)

#heading(level: 2)[5.10.6 Чек-лист ECDF]

- ☐ Ось X не обрезает хвост.
- ☐ Указаны единицы и _n_.
- ☐ Подписаны группы (прямо или легендой).
- ☐ Медиана/квартили отмечены, если они важны.
- ☐ Ось Y — доля или процент, ясно что именно.
- ☐ Нет лишних цветов и толстых ступеней.
- ☐ Для цензурированных данных выбран Kaplan–Meier.
- ☐ Сравнение групп не сводится к средним.
- ☐ Кривые не перекрываются из-за числа групп.
- ☐ Рисунок проверен в конечном размере 85 мм.

#heading(level: 2)[5.10.7 Как воспроизвести]

```bash
uv sync
uv run python 05_charts/10_ecdf/scripts/make_data.py
uv run python 05_charts/10_ecdf/scripts/bad_plot.py
uv run python 05_charts/10_ecdf/scripts/good_plot.py
```

Ключевой фрагмент:

```python
def ecdf(values):
    xs = np.sort(values)
    ys = np.arange(1, len(xs) + 1) / len(xs) * 100
    return xs, ys

xs, ys = ecdf(values)
ax.step(xs, ys, where="post", color=PRIMARY_BLUE, linewidth=1.7)
ax.axvline(np.median(values), color=PRIMARY_BLUE, linestyle=":", linewidth=0.8)
```

`where="post"` важен: ступень держится до следующего значения.
Для сравнения групп используйте одинаковые оси и прямые подписи.

#heading(level: 2)[5.10.8 Что дальше]

Следующий график — *5.11 box plot*: сравнение распределений
по группам. У него будет свой генератор и свой `data/11_dataset.csv`.

#heading(level: 2)[Источники]

- Wilke C. O. _Fundamentals of Data Visualization_. 2019. —
  #link("https://clauswilke.com/dataviz/")[clauswilke.com/dataviz]
- Matplotlib: `step` —
  #link("https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.step.html")[matplotlib.org]
- Weissgerber T. L. et al. Beyond Bar and Line Graphs #text("//") _PLoS Biology_.
  2015. — #link("https://doi.org/10.1371/journal.pbio.1002128")[doi:10.1371/journal.pbio.1002128]
- Tufte E. R. _The Visual Display of Quantitative Information_. 1983. —
  #link("https://www.edwardtufte.com/tufte/books_vdqi")[edwardtufte.com]
