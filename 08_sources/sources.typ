// Раздел 8. Источники.
// Сборка: typst compile --root . 08_sources/sources.typ build/08_sources.pdf

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

= 8. Источники
<источники>
Это скорее карта, чем библиография: что почитать, чем пользоваться и где
сверять требования. Часть источников далека от Python --- типографика,
шрифты, генераторы диаграмм, экспорт, --- но именно от них часто зависит,
будет ли рисунок выглядеть профессионально.

== 8.1 Как пользоваться списком
<как-пользоваться-списком>
+ #strong[Сначала первоисточник.] Для требований журнала ---
  `author guidelines`, для статистики --- статья/учебник, для
  инструмента --- официальная документация.
+ #strong[Потом обзор.] Книги и руководства помогают выбрать метод, но
  не заменяют проверку актуальных требований.
+ #strong[Ссылки стареют.] Проверяйте дату доступа и версию; для ПО
  указывайте версию в методах.
+ #strong[Не цитируйте блог вместо стандарта.] Блог может объяснять, но
  не должен быть единственным основанием для норматива.

== 8.2 Визуализация и восприятие
<визуализация-и-восприятие>
- Tufte E. R. #emph[The Visual Display of Quantitative Information].
  Graphics Press, 1983. ---
  #link("https://www.edwardtufte.com/tufte/books_vdqi")[edwardtufte.com].
  Классика про «чернила», пропорции и графическую честность.
- Tufte E. R. #emph[Envisioning Information]. Graphics Press, 1990. ---
  #link("https://www.edwardtufte.com/tufte/books_ei")[edwardtufte.com].
  Плотность, слои, малые кратные.
- Wilke C. O. #emph[Fundamentals of Data Visualization]. O'Reilly, 2019.
  --- #link("https://clauswilke.com/dataviz/")[clauswilke.com/dataviz].
  Лучший современный учебник по выбору формы.
- Cairo A. #emph[The Truthful Art]. New Riders, 2016. ---
  #link("https://www.thefunctionalart.com/")[thefunctionalart.com].
  Честность, неопределённость, дизайн.
- Munzner T. #emph[Visualization Analysis and Design]. CRC Press, 2014.
  --- #link("https://www.cs.ubc.ca/~tmm/vadbook/")[cs.ubc.ca].
  Формальная рамка «данные --- задачи --- кодирование».
- Ware C. #emph[Information Visualization: Perception for Design]. 4th
  ed., Morgan Kaufmann, 2020. ---
  #link("https://www.elsevier.com/books/information-visualization/ware/978-0-12-812875-6")[elsevier.com].
  Почему глаз видит одно, а не другое.
- Cleveland W. S., McGill R. Graphical Perception /\/ #emph[JASA]. 1984.
  ---
  #link("https://doi.org/10.1080/01621459.1984.10478080")[doi:10.1080/01621459.1984.10478080].
  Экспериментальная база «положение лучше длины, длины лучше угла».
- Few S. #emph[Show Me the Numbers]. Analytics Press, 2012. ---
  #link("https://www.perceptualedge.com/")[perceptualedge.com]. Деловая
  графика и таблицы.
- Kirk A. #emph[Data Visualisation: A Handbook for Data Driven Design].
  SAGE, 2019. ---
  #link("https://www.visualisingdata.com/")[visualisingdata.com].
  Процесс дизайна, а не только код.
- Schwabish J. #emph[Better Data Visualizations]. Columbia UP, 2021. ---
  #link("https://policyviz.com/books/")[policyviz.com]. Практические
  паттерны для отчётов и статей.
- Knaflic C. N. #emph[Storytelling with Data]. Wiley, 2015. ---
  #link("https://www.storytellingwithdata.com/books")[storytellingwithdata.com].
  Контекст, нарратив, презентация.
- Bergstrom C. T., West J. D. #emph[Calling Bullshit]. Random House,
  \2020. --- #link("https://callingbullshit.org/")[callingbullshit.org].
  Как не обмануться графиком и статистикой.

