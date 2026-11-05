// Раздел 5.32. Caterpillar: упорядоченные оценки.
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

#heading(level: 1)[5.32 Caterpillar: упорядоченные оценки]

Caterpillar plot — это точки оценок с доверительными интервалами,
отсортированные по величине. Он показывает и ранг, и точность:
нельзя сравнивать центры только по точке, если интервалы перекрываются.

#heading(level: 2)[5.32.1 Данные]

30 центров, по 80 пациентов, осложнения. 95 % ДИ Уилсона.

Генератор: `05_charts/32_caterpillar/scripts/make_data.py` → `data/32_dataset.csv`.

#heading(level: 2)[5.32.2 Плохой график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_32_bad_caterpillar.png", width: 84%)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.32.1. Плохой caterpillar: без сортировки и CI,
    обрезанная ось, радуга.
  ]]
]

Код: `05_charts/32_caterpillar/scripts/bad_plot.py`. Ошибки: нет сортировки,
CI, общей линии, n; обрезанная ось.

#heading(level: 2)[5.32.3 Правильный график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_32_good_caterpillar.png", width: 85mm)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.32.2. Правильный caterpillar: сортировка, Wilson CI,
    общая линия, крайние центры выделены.
  ]]
]

Код: `05_charts/32_caterpillar/scripts/good_plot.py`. Сортировка, 95 % CI,
общая линия, крайние центры акцентированы, 85 мм.

#heading(level: 2)[5.32.4 Чек-лист]

- ☐ Сортировка по оценке.
- ☐ 95 % CI для каждой оценки.
- ☐ Общая/референсная линия.
- ☐ Указаны n и единицы.
- ☐ Пересечение CI не игнорируется.
- ☐ Крайние центры выделены осознанно.
- ☐ Проверено в 85 мм.

#heading(level: 2)[5.32.5 Как воспроизвести]

```bash
uv sync
uv run python 05_charts/32_caterpillar/scripts/make_data.py
uv run python 05_charts/32_caterpillar/scripts/bad_plot.py
uv run python 05_charts/32_caterpillar/scripts/good_plot.py
```

#heading(level: 2)[5.32.6 Что дальше]

5.33 Funnel plot.

#heading(level: 2)[Источники]

- Spiegelhalter D. J. Funnel Plots for Comparing Institutional Performance
  #text("//") _Statistics in Medicine_. 2005. —
  #link("https://doi.org/10.1002/sim.1970")[doi:10.1002/sim.1970]