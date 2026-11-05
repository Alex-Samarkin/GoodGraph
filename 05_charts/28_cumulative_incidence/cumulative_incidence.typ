// Раздел 5.28. Cumulative incidence: конкурирующие риски.
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

#heading(level: 1)[5.28 Cumulative incidence: конкурирующие риски]

При конкурирующих рисках событие одного типа мешает событию другого.
Обычная 1 − KM завышает риск, если считать конкурирующее событие
цензурированием. Правильная оценка — кумулятивная заболеваемость
(Aalen–Johansen): суммируются cause-specific hazards с учётом общей
выживаемости.

#heading(level: 2)[5.28.1 Данные]

300 пациентов, 36 месяцев; статус: 0 — цензурирован, 1 — кардиальная
смерть, 2 — некардиальная смерть.

Генератор: `05_charts/28_cumulative_incidence/scripts/make_data.py` → `data/28_dataset.csv`.

#heading(level: 2)[5.28.2 Плохой график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_28_bad_cumulative_incidence.png", width: 84%)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.28.1. Плохая CIF: 1-KM без конкурирующего риска,
    одна кривая, тяжёлая сетка.
  ]]
]

Код: `05_charts/28_cumulative_incidence/scripts/bad_plot.py`.

Ошибки: конкурирующая смерть считается цензурированием; риск завышен;
нет второй кривой, n и единиц.

#heading(level: 2)[5.28.3 Правильный график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_28_good_cumulative_incidence.png", width: 85mm)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.28.2. Правильная CIF: кардиальная и некардиальная смерть,
    0–55 %, прямые подписи.
  ]]
]

Код: `05_charts/28_cumulative_incidence/scripts/good_plot.py`.

Улучшения: две cause-specific CIF, общая выживаемость в знаменателе,
полный диапазон, прямые подписи, 85 мм.

#heading(level: 2)[5.28.4 Чек-лист]

- ☐ Конкурирующие события не считаются цензурированием.
- ☐ Показаны все конкурирующие исходы.
- ☐ Ось 0–разумный максимум.
- ☐ Указаны n, время, единицы.
- ☐ Прямые подписи кривых.
- ☐ Нет 1 − KM как «заболеваемости».
- ☐ Проверено в 85 мм.

#heading(level: 2)[5.28.5 Как воспроизвести]

```bash
uv sync
uv run python 05_charts/28_cumulative_incidence/scripts/make_data.py
uv run python 05_charts/28_cumulative_incidence/scripts/bad_plot.py
uv run python 05_charts/28_cumulative_incidence/scripts/good_plot.py
```

#heading(level: 2)[5.28.6 Что дальше]

5.29 ROC-кривая.

#heading(level: 2)[Источники]

- Fine J. P., Gray R. J. A Proportional Hazards Model for the
  Subdistribution of a Competing Risk #text("//") _JASA_. 1999. —
  #link("https://doi.org/10.1080/01621459.1999.10474144")[doi:10.1080/01621459.1999.10474144]
- Wilke C. O. _Fundamentals of Data Visualization_. 2019. —
  #link("https://clauswilke.com/dataviz/")[clauswilke.com/dataviz]