== 8.3 Статистическая графика и отчёты
<статистическая-графика-и-отчёты>
- Weissgerber T. L. et al.~Beyond Bar and Line Graphs /\/ #emph[PLoS
  Biology].
  \2015. ---
  #link("https://doi.org/10.1371/journal.pbio.1002128")[doi:10.1371/journal.pbio.1002128].
  Почему точки и распределения лучше столбцов.
- Cumming G. #emph[Understanding the New Statistics]. Routledge, 2012.
  ---
  #link("https://www.routledge.com/Understanding-the-New-Statistics-Effect-Sizes-Confidence-Intervals-and-Meta-Analysis/Cumming/p/book/9780415879682")[routledge.com].
  Эффекты, CI, мета-анализ.
- Bland J. M., Altman D. G. Statistical Methods for Assessing Agreement
  \/\/ #emph[The Lancet]. 1986. ---
  #link("https://doi.org/10.1016/S0140-6736(86)90837-8")[doi:10.1016/S0140-6736(86)90837-8].
  Bland--Altman.
- Fawcett T. An Introduction to ROC Analysis /\/ #emph[Pattern
  Recognition Letters]. 2006. ---
  #link("https://doi.org/10.1016/j.patrec.2005.10.010")[doi:10.1016/j.patrec.2005.10.010].
  ROC, AUC, пороги.
- Saito T., Rehmsmeier M. The Precision-Recall Plot Is More Informative
  than the ROC Plot /\/ #emph[PLoS ONE]. 2015. ---
  #link("https://doi.org/10.1371/journal.pone.0118432")[doi:10.1371/journal.pone.0118432].
  Редкие исходы.
- Van Calster B. et al.~Calibration: the Achilles Heel of Predictive
  Analytics /\/ #emph[BMC Medicine]. 2019. ---
  #link("https://doi.org/10.1186/s12916-019-1466-7")[doi:10.1186/s12916-019-1466-7].
  Калибровка прогноза.
- Steyerberg E. W. #emph[Clinical Prediction Models]. 2nd ed., Springer,
  \2019. ---
  #link("https://link.springer.com/book/10.1007/978-3-030-16399-0")[springer.com].
  Прогностические модели, валидация, калибровка.
- Harrell F. E. #emph[Regression Modeling Strategies]. 2nd ed.,
  Springer, 2015. --- #link("https://hbiostat.org/rmsc/")[hbiostat.org].
  Регрессия, номограммы, оценка моделей.
- Kaplan E. L., Meier P. Nonparametric Estimation from Incomplete
  Observations /\/ #emph[JASA]. 1958. ---
  #link("https://doi.org/10.1080/01621459.1958.10501452")[doi:10.1080/01621459.1958.10501452].
  KM-оценка.
- Fine J. P., Gray R. J. A Proportional Hazards Model for the
  Subdistribution of a Competing Risk /\/ #emph[JASA]. 1999. ---
  #link("https://doi.org/10.1080/01621459.1999.10474144")[doi:10.1080/01621459.1999.10474144].
  Конкурирующие риски.
- Cochrane Handbook for Systematic Reviews of Interventions. ---
  #link("https://training.cochrane.org/handbook")[training.cochrane.org].
  Мета-анализ, forest/funnel, гетерогенность.
- Spiegelhalter D. #emph[The Art of Statistics]. Pelican, 2019. ---
  #link("https://www.penguin.co.uk/books/294857/the-art-of-statistics-by-spiegelhalter-david/9780241258767")[penguin.co.uk].
  Как думать о данных, а не только рисовать.

== 8.4 Цвет, доступность, восприятие
<цвет-доступность-восприятие>
- Okabe M., Ito K. Color Universal Design (CUD). 2008. ---
  #link("https://jfly.uni-koeln.de/color/")[jfly.uni-koeln.de/color].
  Палитра, различимая при CVD.
- ColorBrewer 2.0. ---
  #link("https://colorbrewer2.org/")[colorbrewer2.org]. Качественные,
  последовательные, дивергентные шкалы.
- Tol P. Colour Schemes. ---
  #link("https://personal.sron.nl/~pault/")[personal.sron.nl/\~pault].
  Наборы bright/muted, проверенные на различимость.
