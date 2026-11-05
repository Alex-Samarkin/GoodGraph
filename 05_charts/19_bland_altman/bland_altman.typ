// Раздел 5.19. Bland–Altman: согласие методов.
// Сборка: typst compile --root . 05_charts/19_bland_altman/bland_altman.typ build/05_19_bland_altman.pdf

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

#heading(level: 1)[5.19 Bland–Altman: согласие методов]

Bland–Altman отвечает на вопрос: *насколько два метода измерения
согласуются?* По X — среднее двух методов, по Y — разница между ними.
Горизонтальная линия — средняя разница (bias), пунктиры — пределы
согласия (limits of agreement, LoA = bias ± 1,96 SD).

Это не корреляция. Два метода могут коррелировать почти идеально
и при этом систематически расходиться; BA показывает именно согласие.

#heading(level: 2)[5.19.1 Сфера применения]

BA отвечает на вопрос: *где проходит средняя разница и в каких
пределах лежат 95 % расхождений?*

Где это пригодится:

- новый анализатор против референсного;
- глюкометр против лаборатории;
- два способа измерения АД;
- согласие шкал/опросников;
- проверка, можно ли заменить метод.

Когда BA *не* нужен:

- сравниваются не методы, а группы;
- нужна корреляция/ассоциация — scatter (5.05);
- нужны только средние — dot + CI (5.14);
- разница зависит от масштаба — нужна лог-трансформация;
- нет парных измерений.

#heading(level: 2)[5.19.2 Данные]

Сценарий: 150 пациентов, глюкоза измерена лабораторным анализатором
и глюкометром. Разница = лаборатория − глюкометр.

#table(
  columns: (1.6fr, 2.6fr, 1.2fr),
  table.header([*Колонка*], [*Смысл*], [*Единица*]),
  [`patient_id`], [идентификатор пациента], [—],
  [`lab_glucose`], [лабораторный анализ], [ммоль/л],
  [`meter_glucose`], [глюкометр], [ммоль/л],
)

Bias = +0,35 ммоль/л; 95 % LoA = −1,09…+1,79 ммоль/л. Глюкометр
систематически занижает, но расхождения укладываются в широкие
пределы.

Генератор: `05_charts/19_bland_altman/scripts/make_data.py` → `data/19_dataset.csv`.

#heading(level: 2)[5.19.3 Плохой график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_19_bad_bland_altman.png", width: 84%)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.19.1. Плохой BA: по X один метод, нет bias и LoA,
    обрезанная ось 0–2, радуга.
  ]]
]

Код: `05_charts/19_bland_altman/scripts/bad_plot.py`.

Что не так:

+ *По X — один метод, а не среднее двух.* Это не BA; разница
  может коррелировать с масштабом.
+ *Нет bias и LoA.* Непонятно, где средняя разница и границы
  согласия.
+ *Ось Y обрезана до 0–2.* Отрицательные разницы скрыты;
  картина согласия искажена.
+ *Радужные точки, тяжёлая сетка, полная рамка.*
+ *Заголовок «Разница методов».* Не сообщает вывод.
+ *Нет единиц и n.*

#heading(level: 2)[5.19.4 Правильный график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_19_good_bland_altman.png", width: 85mm)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.19.2. Правильный BA: среднее по X, разница по Y,
    bias +0,35 и LoA −1,09…+1,79.
  ]]
]

Код: `05_charts/19_bland_altman/scripts/good_plot.py`.

Что изменилось:

+ *По X — среднее двух методов.*
+ *Bias +0,35 и 95 % LoA −1,09…+1,79* — линии и подписи.
+ *Полный диапазон разниц −2,5…+2,5.*
+ *Один цвет, полупрозрачные точки.*
+ *Единицы, n = 150, заголовок-вывод.*
+ *Лёгкая сетка по Y, 85 мм.*

Bias — систематическое расхождение; LoA — случайное. Если LoA шире
клинически допустимого, методы нельзя считать взаимозаменяемыми,
даже если bias мал.

#heading(level: 2)[5.19.5 Было и стало]

#table(
  columns: (1.5fr, 2fr, 2fr),
  table.header([*Что было*], [*Почему плохо*], [*Что сделано*]),
  [по X один метод], [это не BA], [среднее двух методов],
  [нет bias/LoA], [нет согласия], [линии и подписи],
  [ось Y 0–2], [отрицательные скрыты], [−2,5…+2,5],
  [радуга], [CVD, декор], [один цвет],
  [сетка по X и Y], [шум], [сетка только по Y],
  [полная рамка], [визуальный шум], [только левая и нижняя оси],
  [«Разница методов»], [нет вывода], [заголовок с bias],
  [нет единиц и n], [невозможно прочитать], [единицы, n = 150],
)

#heading(level: 2)[5.19.6 Чек-лист Bland–Altman]

- ☐ По X — среднее двух методов.
- ☐ По Y — разница (указано, какой метод из какого вычитается).
- ☐ Показаны bias и 95 % LoA.
- ☐ Ось Y не обрезает разницы.
- ☐ Указаны единицы и _n_.
- ☐ Проверена пропорциональная bias (наклон).
- ☐ LoA сопоставлены с клинически допустимыми.
- ☐ Нет корреляции вместо согласия.
- ☐ Выбросы видны.
- ☐ Рисунок проверен в конечном размере 85 мм.

#heading(level: 2)[5.19.7 Как воспроизвести]

```bash
uv sync
uv run python 05_charts/19_bland_altman/scripts/make_data.py
uv run python 05_charts/19_bland_altman/scripts/bad_plot.py
uv run python 05_charts/19_bland_altman/scripts/good_plot.py
```

Вот как это выглядит в коде:

```python
mean = (lab + meter) / 2
diff = lab - meter
bias = diff.mean()
loa = 1.96 * diff.std(ddof=1)

ax.scatter(mean, diff, s=14, alpha=0.45)
ax.axhline(bias, color="#333333")
ax.axhline(bias - loa, color=ACCENT_VERMILLION, linestyle="--")
ax.axhline(bias + loa, color=ACCENT_VERMILLION, linestyle="--")
```

Если разброс разницы растёт с уровнем, постройте BA для логарифмов
или добавьте регрессию разницы на среднее.

#heading(level: 2)[5.19.8 Что дальше]

Следующий график — *5.20 stacked bar*: состав целого по категориям.
У него будет свой генератор и свой `data/20_dataset.csv`.

#heading(level: 2)[Источники]

- Bland J. M., Altman D. G. Statistical Methods for Assessing Agreement
  between Two Methods of Clinical Measurement #text("//") _The Lancet_. 1986. —
  #link("https://doi.org/10.1016/S0140-6736(86)90837-8")[doi:10.1016/S0140-6736(86)90837-8]
- Giavarina D. Understanding Bland Altman Analysis #text("//") _Biochemia Medica_. 2015. —
  #link("https://doi.org/10.11613/BM.2015.015")[doi:10.11613/BM.2015.015]
- Wilke C. O. _Fundamentals of Data Visualization_. 2019. —
  #link("https://clauswilke.com/dataviz/")[clauswilke.com/dataviz]