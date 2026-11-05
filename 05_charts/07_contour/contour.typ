// Раздел 5.07. Contour: изолинии плотности.
// Сборка: typst compile --root . 05_charts/07_contour/contour.typ build/05_07_contour.pdf

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

#heading(level: 1)[5.07 Contour: изолинии плотности]

Contour plot рисует линии равного значения: плотности, вероятности,
поверхности отклика. В отличие от hexbin, контурная карта выглядит
гладкой и показывает форму облака, но поэтому она может
«придумать» структуру, которой нет в данных.

На практике: *сначала плотность, потом линии.* Контурные линии — это
изолинии оценки плотности; без colorbar и подписи уровней они ничего
не значат.

#heading(level: 2)[5.07.1 Сфера применения]

Contour отвечает на вопрос: *где плотность (или значение поверхности)
одинакова и какова форма двумерного распределения?*

Где это пригодится:

- 2D-плотность больших выборок (возраст и САД, BMI и глюкоза);
- поверхность отклика (доза × время → эффект);
- доверительные области и эллипсы;
- топография/визуализация пространственных полей;
- сглаженная альтернатива hexbin.

Когда contour *не* нужен:

- точек мало — контурная оценка неустойчива;
- нужно прочитать отдельное наблюдение;
- важна локальная структура, а не гладкая форма — hexbin/scatter;
- уровни выбраны произвольно и не подписаны;
- сглаживание скрывает реальные разрывы.

#heading(level: 2)[5.07.2 Данные]

Сценарий: 10 000 взрослых, возраст (лет) и систолическое АД
(мм рт. ст.). САД растёт с возрастом, разброс тоже растёт.

#table(
  columns: (1.4fr, 2.8fr, 1.2fr),
  table.header([*Колонка*], [*Смысл*], [*Единица*]),
  [`patient_id`], [идентификатор пациента], [—],
  [`age_years`], [возраст], [лет],
  [`sbp_mm_hg`], [систолическое АД], [мм рт. ст.],
)

Средний возраст — 51,8 ± 14,7 лет; САД — 125,0 ± 17,3 мм рт. ст.;
корреляция _r_ = 0,49. Порог 140 мм рт. ст. отмечен на графике.

Генератор: `05_charts/07_contour/scripts/make_data.py` →
`data/07_dataset.csv`.

#heading(level: 2)[5.07.3 Плохой график]

#block(breakable: false)[
  #align(center)[
    #image("../../images/05_07_bad_contour.png", width: 84%)
  ]
  #v(2pt)
  #align(center)[
    #text(size: 8.5pt, style: "italic")[
      Рисунок 5.7.1. Плохой contour: радужная палитра, 20 уровней,
      налезающие подписи, обрезанные оси.
    ]
  ]
]

Код: `05_charts/07_contour/scripts/bad_plot.py`.

Что не так:

+ *Палитра `jet` и 20 уровней.* Ложные границы, «радуга»,
  неразличимая при дальтонизме.
+ *Подписи уровней налезают друг на друга.* Читать карту
  невозможно.
+ *Обрезанные оси (40–70 и 110–170).* Хвосты распределения
  скрыты.
+ *Тяжёлая сетка по обеим осям и полная рамка.* Шум поверх
  и без того шумной карты.
+ *Заголовок «Возраст и САД».* Не сообщает, что показана
  плотность и где порог.
+ *Нет единиц, _n_, colorbar и порога 140.* Цвет и уровни
  не читаются.
+ *Слишком мелкие бины.* Карта выглядит «рябой»: шум
  гистограммы принимается за структуру.

#heading(level: 2)[5.07.4 Правильный график]

#block(breakable: false)[
  #align(center)[
    #image("../../images/05_07_good_contour.png", width: 85mm)
  ]
  #v(2pt)
  #align(center)[
    #text(size: 8.5pt, style: "italic")[
      Рисунок 5.7.2. Правильный contour: сглаженная плотность, cividis,
      colorbar 1–20, порог 140, n и r.
    ]
  ]
]

Код: `05_charts/07_contour/scripts/good_plot.py`.

Что изменилось:

+ *Сглаженная 2D-плотность.* `gaussian_filter` убирает шум бинов,
  не стирая облако; структура читается.