- Smith N., van der Walt S. Viridis. ---
  #link("https://bids.github.io/colormap/")[bids.github.io/colormap].
  Воспринимательно равномерная шкала.
- Crameri F. Scientific Colour Maps. ---
  #link("https://www.fabiocrameri.ch/colourmaps/")[fabiocrameri.ch/colourmaps].
  Научные палитры, включая CVD-безопасные.
- W3C. Web Content Accessibility Guidelines (WCAG) 2.2. ---
  #link("https://www.w3.org/TR/WCAG22/")[w3.org/TR/WCAG22]. Контраст,
  не-цветовые подсказки.
- WebAIM Contrast Checker. ---
  #link("https://webaim.org/resources/contrastchecker/")[webaim.org/resources/contrastchecker].
  Быстрая проверка контраста.
- Coblis Color Blindness Simulator. ---
  #link("https://www.color-blindness.com/coblis-color-blindness-simulator/")[color-blindness.com/coblis].
  Симуляция CVD.
- Color Oracle. --- #link("https://colororacle.org/")[colororacle.org].
  Симулятор для рабочего стола.
- Chroma.js. ---
  #link("https://gka.github.io/chroma.js/")[gka.github.io/chroma.js].
  Генератор цветовых шкал и интерполяций.
- Viz Palette. ---
  #link("https://projects.susielu.com/viz-palette")[projects.susielu.com/viz-palette].
  Проверка палитры для диаграмм.
- Coolors. --- #link("https://coolors.co/")[coolors.co]. Быстрые палитры
  (проверяйте CVD вручную).
- Adobe Color. --- #link("https://color.adobe.com/")[color.adobe.com].
  Цветовые круги и гармонии.
- Colorgorical. --- #link("http://colorgorical.com/")[colorgorical.com].
  Генератор качественных палитр с учётом различимости.

== 8.5 Типографика и шрифты
<типографика-и-шрифты>
- Bringhurst R. #emph[The Elements of Typographic Style]. 4th ed.,
  Hartley & Marks, 2012. ---
  #link("https://www.hartleyandmarks.com/")[hartleyandmarks.com]. Ритм,
  пропорции, детали набора.
- Butterick M. #emph[Practical Typography]. ---
  #link("https://practicaltypography.com/")[practicaltypography.com].
  Коротко и по делу: кегль, интерлиньяж, ширина строки.
- Lupton E. #emph[Thinking with Type]. 2nd ed., Princeton Architectural
  Press, 2010. ---
  #link("https://www.thinkingwithtype.com/")[thinkingwithtype.com].
  Типографическая система.
- Hochuli J. #emph[Detail in Typography]. 2nd ed., Niggli, 2015. ---
  #link("https://www.niggli.ch/")[niggli.ch]. Микротипографика: кернинг,
  трекинг, переносы.
- Ruder E. #emph[Typographie]. Niggli, 1967. ---
  #link("https://www.niggli.ch/")[niggli.ch]. Швейцарская школа, сетки.
- Gill E. #emph[An Essay on Typography]. Godine, 1988. ---
  #link("https://www.godine.com/book/an-essay-on-typography/")[godine.com].
  Классическое эссе о ремесле.
- Tschichold J. #emph[The Form of the Book]. Hartley & Marks, 1991. ---
  #link("https://www.oakknoll.com/")[oakknoll.com]. Книжная типографика
  и пропорции.
- Google Fonts. ---
  #link("https://fonts.google.com/")[fonts.google.com]. Свободные шрифты
  с лицензиями.
- SIL Open Font License. ---
  #link("https://openfontlicense.org/")[openfontlicense.org]. Что можно
  делать со шрифтом.
- Font Squirrel. ---
  #link("https://www.fontsquirrel.com/")[fontsquirrel.com]. Отборные
  freeware-шрифты.
- Fonts In Use. --- #link("https://fontsinuse.com/")[fontsinuse.com].
  Примеры реальных пар и контекстов.
- Inter. --- #link("https://rsms.me/inter/")[rsms.me/inter]. Нейтральный
  UI/графический шрифт.
- IBM Plex. --- #link("https://www.ibm.com/plex/")[ibm.com/plex].
  Корпоративная система с хорошей кириллицей.
