// Раздел 5.30. Precision–recall: редкий исход.
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

#heading(level: 1)[5.30 Precision–recall: редкий исход]

При редком исходе ROC выглядит оптимистично: большое число TN маскирует
ложные срабатывания. PR-кривая показывает precision (сколько
предсказанных событий истинны) и recall (какую долю событий поймали).

#heading(level: 2)[5.30.1 Данные]

600 пациентов, prevalence 8 %; score и событие.

Генератор: `05_charts/30_precision_recall/scripts/make_data.py` → `data/30_dataset.csv`.

#heading(level: 2)[5.30.2 Плохой график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_30_bad_precision_recall.png", width: 84%)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.30.1. Плохой PR: обрезанные оси, нет baseline и AP.
  ]]
]

Код: `05_charts/30_precision_recall/scripts/bad_plot.py`. Ошибки: оси 0,2–1,
нет baseline prevalence, AP, n.

#heading(level: 2)[5.30.3 Правильный график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_30_good_precision_recall.png", width: 85mm)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.30.2. Правильный PR: baseline 8 %, AP 0,46, полный диапазон.
  ]]
]

Код: `05_charts/30_precision_recall/scripts/good_plot.py`. Baseline, AP 0,46,
оси 0–1, 85 мм.

#heading(level: 2)[5.30.4 Чек-лист]

- ☐ Указана prevalence/baseline.
- ☐ Оси 0–1.
- ☐ AP или AUC-PR.
- ☐ n и событие.
- ☐ Для редкого исхода PR, не только ROC.

#heading(level: 2)[5.30.5 Как воспроизвести]

```bash
uv sync
uv run python 05_charts/30_precision_recall/scripts/make_data.py
uv run python 05_charts/30_precision_recall/scripts/bad_plot.py
uv run python 05_charts/30_precision_recall/scripts/good_plot.py
```

#heading(level: 2)[5.30.6 Что дальше]

5.31 Calibration.

#heading(level: 2)[Источники]

- Saito T., Rehmsmeier M. The Precision-Recall Plot Is More Informative
  than the ROC Plot #text("//") _PLoS ONE_. 2015. —
  #link("https://doi.org/10.1371/journal.pone.0118432")[doi:10.1371/journal.pone.0118432]
