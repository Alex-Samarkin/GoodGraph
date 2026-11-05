// Раздел 5.26. Corr matrix: корреляционная матрица.
#set page(paper: "a4", margin: (x: 21mm, y: 20mm), numbering: "1")
#set text(font: ("Liberation Serif", "DejaVu Serif"), size: 10.5pt, lang: "ru", hyphenate: true)
#set par(justify: true, leading: 0.64em, spacing: 1.05em)
#show heading: set text(font: ("Liberation Sans", "DejaVu Sans"), weight: "bold")
#show heading: set text(hyphenate: false)
#show heading.where(level: 1): set text(size: 17pt)
#show heading.where(level: 2): set text(size: 13.5pt)
#show heading: it => block(above: 1.15em, below: 0.55em, it)
#set list(indent: 1.2em, spacing: 0.5em)
#set enum(indent: 1.2em, spacing: 0.5em)
#set table(stroke: 0.5pt + luma(190), inset: (x: 5pt, y: 4pt))
#show table: set text(size: 9pt)
#show raw: set text(font: "DejaVu Sans Mono", size: 8.2pt)
#show raw.where(block: true): it => block(fill: luma(247), inset: 8pt, radius: 2pt, width: 100%, breakable: false, it)

#heading(level: 1)[5.26 Corr matrix: корреляционная матрица]

Корреляционная матрица показывает парные связи многих переменных.
Она полезна как *обзор*, но легко перегружается: верхний треугольник
дублирует нижний, а цвет без коэффициентов и шкалы −1…1 обманчив.

#heading(level: 2)[5.26.1 Сфера применения]

- обзор корреляций 5–15 биомаркеров;
- проверка мультиколлинеарности;
- выбор переменных для модели;
- поиск блоков связанных признаков.

Не подходит: причинность, малые выборки, нелинейные связи,
много переменных (>20).

#heading(level: 2)[5.26.2 Данные]

500 пациентов, 8 показателей: возраст, BMI, САД, глюкоза, HbA1c,
ЛПНП, СРБ, eGFR. Корреляции — Пирсона.

Генератор: `05_charts/26_corr_matrix/scripts/make_data.py` → `data/26_dataset.csv`.

#heading(level: 2)[5.26.3 Плохой график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_26_bad_corr_matrix.png", width: 84%)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.26.1. Плохая корреляционная матрица: полная, jet,
    без коэффициентов.
  ]]
]

Код: `05_charts/26_corr_matrix/scripts/bad_plot.py`.

Ошибки: полная матрица с дублированием, `jet`, нет коэффициентов,
нет шкалы −1…1, заголовок «Корреляции».

#heading(level: 2)[5.26.4 Правильный график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_26_good_corr_matrix.png", width: 100mm)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.26.2. Правильная корреляционная матрица: нижний
    треугольник, RdBu_r, коэффициенты.
  ]]
]

Код: `05_charts/26_corr_matrix/scripts/good_plot.py`.

Улучшения: нижний треугольник, `RdBu_r` с центром 0 и границами
−1…1, коэффициенты в ячейках, colorbar «r», заголовок-вывод, 100 мм.

#heading(level: 2)[5.26.5 Чек-лист]

- ☐ Показан только нижний/верхний треугольник.
- ☐ Шкала −1…1 и центр 0.
- ☐ Коэффициенты подписаны.
- ☐ Указан метод (Пирсон/Спирмен).
- ☐ Указаны n и единицы.
- ☐ Нет `jet`.
- ☐ Не интерпретируется как причинность.
- ☐ Проверено в 100 мм.

#heading(level: 2)[5.26.6 Как воспроизвести]

```bash
uv sync
uv run python 05_charts/26_corr_matrix/scripts/make_data.py
uv run python 05_charts/26_corr_matrix/scripts/bad_plot.py
uv run python 05_charts/26_corr_matrix/scripts/good_plot.py
```

#heading(level: 2)[5.26.7 Что дальше]

5.27 Kaplan–Meier: выживаемость.

#heading(level: 2)[Источники]

- Wilke C. O. _Fundamentals of Data Visualization_. 2019. —
  #link("https://clauswilke.com/dataviz/")[clauswilke.com/dataviz]
- Seaborn: `heatmap` —
  #link("https://seaborn.pydata.org/generated/seaborn.heatmap.html")[seaborn.pydata.org]