- Atkinson Hyperlegible. ---
  #link("https://www.brailleinstitute.org/freefont/")[brailleinstitute.org/freefont].
  Повышенная различимость букв.
- Source Sans 3. ---
  #link("https://adobe-fonts.github.io/source-sans/")[adobe-fonts.github.io/source-sans].
  Спокойный гротеск для интерфейсов и figure labels.
- Liberation Fonts. ---
  #link("https://github.com/liberationfonts/liberation-fonts")[github.com/liberationfonts].
  Метрические аналоги Arial/Times/Courier.
- DejaVu Fonts. ---
  #link("https://dejavu-fonts.github.io/")[dejavu-fonts.github.io].
  Широкое покрытие символов.
- Fontjoy. --- #link("https://fontjoy.com/")[fontjoy.com]. Генератор пар
  шрифтов (проверяйте вручную).
- Typescale. --- #link("https://typescale.com/")[typescale.com].
  Модульная шкала кеглей.
- Utopia. --- #link("https://utopia.fyi/")[utopia.fyi]. Fluid type для
  web.
- Modular Scale. ---
  #link("https://www.modularscale.com/")[modularscale.com]. Пропорции
  типографики.

=== Таблица 8.1. Короткий список шрифтов

#table(
  columns: (1.3fr, 1.5fr, 0.8fr, 2.4fr),
  table.header(repeat: true, [*Шрифт*], [*Где уместен*], [*Лицензия*], [*Почему*]),
  [Inter], [web, UI, подписи], [OFL], [нейтральный, хорошая кириллица],
  [IBM Plex Sans], [отчёты, web], [OFL], [корпоративный, полный набор],
  [Source Sans 3], [figure labels], [OFL], [спокойный, экономичный],
  [Atkinson Hyperlegible], [доступность], [free], [различимые буквы],
  [Liberation Sans], [замена Arial], [OFL], [метрики Arial],
  [DejaVu Sans], [символы, LaTeX], [free], [широкое покрытие],
  [Noto Sans], [мультиязычность], [OFL], [много письменностей],
  [Libertinus Serif], [тело, Typst], [OFL], [книжная антиква],
  [Arial/Helvetica], [журнальный стандарт], [proprietary], [привычность, но лицензия],
)

== 8.6 Python и библиотеки
<python-и-библиотеки>
- Matplotlib. --- #link("https://matplotlib.org/")[matplotlib.org].
  Базовая графика, `savefig`, rcParams.
- Seaborn. --- #link("https://seaborn.pydata.org/")[seaborn.pydata.org].
  Статистические графики, `clustermap`, `violinplot`.
- Plotnine. ---
  #link("https://plotnine.readthedocs.io/")[plotnine.readthedocs.io].
  Grammar of graphics в Python.
- pandas. --- #link("https://pandas.pydata.org/")[pandas.pydata.org].
  Данные, группировки, пропуски.
- NumPy. --- #link("https://numpy.org/")[numpy.org]. Массивы,
  интегрирование, seed.
- SciPy. --- #link("https://scipy.org/")[scipy.org]. Статистика,
  t-интервалы, оптимизация.
- statsmodels. ---
  #link("https://www.statsmodels.org/")[statsmodels.org]. LOWESS,
  регрессия, диагностика.
- squarify. ---
  #link("https://github.com/laserson/squarify")[github.com/laserson/squarify].
  Treemap.
- adjustText. ---
  #link("https://github.com/Phlya/adjustText")[github.com/Phlya/adjustText].
  Разведение подписей.
- Pillow. --- #link("https://python-pillow.org/")[python-pillow.org].
  TIFF/PNG, компрессия.
- colour-science. ---
  #link("https://www.colour-science.org/")[colour-science.org]. Цветовые
  пространства, конверсии.
- colorspacious. ---
  #link("https://colorspacious.readthedocs.io/")[colorspacious.readthedocs.io].
  CVD-симуляция и перцептивные пространства.
- palettable. ---
  #link("https://jiffyclub.github.io/palettable/")[jiffyclub.github.io/palettable].
  ColorBrewer/Tol в Python.
