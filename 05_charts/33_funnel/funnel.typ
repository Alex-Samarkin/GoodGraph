// Раздел 5.33. Funnel: асимметрия и малые исследования.
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

#heading(level: 1)[5.33 Funnel: асимметрия и малые исследования]

Funnel plot показывает эффект против точности (SE). Воронка — 95 %
область вокруг pooled-эффекта. Асимметрия (малые исследования
«выпадают» из воронки) — сигнал publication bias / small-study effects.

#heading(level: 2)[5.33.1 Данные]

25 исследований, log OR и SE.

Генератор: `05_charts/33_funnel/scripts/make_data.py` → `data/33_dataset.csv`.

#heading(level: 2)[5.33.2 Плохой график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_33_bad_funnel.png", width: 84%)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.33.1. Плохой funnel: без воронки, pooled и подписей.
  ]]
]

Код: `05_charts/33_funnel/scripts/bad_plot.py`. Ошибки: нет 95 % воронки,
pooled-линии, осей эффекта/SE, n.

#heading(level: 2)[5.33.3 Правильный график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_33_good_funnel.png", width: 85mm)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.33.2. Правильный funnel: pooled, 95 % воронка, асимметрия.
  ]]
]

Код: `05_charts/33_funnel/scripts/good_plot.py`. Pooled, 95 % воронка,
SE по Y, точки, заголовок об асимметрии, 85 мм.

#heading(level: 2)[5.33.4 Чек-лист]

- ☐ Эффект по X, SE/точность по Y (SE вниз).
- ☐ Pooled-эффект.
- ☐ 95 % воронка.
- ☐ Указаны k (число исследований).
- ☐ Асимметрия не подана как доказательство bias.
- ☐ Проверено в 85 мм.

#heading(level: 2)[5.33.5 Как воспроизвести]

```bash
uv sync
uv run python 05_charts/33_funnel/scripts/make_data.py
uv run python 05_charts/33_funnel/scripts/bad_plot.py
uv run python 05_charts/33_funnel/scripts/good_plot.py
```

#heading(level: 2)[5.33.6 Итог раздела 5]

Все 33 графика разобраны: данные → плохой пример → разбор →
правильный пример. Каждый — со своим генератором, датасетом,
SVG/PNG и Typst-дубликатом.

#heading(level: 2)[Источники]

- Egger M. et al. Bias in Meta-Analysis Detected by a Simple, Graphical
  Test #text("//") _BMJ_. 1997. —
  #link("https://doi.org/10.1136/bmj.315.7109.629")[doi:10.1136/bmj.315.7109.629]
- Sterne J. A. C. et al. Recommendations for Examining and Interpreting
  Funnel Plot Asymmetry #text("//") _BMJ_. 2011. —
  #link("https://doi.org/10.1136/bmj.d4002")[doi:10.1136/bmj.d4002]