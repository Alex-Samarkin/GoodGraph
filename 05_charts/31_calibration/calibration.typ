// Раздел 5.31. Calibration: соответствие прогноза и реальности.
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

#heading(level: 1)[5.31 Calibration: соответствие прогноза и реальности]

Калибровка отвечает: если модель говорит «риск 30 %», действительно ли
у 30 % наступает событие? ROC/AUC этого не показывают. Идеальная
калибровка — диагональ.

#heading(level: 2)[5.31.1 Данные]

400 пациентов, прогнозируемый риск и бинарный исход; 8 бинов.

Генератор: `05_charts/31_calibration/scripts/make_data.py` → `data/31_dataset.csv`.

#heading(level: 2)[5.31.2 Плохой график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_31_bad_calibration.png", width: 84%)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.31.1. Плохая калибровка: обрезанные оси, нет диагонали и CI.
  ]]
]

Код: `05_charts/31_calibration/scripts/bad_plot.py`. Ошибки: оси 0,2–0,8, нет
диагонали, CI, Brier и n.

#heading(level: 2)[5.31.3 Правильный график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_31_good_calibration.png", width: 85mm)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.31.2. Правильная калибровка: диагональ, Wilson CI, Brier 0,19.
  ]]
]

Код: `05_charts/31_calibration/scripts/good_plot.py`. Диагональ, 8 бинов,
Wilson CI, Brier 0,19, 85 мм.

#heading(level: 2)[5.31.4 Чек-лист]

- ☐ Диагональ идеальной калибровки.
- ☐ Бины и n.
- ☐ CI/uncertainty.
- ☐ Brier или calibration slope.
- ☐ Оси 0–1.
- ☐ Не путать с ROC/AUC.

#heading(level: 2)[5.31.5 Как воспроизвести]

```bash
uv sync
uv run python 05_charts/31_calibration/scripts/make_data.py
uv run python 05_charts/31_calibration/scripts/bad_plot.py
uv run python 05_charts/31_calibration/scripts/good_plot.py
```

#heading(level: 2)[5.31.6 Что дальше]

5.32 Caterpillar plot.

#heading(level: 2)[Источники]

- Van Calster B. et al. Calibration: the Achilles Heel of Predictive
  Analytics #text("//") _BMC Medicine_. 2019. —
  #link("https://doi.org/10.1186/s12916-019-1466-7")[doi:10.1186/s12916-019-1466-7]