- cmcrameri. ---
  #link("https://github.com/callumrollo/cmcrameri")[github.com/callumrollo/cmcrameri].
  Scientific colour maps в matplotlib.
- lifelines. ---
  #link("https://lifelines.readthedocs.io/")[lifelines.readthedocs.io].
  Kaplan--Meier, Cox, log-rank.
- scikit-learn. ---
  #link("https://scikit-learn.org/")[scikit-learn.org]. ROC/PR,
  калибровка, модели.
- SHAP. --- #link("https://shap.readthedocs.io/")[shap.readthedocs.io].
  Интерпретация моделей.
- ArviZ. --- #link("https://python.arviz.org/")[python.arviz.org].
  Байесовская диагностика.
- Plotly. --- #link("https://plotly.com/python/")[plotly.com/python].
  Интерактив и web-экспорт.
- Altair. ---
  #link("https://altair-viz.github.io/")[altair-viz.github.io].
  Vega-Lite из Python.
- Bokeh. --- #link("https://bokeh.org/")[bokeh.org]. Интерактивные
  web-графики.
- SciencePlots. ---
  #link("https://github.com/garrettj403/SciencePlots")[github.com/garrettj403/SciencePlots].
  Готовые journal-стили для matplotlib.
- brokenaxes. ---
  #link("https://github.com/bendichter/brokenaxes")[github.com/bendichter/brokenaxes].
  Разрывы оси без обмана.
- matplotlib-scalebar. ---
  #link("https://github.com/ppinard/matplotlib-scalebar")[github.com/ppinard/matplotlib-scalebar].
  Масштабные линейки для изображений.

== 8.7 Генераторы и low-code инструменты
<генераторы-и-low-code-инструменты>
- Datawrapper. --- #link("https://www.datawrapper.de/")[datawrapper.de].
  Быстрые публикационные графики и карты.
- Flourish. --- #link("https://flourish.studio/")[flourish.studio].
  Инфографика и анимация.
- RAWGraphs. --- #link("https://www.rawgraphs.io/")[rawgraphs.io]. Много
  нестандартных типов из CSV.
- Tableau Public. ---
  #link("https://public.tableau.com/")[public.tableau.com].
  Исследовательская визуализация.
- Observable. --- #link("https://observablehq.com/")[observablehq.com].
  Notebooks и D3/Plot.
- Vega-Lite. ---
  #link("https://vega.github.io/vega-lite/")[vega.github.io/vega-lite].
  Декларативная грамматика.
- D3. --- #link("https://d3js.org/")[d3js.org]. Полный контроль, высокая
  цена.
- Chart.js. --- #link("https://www.chartjs.org/")[chartjs.org]. Простые
  web-графики.
- ggplot2. ---
  #link("https://ggplot2.tidyverse.org/")[ggplot2.tidyverse.org]. Эталон
  grammar of graphics.
- R Graph Gallery. ---
  #link("https://r-graph-gallery.com/")[r-graph-gallery.com]. Рецепты на
  R.
- Python Graph Gallery. ---
  #link("https://python-graph-gallery.com/")[python-graph-gallery.com].
  Рецепты на Python.
- From Data to Viz. ---
  #link("https://www.data-to-viz.com/")[data-to-viz.com]. Дерево выбора
  графика.
- FT Visual Vocabulary. ---
  #link("https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary")[github.com/Financial-Times/chart-doctor].
  «Какая задача --- какой график».
- Data Viz Project. ---
  #link("https://datavizproject.com/")[datavizproject.com]. Каталог
  форм.
- Quarto. --- #link("https://quarto.org/")[quarto.org]. Документы и
  отчёты из кода.
- Typst. --- #link("https://typst.app/")[typst.app]. Вёрстка этой
  методички.
- PGFPlots. ---
  #link("https://pgfplots.sourceforge.net/")[pgfplots.sourceforge.net].
  Графики внутри LaTeX.

=== Таблица 8.2. Инструменты по задачам

