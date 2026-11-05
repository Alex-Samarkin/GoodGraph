// Раздел 5.27. Kaplan–Meier: выживаемость.
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

#heading(level: 1)[5.27 Kaplan–Meier: выживаемость]

Кривая Каплана–Мейера показывает долю пациентов без события во времени
с учётом *цензурирования*. Это не доля выживших к фиксированному сроку:
кривая пересчитывается в каждом событии, а цензурированные пациенты
выходят из риска, не считаясь событиями.

#heading(level: 2)[5.27.1 Сфера применения]

- время до смерти/рецидива/госпитализации;
- сравнение групп с цензурированием;
- оценка выживаемости к 12/24/36 месяцам;
- проверка пропорциональности рисков (лог-ранг).

Не подходит: нет цензурирования (ECDF), конкурирующие риски
(5.28), сравнение средних без времени.

#heading(level: 2)[5.27.2 Данные]

240 пациентов, две группы по 120, наблюдение до 36 месяцев;
событие — смерть, остальные цензурированы.

#table(
  columns: (1.5fr, 3fr),
  table.header([*Колонка*], [*Смысл*]),
  [`group`], [контроль/лечение],
  [`time_months`], [время наблюдения],
  [`event`], [1 смерть, 0 цензурирование],
)

Генератор: `05_charts/27_kaplan_meier/scripts/make_data.py` → `data/27_dataset.csv`.

#heading(level: 2)[5.27.3 Плохой график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_27_bad_kaplan_meier.png", width: 84%)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.27.1. Плохая KM: обрезанная ось 0,5–1,0, радуга,
    нет цензурирования и риска.
  ]]
]

Код: `05_charts/27_kaplan_meier/scripts/bad_plot.py`.

Ошибки: ось 0,5–1,0 скрывает половину кривых; нет меток
цензурирования, числа под риском, CI; радуга, тяжёлая сетка.

#heading(level: 2)[5.27.4 Правильный график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_27_good_kaplan_meier.png", width: 95mm)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.27.2. Правильная KM: две группы, метки цензурирования,
    риск-таблица, 95 мм.
  ]]
]

Код: `05_charts/27_kaplan_meier/scripts/good_plot.py`.

Улучшения: полный диапазон 0–1, две группы, метки цензурирования,
таблица «число под риском» на 0/12/24/36, единицы, 95 мм.

#heading(level: 2)[5.27.5 Чек-лист]

- ☐ Указано событие и цензурирование.
- ☐ Ось Y 0–1.
- ☐ Метки цензурирования.
- ☐ Число под риском по времени.
- ☐ Указаны n и единицы времени.
- ☐ Нет радуги/тяжёлой сетки.
- ☐ Лог-ранг/HR — если есть сравнение.
- ☐ Проверено в 95 мм.

#heading(level: 2)[5.27.6 Как воспроизвести]

```bash
uv sync
uv run python 05_charts/27_kaplan_meier/scripts/make_data.py
uv run python 05_charts/27_kaplan_meier/scripts/bad_plot.py
uv run python 05_charts/27_kaplan_meier/scripts/good_plot.py
```

#heading(level: 2)[5.27.7 Что дальше]

5.28 Cumulative incidence: конкурирующие риски.

#heading(level: 2)[Источники]

- Kaplan E. L., Meier P. Nonparametric Estimation from Incomplete
  Observations #text("//") _JASA_. 1958. —
  #link("https://doi.org/10.1080/01621459.1958.10501452")[doi:10.1080/01621459.1958.10501452]
- Wilke C. O. _Fundamentals of Data Visualization_. 2019. —
  #link("https://clauswilke.com/dataviz/")[clauswilke.com/dataviz]