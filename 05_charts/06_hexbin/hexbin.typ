// Раздел 5.06. Hexbin: плотность тысяч точек.
// Сборка: typst compile --root . 05_charts/06_hexbin/hexbin.typ build/05_06_hexbin.pdf

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

#heading(level: 1)[5.06 Hexbin: плотность тысяч точек]

Hexbin — это scatter, у которого точки агрегированы в шестиугольные бины,
а цвет показывает число наблюдений в бине. Он нужен там, где обычный
scatter превращается в сплошное пятно: тысячи точек, плотное ядро,
длинные хвосты.

Важно помнить: hexbin показывает *плотность*, а не отдельного пациента.
Цвет — это число наблюдений в бине, а не значение признака.

#heading(level: 2)[5.06.1 Сфера применения]

Hexbin отвечает на вопрос: *где наблюдений много, а где мало, и какова
форма облака при больших n?*

Типичные случаи:

- 5 000–1 000 000 точек в scatter;
- плотность биомедицинских показателей (HbA1c и глюкоза, BMI и АД);
- кластеры и гетерогенность в больших когортах;
- проверка формы распределения перед регрессией;
- визуализация больших выгрузок без потери плотности.

Когда hexbin *не* нужен:

- точек мало (до нескольких сотен) — scatter честнее;
- нужно прочитать отдельное наблюдение;
- одна из переменных категориальная;
- важна точная форма хвоста, а бинование её огрубляет;
- нужна связь, а не плотность — scatter или contour.

#heading(level: 2)[5.06.2 Данные]

Сценарий: 8 000 пациентов, HbA1c (%) и глюкоза натощак (ммоль/л).
Связь сильная, но с разбросом; при 8 000 точек обычный scatter
превращается в пятно.

#table(
  columns: (1.4fr, 2.8fr, 1.2fr),
  table.header([*Колонка*], [*Смысл*], [*Единица*]),
  [`patient_id`], [идентификатор пациента], [—],
  [`hba1c_pct`], [гликированный гемоглобин], [%],
  [`glucose_mmol_l`], [глюкоза натощак], [ммоль/л],
)

Средний HbA1c — 6,3 ± 0,9 %; глюкоза — 7,5 ± 1,8 ммоль/л;
корреляция Пирсона _r_ = 0,83.

Генератор: `05_charts/06_hexbin/scripts/make_data.py` →
`data/06_dataset.csv`.

#heading(level: 2)[5.06.3 Плохой график]

#block(breakable: false)[
  #align(center)[
    #image("../../images/05_06_bad_hexbin.png", width: 84%)
  ]
  #v(2pt)
  #align(center)[
    #text(size: 8.5pt, style: "italic")[
      Рисунок 5.6.1. Плохой пример: 8 000 непрозрачных точек, overplotting,
      обрезанные оси, тяжёлая сетка.
    ]
  ]
]

Код: `05_charts/06_hexbin/scripts/bad_plot.py`.

Что с ним не так:

+ *8 000 непрозрачных точек.* Вместо плотности — чёрное пятно;
  в центре точки сливаются, хвосты теряются.
+ *Обрезанные оси (5–9 и 4–12).* Часть наблюдений и хвосты
  распределения скрыты.
+ *Тяжёлая сетка по обеим осям и полная рамка.* Сетка конкурирует
  с плотным облаком.
+ *Заголовок «Связь HbA1c и глюкозы».* Не сообщает, что важно
  именно распределение плотности.
+ *Нет единиц, n и r.* Непонятно, сколько наблюдений и какова сила
  связи.
+ *Чёрный цвет не кодирует плотность.* Читатель не видит, где
  наблюдений больше.

#heading(level: 2)[5.06.4 Правильный график]

#block(breakable: false)[
  #align(center)[
    #image("../../images/05_06_good_hexbin.png", width: 85mm)
  ]
  #v(2pt)
  #align(center)[
    #text(size: 8.5pt, style: "italic")[
      Рисунок 5.6.2. Правильный hexbin: плотность в логарифмической шкале,
      colorbar 1–100, полный диапазон, n и r.
    ]
  ]
]

Код: `05_charts/06_hexbin/scripts/good_plot.py`.

Что улучшено:

+ *Hexbin вместо scatter.* Цвет кодирует число пациентов
  в шестиугольнике; плотность видна.