#table(
  columns: (1.5fr, 1.1fr, 3.4fr),
  table.header(repeat: true, [*Инструмент*], [*Тип*], [*Зачем*]),
  [Datawrapper], [online], [быстрый график для публикации],
  [Flourish], [online], [инфографика и анимация],
  [RAWGraphs], [online], [нестандартные типы из CSV],
  [Observable Plot], [JS], [лаконичные web-графики],
  [Vega-Lite], [JS], [декларативные спецификации],
  [SciencePlots], [Python], [journal-стили matplotlib],
  [ColorBrewer], [palette], [проверенные шкалы],
  [Viz Palette], [palette], [проверка палитры],
  [From Data to Viz], [guide], [выбор формы],
  [Quarto], [docs], [отчёты и воспроизводимость],
)

== 8.8 Публикация, экспорт, вектор
<публикация-экспорт-вектор>
- Nature Portfolio. Final submission guidelines --- figures. ---
  #link("https://www.nature.com/nature-portfolio/editorial-policies/figures")[nature.com].
- Elsevier. Artwork and media instructions. ---
  #link("https://www.elsevier.com/researcher/author/tools-and-resources/artwork-guidelines")[elsevier.com].
- IEEE. Author guidelines --- graphics. ---
  #link("https://journals.ieeeauthorcenter.ieee.org/")[journals.ieeeauthorcenter.ieee.org].
- ICMJE. Recommendations for the Conduct, Reporting, Editing, and
  Publication of Scholarly Work. ---
  #link("https://www.icmje.org/recommendations/")[icmje.org].
- EQUATOR Network. ---
  #link("https://www.equator-network.org/")[equator-network.org].
  Reporting guidelines.
- Inkscape. --- #link("https://inkscape.org/")[inkscape.org]. Векторная
  правка SVG/PDF.
- Adobe Illustrator. ---
  #link("https://www.adobe.com/products/illustrator.html")[adobe.com].
  CMYK, bleed, финальная правка.
- Affinity Designer. ---
  #link("https://affinity.serif.com/")[affinity.serif.com]. Альтернатива
  Illustrator.
- Scribus. --- #link("https://www.scribus.net/")[scribus.net]. Открытая
  вёрстка.
- ImageMagick. --- #link("https://imagemagick.org/")[imagemagick.org].
  Пакетная обработка растров.
- Ghostscript. ---
  #link("https://www.ghostscript.com/")[ghostscript.com]. PDF/PS,
  цветовые профили.
- qpdf. --- #link("https://qpdf.sourceforge.io/")[qpdf.sourceforge.io].
  Проверка/починка PDF.
- veraPDF. --- #link("https://verapdf.org/")[verapdf.org]. Валидация
  PDF/A.
- ExifTool. --- #link("https://exiftool.org/")[exiftool.org]. Метаданные
  изображений.
- Poppler `pdffonts`. ---
  #link("https://poppler.freedesktop.org/")[poppler.freedesktop.org].
  Проверка встроенных шрифтов.
- SVGO. --- #link("https://github.com/svg/svgo")[github.com/svg/svgo].
  Оптимизация SVG.
- SVGOMG. ---
  #link("https://jakearchibald.github.io/svgomg/")[jakearchibald.github.io/svgomg].
  Визуальная оптимизация SVG.

== 8.9 Web-графика
<web-графика>
- MDN. Responsive images. ---
  #link("https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images")[developer.mozilla.org].
  `srcset`, `sizes`, `<picture>`.
- MDN. `<img>`. ---
  #link("https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img")[developer.mozilla.org].
  `alt`, `width`, `height`, `loading`.
- web.dev. Learn Images. ---
  #link("https://web.dev/learn/images/")[web.dev/learn/images]. Форматы,
  сжатие, responsive.
- Can I use. --- #link("https://caniuse.com/")[caniuse.com]. Поддержка
  WebP/AVIF/SVG.
- WCAG Quick Reference. ---
  #link("https://www.w3.org/WAI/WCAG22/quickref/")[w3.org/WAI/WCAG22/quickref].
  Контраст и доступность.
- MDN. `prefers-color-scheme`. ---
  #link("https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme")[developer.mozilla.org].
  Тёмная тема.
- Squoosh. --- #link("https://squoosh.app/")[squoosh.app]. Сжатие
  изображений.
