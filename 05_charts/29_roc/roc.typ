// Раздел 5.29. ROC: чувствительность и специфичность.
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
#show raw: set text(font: "DejaVu Sans Mono", size: 8.2pt)
#show raw.where(block: true): it => block(fill: luma(247), inset: 8pt, radius: 2pt, width: 100%, breakable: false, it)

#heading(level: 1)[5.29 ROC: чувствительность и специфичность]

ROC показывает компромисс TPR/FPR при всех порогах; AUC — площадь.
AUC 0,5 — случайность, 1 — идеал. ROC полезна для баланса классов,
но при редком исходе PR информативнее (5.30).

#heading(level: 2)[5.29.1 Данные]

500 пациентов, score и бинарный исход; prevalence 31 %.

Генератор: `05_charts/29_roc/scripts/make_data.py` → `data/29_dataset.csv`.

#heading(level: 2)[5.29.2 Плохой график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_29_bad_roc.png", width: 84%)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.29.1. Плохая ROC: обрезанные оси 0–0,8, нет диагонали и AUC.
  ]]
]

Код: `05_charts/29_roc/scripts/bad_plot.py`. Ошибки: обрезаны оси, нет
диагонали, AUC/n, тяжёлая сетка.

#heading(level: 2)[5.29.3 Правильный график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_29_good_roc.png", width: 85mm)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.29.2. Правильная ROC: диагональ, AUC 0,84, полный диапазон.
  ]]
]

Код: `05_charts/29_roc/scripts/good_plot.py`. Диагональ, AUC 0,84,
оси 0–1, единицы, 85 мм.

#heading(level: 2)[5.29.4 Чек-лист]

- ☐ Оси 0–1.
- ☐ Диагональ случайного классификатора.
- ☐ AUC и n.
- ☐ Указан порог/цель.
- ☐ Для редкого исхода — PR.

#heading(level: 2)[5.29.5 Как воспроизвести]

```bash
uv sync
uv run python 05_charts/29_roc/scripts/make_data.py
uv run python 05_charts/29_roc/scripts/bad_plot.py
uv run python 05_charts/29_roc/scripts/good_plot.py
```

#heading(level: 2)[5.29.6 Что дальше]

5.30 Precision–recall.

#heading(level: 2)[Источники]

- Fawcett T. An Introduction to ROC Analysis #text("//") _Pattern Recognition Letters_. 2006. —
  #link("https://doi.org/10.1016/j.patrec.2005.10.010")[doi:10.1016/j.patrec.2005.10.010]