+ *`cividis` и 9 уровней.* Последовательная доступная шкала,
  без ложных границ.
+ *Полный диапазон осей.* 20–80 лет и 90–200 мм рт. ст.
+ *Подписанный colorbar.* «Пациенты (лог. шкала)», деления
  1/3/10/20.
+ *Порог 140 мм рт. ст.* Выделен пунктиром и подписью.
+ *Единицы, _n_ и _r_.* «Возраст, лет», «САД, мм рт. ст.»,
  _n_ = 10000, _r_ = 0,49.
+ *Без тяжёлой сетки.* Контурные линии — единственная
  вспомогательная графика.
+ *85 мм.* Рисунок спроектирован в конечном размере.

Контурная карта — это *оценка* плотности. Сглаживание и число
уровней — параметры модели, а не «истина». Если структура важна,
сравните contour с hexbin или scatter.

#heading(level: 2)[5.07.5 Было и стало]

#table(
  columns: (1.5fr, 2fr, 2fr),
  table.header([*Что было*], [*Почему плохо*], [*Что сделано*]),
  [`jet`, 20 уровней], [ложные границы, CVD], [`cividis`, 9 уровней],
  [подписи всех уровней], [налезают], [без подписей, colorbar],
  [оси 40–70 / 110–170], [хвосты обрезаны], [20–80 / 90–200],
  [мелкие бины], [шум как структура], [сглаживание],
  [сетка по X и Y], [шум], [без сетки],
  [полная рамка], [визуальный шум], [только левая и нижняя оси],
  [«Возраст и САД»], [нет сообщения], [заголовок о плотности],
  [нет единиц и _n_], [невозможно прочитать], [единицы, _n_, _r_],
  [нет colorbar], [цвет не читается], [colorbar 1–20],
  [нет порога 140], [клинический контекст потерян], [пунктир 140],
)

#heading(level: 2)[5.07.6 Чек-лист contour]

- ☐ Понятно, что такое «уровень» и что кодирует цвет.
- ☐ Указаны единицы и _n_.
- ☐ Оси не обрезают данные.
- ☐ Уровни подписаны или есть colorbar.
- ☐ Палитра последовательная, не `jet`.
- ☐ Сглаживание не уничтожает реальную структуру.
- ☐ Подписи уровней не налезают.
- ☐ Есть клинический/смысловой порог, если он важен.
- ☐ Для локальной структуры рассмотрен hexbin.
- ☐ Рисунок проверен в конечном размере 85 мм.

#heading(level: 2)[5.07.7 Как воспроизвести]

```bash
uv sync
uv run python 05_charts/07_contour/scripts/make_data.py
uv run python 05_charts/07_contour/scripts/bad_plot.py
uv run python 05_charts/07_contour/scripts/good_plot.py
```

Вот как это выглядит в коде:

```python
hist, xedges, yedges = np.histogram2d(
    age, sbp, bins=(45, 45), range=[[20, 80], [90, 200]]
)
smooth = gaussian_filter(hist, sigma=1.2)
levels = np.logspace(0, np.log10(smooth.max()), 9)
ax.contourf(xx, yy, smooth.T, levels=levels, cmap="cividis")
```

`sigma` и число уровней — параметры сглаживания. Меняйте их
осознанно и проверяйте, что вывод не зависит от выбранного
сглаживания.

#heading(level: 2)[5.07.8 Что дальше]

Следующий график — *5.08 loess*: нелинейный тренд на scatter
с доверительной полосой. У него будет свой генератор и свой
`data/08_dataset.csv`.

#heading(level: 2)[Источники]

- Wilke C. O. _Fundamentals of Data Visualization_. 2019. —
  #link("https://clauswilke.com/dataviz/")[clauswilke.com/dataviz]
- Matplotlib: `contourf` —
  #link("https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html")[matplotlib.org]
- SciPy: `gaussian_filter` —
  #link("https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.gaussian_filter.html")[docs.scipy.org]
- Tufte E. R. _The Visual Display of Quantitative Information_. 1983. —
  #link("https://www.edwardtufte.com/tufte/books_vdqi")[edwardtufte.com]