+ *Логарифмическая шкала плотности.* Видны и плотное ядро,
  и разреженные хвосты; линейная шкала «съела» бы хвосты.
+ *`mincnt=1`.* Пустые бины остаются белыми, а не окрашиваются
  в цвет «нуля».
+ *Полный диапазон осей.* 4,5–11 % и 2–16 ммоль/л; данные
  не обрезаны.
+ *Подписанный colorbar.* «Пациенты (лог. шкала)», деления
  1/3/10/30/100 — цвет читается как число.
+ *Единицы, n и r.* «HbA1c, %», «Глюкоза, ммоль/л»,
  _n_ = 8000, _r_ = 0,83.
+ *`cividis`.* Последовательная шкала, читаемая при дальтонизме.
+ *85 мм.* Рисунок спроектирован в конечном размере.

Hexbin не заменяет scatter для отдельных наблюдений: он показывает
плотность. Если нужен конкретный пациент или выброс, hexbin его
не подпишет.

#heading(level: 2)[5.06.5 Сопоставление]

#table(
  columns: (1.5fr, 2fr, 2fr),
  table.header([*Что было*], [*Почему плохо*], [*Что сделано*]),
  [8 000 точек scatter], [overplotting], [hexbin],
  [оси 5–9 / 4–12], [хвосты обрезаны], [4,5–11 / 2–16],
  [чёрный цвет], [не кодирует плотность], [цвет = число пациентов],
  [линейная шкала], [хвосты не видны], [лог. шкала],
  [пустые бины окрашены], [ложные «нули»], [`mincnt=1`],
  [сетка по X и Y], [шум], [без сетки],
  [полная рамка], [визуальный шум], [только левая и нижняя оси],
  [«Связь HbA1c и глюкозы»], [нет сообщения], [заголовок о плотности],
  [нет единиц и _n_], [невозможно прочитать], [единицы, _n_, _r_],
  [нет colorbar], [цвет не читается], [colorbar с делениями],
)

#heading(level: 2)[5.06.6 Чек-лист hexbin]

- ☐ Точек действительно много; scatter уже не читается.
- ☐ Понятно, что цвет кодирует число наблюдений, а не значение.
- ☐ Указаны единицы и _n_.
- ☐ Оси не обрезают данные.
- ☐ `mincnt=1`, чтобы пустые бины не выглядели «нулём».
- ☐ Шкала плотности (линейная/логарифмическая) подписана.
- ☐ Colorbar с делениями и единицами.
- ☐ `gridsize` не слишком крупный и не слишком мелкий.
- ☐ Для точных значений используется scatter/contour.
- ☐ Рисунок проверен в конечном размере 85 мм.

#heading(level: 2)[5.06.7 Как воспроизвести]

```bash
uv sync
uv run python 05_charts/06_hexbin/scripts/make_data.py
uv run python 05_charts/06_hexbin/scripts/bad_plot.py
uv run python 05_charts/06_hexbin/scripts/good_plot.py
```

Ключевой фрагмент:

```python
hexbin = ax.hexbin(
    x, y,
    gridsize=32,
    cmap="cividis",
    mincnt=1,
    bins="log",
    linewidths=0,
)
cbar = fig.colorbar(hexbin, ax=ax, fraction=0.05, pad=0.02, shrink=0.85)
cbar.set_label("Пациенты (лог. шкала)")
```

`bins="log"` включает логарифмическую нормализацию цвета; `mincnt=1`
оставляет пустые бины белыми. Если нужно среднее значение в бине,
используйте `reduce_C_function=np.mean` и подпишите, что кодирует цвет.

#heading(level: 2)[5.06.8 Что дальше]

Следующий график — *5.07 contour*: изолинии плотности или поверхности
отклика. У него будет свой генератор и свой `data/07_dataset.csv`.

#heading(level: 2)[Источники]

- Wilke C. O. _Fundamentals of Data Visualization_. 2019. —
  #link("https://clauswilke.com/dataviz/")[clauswilke.com/dataviz]
- Matplotlib: `hexbin` —
  #link("https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hexbin.html")[matplotlib.org]
- Tufte E. R. _The Visual Display of Quantitative Information_. 1983. —
  #link("https://www.edwardtufte.com/tufte/books_vdqi")[edwardtufte.com]
- Cairo A. _The Truthful Art_. New Riders, 2016. —
  #link("https://www.thefunctionalart.com/")[thefunctionalart.com]
