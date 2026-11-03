// Главный файл сборки методички.
// Сборка: typst compile --root . typst/main.typ build/metodichka.pdf

#set document(
  title: "GoodGraph — методичка по научной графике на Python",
  author: ("GoodGraph",),
  keywords: ("научная графика", "matplotlib", "визуализация данных", "Python"),
)

#set page(
  paper: "a4",
  margin: (x: 21mm, y: 20mm),
  numbering: "1",
)
#set text(
  font: ("Liberation Serif", "DejaVu Serif"),
  size: 10.5pt,
  lang: "ru",
  hyphenate: true,
)
#set par(justify: true, leading: 0.64em, spacing: 1.05em)
#set heading(numbering: none)
#show heading: set text(font: ("Liberation Sans", "DejaVu Sans"), weight: "bold")
#show heading.where(level: 1): set text(size: 17pt)
#show heading.where(level: 2): set text(size: 13.5pt)
#show heading.where(level: 3): set text(size: 11.5pt)
#show heading: it => block(above: 1.15em, below: 0.55em, it)
#set table(stroke: 0.5pt + luma(190), inset: (x: 5pt, y: 4pt))
#show table: set text(size: 9pt)

// ---------------------------------------------------------------------------
// Титульная страница
// ---------------------------------------------------------------------------
#align(center)[
  #v(38mm)
  #text(
    size: 32pt,
    weight: "bold",
    font: "Liberation Sans",
    fill: rgb("#0072B2"),
  )[GoodGraph]
  #v(6mm)
  #text(size: 16pt)[Методичка по научной графике на Python]
  #v(5mm)
  #text(size: 10.5pt, fill: luma(90))[Принципы · нормативы · примеры «плохо/хорошо»]
  #v(24mm)
  #text(size: 9pt, fill: luma(110))[Версия 0.1 · ноябрь 2026]
]

#pagebreak()

// ---------------------------------------------------------------------------
// Содержание
// ---------------------------------------------------------------------------
#show outline: set text(size: 10pt)
#outline(title: "Содержание", indent: 1.2em, depth: 1)

#pagebreak()

// ---------------------------------------------------------------------------
// Разделы. По мере готовности добавляйте сюда новые include.
// ---------------------------------------------------------------------------
#include "../01_principles/principles.typ"

#pagebreak()

#include "../02_python/python.typ"

#pagebreak()

#include "../03_requirements/requirements.typ"

#pagebreak()

#include "../04_overview/overview.typ"

#pagebreak()

#include "../05_charts/01_line/line.typ"

#pagebreak()

#include "../05_charts/02_step/step.typ"

#pagebreak()

#include "../05_charts/03_area/area.typ"

#pagebreak()

#include "../05_charts/04_small_multiples/small_multiples.typ"

#pagebreak()

#include "../05_charts/05_scatter/scatter.typ"

#pagebreak()

#include "../05_charts/06_hexbin/hexbin.typ"

#pagebreak()

#include "../05_charts/07_contour/contour.typ"

#pagebreak()

#include "../05_charts/08_loess/loess.typ"

#pagebreak()

#include "../05_charts/09_histogram/histogram.typ"

#pagebreak()

#include "../05_charts/10_ecdf/ecdf.typ"

#pagebreak()

#include "../05_charts/11_box/box.typ"

#pagebreak()

#include "../05_charts/12_violin/violin.typ"

#pagebreak()

#include "../05_charts/13_strip/strip.typ"

#pagebreak()

#include "../05_charts/14_dot_ci/dot_ci.typ"

#pagebreak()

#include "../05_charts/15_bar/bar.typ"

#pagebreak()

#include "../05_charts/16_forest/forest.typ"

#pagebreak()

#include "../05_charts/17_slope/slope.typ"

#pagebreak()

#include "../05_charts/18_paired_dot/paired_dot.typ"

#pagebreak()

#include "../05_charts/19_bland_altman/bland_altman.typ"

#pagebreak()

#include "../05_charts/20_stacked_bar/stacked_bar.typ"

#pagebreak()

#include "../05_charts/21_bar_100/bar_100.typ"

#pagebreak()

#include "../05_charts/22_pie/pie.typ"

#pagebreak()

#include "../05_charts/23_treemap/treemap.typ"
