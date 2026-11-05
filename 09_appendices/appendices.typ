// Раздел 9. Приложения: R, Julia, электронные таблицы.
// Сборка: typst compile --root . 09_appendices/appendices.typ build/09_appendices.pdf

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
#set table(stroke: 0.5pt + luma(190), inset: (x: 4pt, y: 3pt))
#show table: set text(size: 8pt)
#show raw: set text(font: "DejaVu Sans Mono", size: 8.2pt)
#show raw.where(block: true): it => block(fill: luma(247), inset: 8pt, radius: 2pt, width: 100%, breakable: false, it)

#heading(level: 1)[9. Приложения]

R, Julia и электронные таблицы — краткий обзор и шесть графиков
в каждой среде. Основная методичка построена на Python, но научная
графика не начинается и не заканчивается им.

Чтобы сравнение было честным, все три примера используют *один и тот
же учебный набор* `data/09_appendix_dataset.csv`: 150 пациентов, три
группы, САД на 0/4/8/12-й неделе, возраст, BMI, глюкоза, время до
события и категория нежелательного явления.

Это не учебники по R, Julia и Excel. Скорее — «карта входа»: какие
шесть графиков там делаются естественно, где начинаются ограничения и
что стоит автоматизировать, а что оставить руками.

#heading(level: 2)[A. Системы моделирования и анализа]

#table(
  columns: (1.2fr, 2.2fr, 2.2fr, 2.4fr),
  table.header(repeat: true, [*Среда*], [*Сильная сторона*], [*Ключевые пакеты*], [*Ограничения*]),
  [*R*], [статистика, Bioconductor, ggplot2, отчётные пакеты], [ggplot2, dplyr, tidyr, survival, gridExtra, rmarkdown], [синтаксис непривычен после Python; скорость на больших данных ниже],
  [*Julia*], [скорость, типы, дифференциальные уравнения, большие массивы], [Plots, DataFrames, CSV, DifferentialEquations, Makie], [экосистема меньше; предкомпиляция и версии требуют дисциплины],
  [*Excel / LibreOffice*], [быстрый взгляд, таблицы, ручная правка, отчёты], [встроенные диаграммы, сводные таблицы, условное форматирование], [воспроизводимость, сложные статистические графики, контроль версий],
  [*Python*], [автоматизация, ML, интеграция], [matplotlib, seaborn, plotnine, pandas, statsmodels], [требует кода и настройки окружения],
)

*R* хорош там, где статистика уже живёт в R: модели, тесты, выживаемость,
мета-анализ. `ggplot2` задаёт грамматику слоёв и облегчает faceting;
`survival` и `gridExtra` закрывают KM и сборку панелей. Слабое место —
воспроизводимость проектов: версии пакетов нужно фиксировать (`renv`),
а не «у меня работает».

*Julia* выигрывает, когда важна скорость или математическая модель:
дифференциальные уравнения, оптимизация, большие массивы. `Plots` даёт
быстрый старт, `Makie` — более тонкий контроль. Плата — время на
предкомпиляцию и более молодой набор пакетов; проект лучше держать в
отдельном `Project.toml`/`Manifest.toml`.

*Excel/LibreOffice* незаменим для черновика, быстрой проверки и разговора
с коллегами, которые не пишут код. Но как только нужны доверительные
интервалы, KM, box plot с точками или единый стиль, таблица начинает
проигрывать скрипту. Хорошая стратегия — считать в R/Julia/Python,
а в Excel смотреть и обсуждать.

#heading(level: 2)[B. Шесть графиков в R]

Скрипт: `09_appendices/r/six_plots.R`. Пакеты: `ggplot2`, `gridExtra`,
`survival`. Запуск:

```bash
Rscript 09_appendices/r/six_plots.R
```

#block(breakable: false)[
  #align(center)[#image("../images/09_r_six.png", width: 100%)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 9.1. Шесть графиков в R: линия с 95 % CI, scatter с LOESS,
    box + точки, столбцы с CI, heatmap и Kaplan–Meier.
  ]]
]

Что показано:

+ *Линия* — среднее САД по неделям с 95 % CI; группы различаются цветом.
+ *Scatter + LOESS* — BMI и глюкоза; точки полупрозрачны, шум не скрыт.
+ *Box + jitter* — индивидуальное изменение к 12-й неделе; видно разброс и выбросы.
+ *Столбцы с 95 % CI* — среднее изменение по группам, нулевая линия.
+ *Heatmap* — среднее САД по группе и неделе, значения в ячейках.
+ *Kaplan–Meier* — выживаемость с метками цензурирования, без «1 − KM».

Ключевой фрагмент:

```r
agg <- aggregate(sbp_mm_hg ~ group + week, df,
                 function(x) c(mean = mean(x), sd = sd(x), n = length(x)))
agg <- do.call(data.frame, agg); agg$ci <- 1.96 * agg$sd / sqrt(agg$n)

ggplot(agg, aes(week, mean, color = group)) +
  geom_errorbar(aes(ymin = mean - ci, ymax = mean + ci), width = 0.35) +
  geom_line() + geom_point() +
  scale_color_manual(values = c("#7F7F7F", "#0072B2", "#D55E00")) +
  labs(x = "Неделя", y = "САД, мм рт. ст.")
```

Сильные места R здесь — `geom_ribbon`/`geom_errorbar`, `facet_wrap`,
`survival::survfit` и `gridExtra` для панелей. Слабые — необходимость
помнить про факторы, порядок уровней и `stringsAsFactors`.

#heading(level: 2)[C. Шесть графиков в Julia]

Скрипт: `09_appendices/julia/six_plots.jl`. Проект:
`09_appendices/julia_env/`. Запуск:

```bash
JULIA_DEPOT_PATH="$PWD/.julia:$HOME/.julia" \
julia --project=09_appendices/julia_env 09_appendices/julia/six_plots.jl
```

#block(breakable: false)[
  #align(center)[#image("../images/09_julia_six.png", width: 100%)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 9.2. Шесть графиков в Julia: линия с ribbon, scatter, точки
    с медианой, столбцы с ошибками, heatmap и KM.
  ]]
]

Что показано:

+ *Линия + ribbon* — среднее САД и 95 % CI; `ribbon` рисует полосу.
+ *Scatter* — BMI и глюкоза, цвет по группе; без ложного сглаживания.
+ *Точки + медиана* — индивидуальные изменения и медиана группы.
+ *Столбцы с ошибками* — среднее изменение и 95 % CI.
+ *Heatmap* — среднее САД, значения подписаны.
+ *Kaplan–Meier* — шаговая выживаемость по группам.

Ключевой фрагмент:

```julia
using Plots, DataFrames, CSV, Statistics
df = CSV.read("data/09_appendix_dataset.csv", DataFrame)
agg = combine(groupby(df, [:group, :week]),
              :sbp_mm_hg => mean => :mean,
              :sbp_mm_hg => std => :sd,
              :sbp_mm_hg => length => :n)
agg.ci = 1.96 .* agg.sd ./ sqrt.(agg.n)

plot(agg.week, agg.mean, group = agg.group, ribbon = agg.ci,
     marker = :circle, linecolor = [:gray, :blue, :orange])
```

Julia требует больше дисциплины к окружению: отдельный проект,
`Manifest.toml`, предкомпиляция. Зато `Plots`/`Makie` хорошо ложатся
на большие массивы и математические модели; для интерактивных отчётов
чаще берут Makie или связку с Python.

#heading(level: 2)[D. Шесть графиков в Excel / LibreOffice]

Книга: `09_appendices/excel/make_workbook.py` собирает `.xlsx` с шестью
листами-графиками; данные лежат на скрытых листах. Запуск:

```bash
uv run python 09_appendices/excel/make_workbook.py
```

#block(breakable: false)[
  #align(center)[#image("../images/09_excel_six.png", width: 100%)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 9.3. Шесть графиков в Excel: линия, scatter с трендом,
    столбцы, stacked, pie и bar.
  ]]
]

Что показано:

+ *Линия* — среднее САД по неделям, три серии, ось 120–170.
+ *Scatter* — BMI и глюкоза, линейный тренд, без соединительных линий.
+ *Столбцы* — среднее изменение САД по группам, нулевая линия.
+ *Stacked columns* — нежелательные явления по группам.
+ *Pie* — структура явлений, 3 доли, проценты.
+ *Bar* — доля серьёзных явлений по группам, значения подписаны.

