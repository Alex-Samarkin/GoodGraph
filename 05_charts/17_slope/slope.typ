// Раздел 5.17. Slope: изменение между двумя точками.
// Сборка: typst compile --root . 05_charts/17_slope/slope.typ build/05_17_slope.pdf

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

#heading(level: 1)[5.17 Slope: изменение между двумя точками]

Slope plot соединяет две точки — «до» и «после» — для нескольких групп.
Наклон линии показывает направление и величину изменения, а набор
линий — гетерогенность эффекта.

Это график *парных агрегатов* (средних по группам), а не spaghetti
из сотен индивидуальных траекторий: при больших _n_ линии сливаются.

#heading(level: 2)[5.17.1 Сфера применения]

Slope отвечает на вопрос: *как изменился показатель в каждой группе
и насколько различается эффект?*

Где это пригодится:

- средние до/после программы по клиникам;
- парные измерения до/после лечения;
- изменение доли/риска по центрам;
- сравнение эффекта вмешательства в 2–8 группах;
- наглядная величина сдвига.

Когда slope *не* нужен:

- больше 8–10 групп — spaghetti/labels;
- нужны индивидуальные траектории — paired dot (5.18);
- нет парных измерений;
- нужно распределение — box/violin;
- динамика многих временных точек — line.

#heading(level: 2)[5.17.2 Данные]

Сценарий: 360 пациентов, шесть клиник, по 60 человек. Вес до и через
12 недель программы снижения веса.

#table(
  columns: (1.5fr, 2.6fr, 1.2fr),
  table.header([*Колонка*], [*Смысл*], [*Единица*]),
  [`patient_id`], [идентификатор пациента], [—],
  [`clinic`], [клиника], [—],
  [`weight_before_kg`], [вес до], [кг],
  [`weight_after_kg`], [вес после], [кг],
)

Среднее снижение — 6,7 кг. Клиника C — лидер: −11,2 кг; клиника D —
минимум: −3,8 кг. Все клиники снизили вес.

Генератор: `05_charts/17_slope/scripts/make_data.py` → `data/17_dataset.csv`.

#heading(level: 2)[5.17.3 Плохой график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_17_bad_slope.png", width: 84%)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.17.1. Плохой slope: шесть радужных линий без подписей,
    обрезанная ось 82–102, нет единиц и n.
  ]]
]

Код: `05_charts/17_slope/scripts/bad_plot.py`.

Что не так:

+ *Шесть радужных линий без подписей.* Непонятно, где какая
  клиника; цвет не помогает.
+ *Ось Y обрезана до 82–102.* Нижние значения и размах скрыты.
+ *Нет подписей «до/после» и единиц.*
+ *Тяжёлая сетка, полная рамка.*
+ *Заголовок «Вес до и после».* Не сообщает вывод.
+ *Нет n и изменения в кг.*

#heading(level: 2)[5.17.4 Правильный график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_17_good_slope.png", width: 100%)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.17.2. Правильный slope: серые линии, акцент на лидере,
    подписи до/после, 120 мм.
  ]]
]

Код: `05_charts/17_slope/scripts/good_plot.py`.

Что изменилось:

+ *Серые линии для всех, акцент на лидере.* Видно общий паттерн
  и лучший результат.
+ *Прямые подписи слева и справа* с лидер-линиями:
  клиника и вес до, вес после и изменение.
+ *Полный диапазон 80–106 кг.*
+ *Подписи «До/После», единицы, n = 60.*
+ *Заголовок-вывод:* все клиники снизили вес в среднем на 6,7 кг.
+ *120 мм* — хватает места для подписей.

Slope показывает *направление и величину* изменения, но не
статистическую значимость. Для вывода о различии эффектов нужны
парный тест/модель и доверительные интервалы.

#heading(level: 2)[5.17.5 Было и стало]

#table(
  columns: (1.5fr, 2fr, 2fr),
  table.header([*Что было*], [*Почему плохо*], [*Что сделано*]),
  [радуга без подписей], [непонятно, где кто], [серые + акцент + подписи],
  [ось Y 82–102], [размах скрыт], [80–106],
  [нет «до/после»], [непонятны точки], [подписи осей],
  [нет единиц], [«вес» без кг], [«Вес, кг»],
  [сетка по X и Y], [шум], [сетка только по Y],
  [полная рамка], [визуальный шум], [только левая и нижняя оси],
  [«Вес до и после»], [нет вывода], [заголовок-вывод],
  [нет n], [непонятна точность], [n = 60],
)

#heading(level: 2)[5.17.6 Чек-лист slope]

- ☐ Понятно, что слева «до», справа «после».
- ☐ Каждая линия подписана.
- ☐ Ось не обрезает диапазон.
- ☐ Указаны единицы и _n_.
- ☐ Линия не тонет в радуге.
- ☐ Акцент оправдан (лидер/аутлайер).
- ☐ Для многих групп — не spaghetti.
- ☐ Для индивидуальных пар — paired dot.
- ☐ Нет ложной причинности.
- ☐ Рисунок проверен в конечном размере.

#heading(level: 2)[5.17.7 Как воспроизвести]

```bash
uv sync
uv run python 05_charts/17_slope/scripts/make_data.py
uv run python 05_charts/17_slope/scripts/bad_plot.py
uv run python 05_charts/17_slope/scripts/good_plot.py
```

Вот как это выглядит в коде:

```python
ax.plot([0, 1], [before, after], color="#8A8A8A", marker="o")
ax.annotate(f"{clinic}  {before:.0f}", xy=(0, before), xytext=(-0.1, label_y),
            ha="right", arrowprops={"arrowstyle": "-", "color": "#BBBBBB"})
ax.set_xticks([0, 1])
ax.set_xticklabels(["До", "После"])
```

Подписи можно развести по вертикали, сохраняя порядок; стрелки
свяжут подпись с точкой.

#heading(level: 2)[5.17.8 Что дальше]

Следующий график — *5.18 paired dot*: индивидуальные парные
изменения. У него будет свой генератор и свой `data/18_dataset.csv`.

#heading(level: 2)[Источники]

- Wilke C. O. _Fundamentals of Data Visualization_. 2019. —
  #link("https://clauswilke.com/dataviz/")[clauswilke.com/dataviz]
- Tufte E. R. _The Visual Display of Quantitative Information_. 1983. —
  #link("https://www.edwardtufte.com/tufte/books_vdqi")[edwardtufte.com]
- Matplotlib: `annotate` —
  #link("https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html")[matplotlib.org]