- ImageOptim. --- #link("https://imageoptim.com/")[imageoptim.com].
  Оптимизация PNG/JPEG.
- Lighthouse. ---
  #link("https://developer.chrome.com/docs/lighthouse/overview/")[developer.chrome.com].
  Производительность и доступность.
- axe. --- #link("https://www.deque.com/axe/")[deque.com/axe].
  Автоматическая проверка доступности.

== 8.10 Воспроизводимость и инфраструктура
<воспроизводимость-и-инфраструктура>
- The Turing Way. ---
  #link("https://the-turing-way.netlify.app/")[the-turing-way.netlify.app].
  Практики воспроизводимой науки.
- uv. --- #link("https://docs.astral.sh/uv/")[docs.astral.sh/uv].
  Окружение и lock-файл.
- Git. --- #link("https://git-scm.com/")[git-scm.com]. История и ревью.
- DVC. --- #link("https://dvc.org/")[dvc.org]. Версии данных и моделей.
- Zenodo. --- #link("https://zenodo.org/")[zenodo.org]. DOI для
  данных/кода.
- Jupyter. --- #link("https://jupyter.org/")[jupyter.org]. Ноутбуки и
  исследование.
- Quarto. --- #link("https://quarto.org/")[quarto.org]. Воспроизводимые
  документы.
- GNU Make. ---
  #link("https://www.gnu.org/software/make/")[gnu.org/software/make].
  Пайплайн «данные → рисунки → PDF».
- pytest. --- #link("https://docs.pytest.org/")[docs.pytest.org]. Тесты
  для кода и данных.
- Ruff. --- #link("https://docs.astral.sh/ruff/")[docs.astral.sh/ruff].
  Линтер и форматтер.
- pre-commit. --- #link("https://pre-commit.com/")[pre-commit.com]. Хуки
  перед коммитом.
- Docker. --- #link("https://docs.docker.com/")[docs.docker.com].
  Воспроизводимая среда.

== 8.11 Отчётные стандарты
<отчётные-стандарты>
- CONSORT. ---
  #link("http://www.consort-statement.org/")[consort-statement.org].
  РКИ.
- STROBE. ---
  #link("https://www.strobe-statement.org/")[strobe-statement.org].
  Наблюдательные исследования.
- PRISMA. ---
  #link("https://www.prisma-statement.org/")[prisma-statement.org].
  Систематические обзоры.
- SAMPL. ---
  #link("https://www.equator-network.org/reporting-guidelines/sampl/")[equator-network.org].
  Представление данных.
- TRIPOD. ---
  #link("https://www.tripod-statement.org/")[tripod-statement.org].
  Прогностические модели.
- PROBAST. --- #link("https://www.probast.org/")[probast.org]. Риск
  смещения моделей.
- ICMJE. --- #link("https://www.icmje.org/recommendations/")[icmje.org].
  Единые требования к рукописям.

== 8.12 Что не считать источником
<что-не-считать-источником>
- скриншоты чужих графиков без контекста;
- блоги без данных и методов;
- «красивые» галереи без проверки доступности;
- AI-ответы без первоисточника;
- устаревшие требования журнала;
- код без версии и лицензии.

Источник --- это то, что можно проверить, датировать и процитировать.

== 8.13 Куда идти дальше
<куда-идти-дальше>
- #strong[Выбор формы:] Wilke → From Data to Viz → раздел 5.
- #strong[Статистика:] Cumming → Harrell/Steyerberg → раздел 6.
- #strong[Цвет:] Okabe--Ito → ColorBrewer → WCAG.
- #strong[Типографика:] Bringhurst → Practical Typography → шрифты.
- #strong[Публикация:] guidelines журнала → раздел 7 → препресс.
- #strong[Воспроизводимость:] The Turing Way → uv/Git/Make.

== 8.14 Как цитировать эту методичку
<как-цитировать-эту-методичку>
#quote(block: true)[
GoodGraph. Методичка по научной графике на Python. Версия 0.1, 2026.
Репозиторий: `GoodGraph`\; сборка: `build/metodichka.pdf`.
]

Для ссылки на конкретный раздел указывайте номер и версию: например,
«раздел 5.14, версия 0.1».