В Excel это делается через *Вставка → Диаграмма*:

#table(
  columns: (1.2fr, 1.8fr, 3.8fr),
  table.header(repeat: true, [*График*], [*Тип Excel*], [*Настройки*]),
  [Линия], [Line], [без 3D, маркеры, ось Y 120–170],
  [Scatter], [XY (Scatter)], [только маркеры, линейный тренд],
  [Столбцы], [Column], [нулевая линия, ось Y −25…5],
  [Stacked], [Stacked Column], [100 % перекрытие, 3 серии],
  [Pie], [Pie], [3 доли, проценты, без 3D],
  [Bar], [Bar], [горизонтально, значения, ось 0–30],
)

Excel силён в простых формах и быстрой правке. Но у него нет
нормального box plot с точками, KM и heatmap «из коробки»; для них
нужны надстройки, Python/R или ручная сборка. Плюс версии файла и
«ручные» правки плохо проверяются в ревью — поэтому книгу лучше
генерировать скриптом, а не править мышью.

#heading(level: 2)[E. Что выбрать]

- *R* — если статистика, модели и отчёт уже в R; ggplot2 + survival.
- *Julia* — если важны скорость, типы и математическая модель.
- *Excel* — если нужен быстрый черновик, таблица или разговор с коллегами;
  для финальных журнальных рисунков — редко.
- *Python* — если нужен единый пайплайн «данные → рисунки → PDF»
  и автоматическая проверка, как в этой методичке.

Хорошая практика — не выбирать «одну среду навсегда», а разделять:
расчёт в R/Julia/Python, просмотр в Excel, финальная вёрстка в
Typst/LaTeX/Illustrator. Тогда сильные стороны каждой среды работают
на результат, а не спорят друг с другом.

#heading(level: 2)[F. Перенос графика между средами]

При переносе одного и того же рисунка из R в Julia, из Julia в Excel
или из любой среды в журнал проверяйте не «похожесть картинки», а
инварианты:

#table(
  columns: (2.1fr, 3.9fr),
  table.header(repeat: true, [*Что проверить*], [*Почему это важно*]),
  [Уровни групп и порядок], [R и Julia по-разному сортируют факторы; порядок меняет легенду и цвета],
  [Неделя как число], [В Excel дата/текст легко превращается в категорию],
  [Пропуски], [`NA`, `missing` и пустая ячейка — разные вещи],
  [Определение CI], [95 % CI среднего, Уилсона или бутстрэп — не взаимозаменяемы],
  [Шрифт и кириллица], [Проверяйте встраивание и наличие глифов в PDF],
  [Размер в мм], [85/170 мм, а не «по ширине окна»],
  [Цвет и печать], [CVD, серый, белый фон, 3:1 для линий],
  [Версии и seed], [Без фиксации версий и seed рисунок не воспроизводится],
)

Практический минимум: сохраните исходные данные, скрипт, версии
пакетов и финальный PDF/SVG. Excel-файл без скрипта — это не
воспроизводимый артефакт, а иллюстрация.

#heading(level: 2)[Источники]

- R Core Team. _R: A Language and Environment for Statistical Computing_. —
  #link("https://www.r-project.org/")[r-project.org]
- Wickham H. _ggplot2: Elegant Graphics for Data Analysis_. 3rd ed., Springer, 2024. —
  #link("https://ggplot2.tidyverse.org/")[ggplot2.tidyverse.org]
- Therneau T. _A Package for Survival Analysis in R_. —
  #link("https://cran.r-project.org/package=survival")[cran.r-project.org]
- Julia Language. _Documentation_. — #link("https://docs.julialang.org/")[docs.julialang.org]
- Plots.jl. _Documentation_. — #link("https://docs.juliaplots.org/")[docs.juliaplots.org]
- Microsoft. _Create a chart from start to finish_. —
  #link("https://support.microsoft.com/en-us/office/create-a-chart-from-start-to-finish-0baf399e-dd61-4e18-8a73-b3fd5d5680c2")[support.microsoft.com]
- LibreOffice. _Charts_. —
  #link("https://help.libreoffice.org/latest/en-US/text/shared/guide/chart_insert.html")[help.libreoffice.org]
