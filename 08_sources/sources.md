# 8. Источники

Источники ниже — не «список литературы для галочки», а карта: что
читать, чем пользоваться и где проверять требования. Часть источников
довольно далёкая от Python — типографика, шрифты, генераторы диаграмм,
инструменты экспорта — но именно они определяют, будет ли рисунок
выглядеть профессионально.

## 8.1 Как пользоваться списком

1. **Сначала первоисточник.** Для требований журнала — `author
   guidelines`, для статистики — статья/учебник, для инструмента —
   официальная документация.
2. **Потом обзор.** Книги и руководства помогают выбрать метод,
   но не заменяют проверку актуальных требований.
3. **Ссылки стареют.** Проверяйте дату доступа и версию; для ПО
   указывайте версию в методах.
4. **Не цитируйте блог вместо стандарта.** Блог может объяснять,
   но не должен быть единственным основанием для норматива.

## 8.2 Визуализация и восприятие

- Tufte E. R. *The Visual Display of Quantitative Information*.
  Graphics Press, 1983. — [edwardtufte.com](https://www.edwardtufte.com/tufte/books_vdqi).
  Классика про «чернила», пропорции и графическую честность.
- Tufte E. R. *Envisioning Information*. Graphics Press, 1990. —
  [edwardtufte.com](https://www.edwardtufte.com/tufte/books_ei).
  Плотность, слои, малые кратные.
- Wilke C. O. *Fundamentals of Data Visualization*. O'Reilly, 2019. —
  [clauswilke.com/dataviz](https://clauswilke.com/dataviz/).
  Лучший современный учебник по выбору формы.
- Cairo A. *The Truthful Art*. New Riders, 2016. —
  [thefunctionalart.com](https://www.thefunctionalart.com/).
  Честность, неопределённость, дизайн.
- Munzner T. *Visualization Analysis and Design*. CRC Press, 2014. —
  [cs.ubc.ca](https://www.cs.ubc.ca/~tmm/vadbook/).
  Формальная рамка «данные — задачи — кодирование».
- Ware C. *Information Visualization: Perception for Design*.
  4th ed., Morgan Kaufmann, 2020. —
  [elsevier.com](https://www.elsevier.com/books/information-visualization/ware/978-0-12-812875-6).
  Почему глаз видит одно, а не другое.
- Cleveland W. S., McGill R. Graphical Perception // *JASA*. 1984. —
  [doi:10.1080/01621459.1984.10478080](https://doi.org/10.1080/01621459.1984.10478080).
  Экспериментальная база «положение лучше длины, длины лучше угла».
- Few S. *Show Me the Numbers*. Analytics Press, 2012. —
  [perceptualedge.com](https://www.perceptualedge.com/).
  Деловая графика и таблицы.
- Kirk A. *Data Visualisation: A Handbook for Data Driven Design*.
  SAGE, 2019. — [visualisingdata.com](https://www.visualisingdata.com/).
  Процесс дизайна, а не только код.
- Schwabish J. *Better Data Visualizations*. Columbia UP, 2021. —
  [policyviz.com](https://policyviz.com/books/).
  Практические паттерны для отчётов и статей.
- Knaflic C. N. *Storytelling with Data*. Wiley, 2015. —
  [storytellingwithdata.com](https://www.storytellingwithdata.com/books).
  Контекст, нарратив, презентация.
- Bergstrom C. T., West J. D. *Calling Bullshit*. Random House, 2020. —
  [callingbullshit.org](https://callingbullshit.org/).
  Как не обмануться графиком и статистикой.

## 8.3 Статистическая графика и отчёты

- Weissgerber T. L. et al. Beyond Bar and Line Graphs // *PLoS Biology*.
  2015. — [doi:10.1371/journal.pbio.1002128](https://doi.org/10.1371/journal.pbio.1002128).
  Почему точки и распределения лучше столбцов.
- Cumming G. *Understanding the New Statistics*. Routledge, 2012. —
  [routledge.com](https://www.routledge.com/Understanding-the-New-Statistics-Effect-Sizes-Confidence-Intervals-and-Meta-Analysis/Cumming/p/book/9780415879682).
  Эффекты, CI, мета-анализ.
- Bland J. M., Altman D. G. Statistical Methods for Assessing Agreement //
  *The Lancet*. 1986. —
  [doi:10.1016/S0140-6736(86)90837-8](https://doi.org/10.1016/S0140-6736(86)90837-8).
  Bland–Altman.
- Fawcett T. An Introduction to ROC Analysis // *Pattern Recognition
  Letters*. 2006. —
  [doi:10.1016/j.patrec.2005.10.010](https://doi.org/10.1016/j.patrec.2005.10.010).
  ROC, AUC, пороги.
- Saito T., Rehmsmeier M. The Precision-Recall Plot Is More Informative
  than the ROC Plot // *PLoS ONE*. 2015. —
  [doi:10.1371/journal.pone.0118432](https://doi.org/10.1371/journal.pone.0118432).
  Редкие исходы.
- Van Calster B. et al. Calibration: the Achilles Heel of Predictive
  Analytics // *BMC Medicine*. 2019. —
  [doi:10.1186/s12916-019-1466-7](https://doi.org/10.1186/s12916-019-1466-7).
  Калибровка прогноза.
- Steyerberg E. W. *Clinical Prediction Models*. 2nd ed., Springer, 2019. —
  [springer.com](https://link.springer.com/book/10.1007/978-3-030-16399-0).
  Прогностические модели, валидация, калибровка.
- Harrell F. E. *Regression Modeling Strategies*. 2nd ed., Springer, 2015. —
  [hbiostat.org](https://hbiostat.org/rmsc/).
  Регрессия, номограммы, оценка моделей.
- Kaplan E. L., Meier P. Nonparametric Estimation from Incomplete
  Observations // *JASA*. 1958. —
  [doi:10.1080/01621459.1958.10501452](https://doi.org/10.1080/01621459.1958.10501452).
  KM-оценка.
- Fine J. P., Gray R. J. A Proportional Hazards Model for the
  Subdistribution of a Competing Risk // *JASA*. 1999. —
  [doi:10.1080/01621459.1999.10474144](https://doi.org/10.1080/01621459.1999.10474144).
  Конкурирующие риски.
- Cochrane Handbook for Systematic Reviews of Interventions. —
  [training.cochrane.org](https://training.cochrane.org/handbook).
  Мета-анализ, forest/funnel, гетерогенность.
- Spiegelhalter D. *The Art of Statistics*. Pelican, 2019. —
  [penguin.co.uk](https://www.penguin.co.uk/books/294857/the-art-of-statistics-by-spiegelhalter-david/9780241258767).
  Как думать о данных, а не только рисовать.

## 8.4 Цвет, доступность, восприятие

- Okabe M., Ito K. Color Universal Design (CUD). 2008. —
  [jfly.uni-koeln.de/color](https://jfly.uni-koeln.de/color/).
  Палитра, различимая при CVD.
- ColorBrewer 2.0. — [colorbrewer2.org](https://colorbrewer2.org/).
  Качественные, последовательные, дивергентные шкалы.
- Tol P. Colour Schemes. — [personal.sron.nl/~pault](https://personal.sron.nl/~pault/).
  Наборы bright/muted, проверенные на различимость.
- Smith N., van der Walt S. Viridis. —
  [bids.github.io/colormap](https://bids.github.io/colormap/).
  Воспринимательно равномерная шкала.
- Crameri F. Scientific Colour Maps. —
  [fabiocrameri.ch/colourmaps](https://www.fabiocrameri.ch/colourmaps/).
  Научные палитры, включая CVD-безопасные.
- W3C. Web Content Accessibility Guidelines (WCAG) 2.2. —
  [w3.org/TR/WCAG22](https://www.w3.org/TR/WCAG22/).
  Контраст, не-цветовые подсказки.
- WebAIM Contrast Checker. —
  [webaim.org/resources/contrastchecker](https://webaim.org/resources/contrastchecker/).
  Быстрая проверка контраста.
- Coblis Color Blindness Simulator. —
  [color-blindness.com/coblis](https://www.color-blindness.com/coblis-color-blindness-simulator/).
  Симуляция CVD.
- Color Oracle. — [colororacle.org](https://colororacle.org/).
  Симулятор для рабочего стола.
- Chroma.js. — [gka.github.io/chroma.js](https://gka.github.io/chroma.js/).
  Генератор цветовых шкал и интерполяций.
- Viz Palette. — [projects.susielu.com/viz-palette](https://projects.susielu.com/viz-palette).
  Проверка палитры для диаграмм.
- Coolors. — [coolors.co](https://coolors.co/).
  Быстрые палитры (проверяйте CVD вручную).
- Adobe Color. — [color.adobe.com](https://color.adobe.com/).
  Цветовые круги и гармонии.
- Colorgorical. — [colorgorical.com](http://colorgorical.com/).
  Генератор качественных палитр с учётом различимости.

## 8.5 Типографика и шрифты

- Bringhurst R. *The Elements of Typographic Style*. 4th ed.,
  Hartley & Marks, 2012. —
  [hartleyandmarks.com](https://www.hartleyandmarks.com/).
  Ритм, пропорции, детали набора.
- Butterick M. *Practical Typography*. —
  [practicaltypography.com](https://practicaltypography.com/).
  Коротко и по делу: кегль, интерлиньяж, ширина строки.
- Lupton E. *Thinking with Type*. 2nd ed., Princeton Architectural
  Press, 2010. — [thinkingwithtype.com](https://www.thinkingwithtype.com/).
  Типографическая система.
- Hochuli J. *Detail in Typography*. 2nd ed., Niggli, 2015. —
  [niggli.ch](https://www.niggli.ch/).
  Микротипографика: кернинг, трекинг, переносы.
- Ruder E. *Typographie*. Niggli, 1967. —
  [niggli.ch](https://www.niggli.ch/).
  Швейцарская школа, сетки.
- Gill E. *An Essay on Typography*. Godine, 1988. —
  [godine.com](https://www.godine.com/book/an-essay-on-typography/).
  Классическое эссе о ремесле.
- Tschichold J. *The Form of the Book*. Hartley & Marks, 1991. —
  [oakknoll.com](https://www.oakknoll.com/).
  Книжная типографика и пропорции.
- Google Fonts. — [fonts.google.com](https://fonts.google.com/).
  Свободные шрифты с лицензиями.
- SIL Open Font License. — [openfontlicense.org](https://openfontlicense.org/).
  Что можно делать со шрифтом.
- Font Squirrel. — [fontsquirrel.com](https://www.fontsquirrel.com/).
  Отборные freeware-шрифты.
- Fonts In Use. — [fontsinuse.com](https://fontsinuse.com/).
  Примеры реальных пар и контекстов.
- Inter. — [rsms.me/inter](https://rsms.me/inter/).
  Нейтральный UI/графический шрифт.
- IBM Plex. — [ibm.com/plex](https://www.ibm.com/plex/).
  Корпоративная система с хорошей кириллицей.
- Atkinson Hyperlegible. —
  [brailleinstitute.org/freefont](https://www.brailleinstitute.org/freefont/).
  Повышенная различимость букв.
- Source Sans 3. — [adobe-fonts.github.io/source-sans](https://adobe-fonts.github.io/source-sans/).
  Спокойный гротеск для интерфейсов и figure labels.
- Liberation Fonts. —
  [github.com/liberationfonts](https://github.com/liberationfonts/liberation-fonts).
  Метрические аналоги Arial/Times/Courier.
- DejaVu Fonts. — [dejavu-fonts.github.io](https://dejavu-fonts.github.io/).
  Широкое покрытие символов.
- Fontjoy. — [fontjoy.com](https://fontjoy.com/).
  Генератор пар шрифтов (проверяйте вручную).
- Typescale. — [typescale.com](https://typescale.com/).
  Модульная шкала кеглей.
- Utopia. — [utopia.fyi](https://utopia.fyi/).
  Fluid type для web.
- Modular Scale. — [modularscale.com](https://www.modularscale.com/).
  Пропорции типографики.

### Таблица 8.1. Короткий список шрифтов

| Шрифт | Где уместен | Лицензия | Почему |
|---|---|---|---|
| Inter | web, UI, подписи | OFL | нейтральный, хорошая кириллица |
| IBM Plex Sans | отчёты, web | OFL | корпоративный, полный набор |
| Source Sans 3 | figure labels | OFL | спокойный, экономичный |
| Atkinson Hyperlegible | доступность | free | различимые буквы |
| Liberation Sans | замена Arial | OFL | метрики Arial |
| DejaVu Sans | символы, LaTeX | free | широкое покрытие |
| Noto Sans | мультиязычность | OFL | много письменностей |
| Libertinus Serif | тело, Typst | OFL | книжная антиква |
| Arial/Helvetica | журнальный стандарт | proprietary | привычность, но лицензия |

## 8.6 Python и библиотеки

- Matplotlib. — [matplotlib.org](https://matplotlib.org/).
  Базовая графика, `savefig`, rcParams.
- Seaborn. — [seaborn.pydata.org](https://seaborn.pydata.org/).
  Статистические графики, `clustermap`, `violinplot`.
- Plotnine. — [plotnine.readthedocs.io](https://plotnine.readthedocs.io/).
  Grammar of graphics в Python.
- pandas. — [pandas.pydata.org](https://pandas.pydata.org/).
  Данные, группировки, пропуски.
- NumPy. — [numpy.org](https://numpy.org/).
  Массивы, интегрирование, seed.
- SciPy. — [scipy.org](https://scipy.org/).
  Статистика, t-интервалы, оптимизация.
- statsmodels. — [statsmodels.org](https://www.statsmodels.org/).
  LOWESS, регрессия, диагностика.
- squarify. — [github.com/laserson/squarify](https://github.com/laserson/squarify).
  Treemap.
- adjustText. — [github.com/Phlya/adjustText](https://github.com/Phlya/adjustText).
  Разведение подписей.
- Pillow. — [python-pillow.org](https://python-pillow.org/).
  TIFF/PNG, компрессия.
- colour-science. — [colour-science.org](https://www.colour-science.org/).
  Цветовые пространства, конверсии.
- colorspacious. — [colorspacious.readthedocs.io](https://colorspacious.readthedocs.io/).
  CVD-симуляция и перцептивные пространства.
- palettable. — [jiffyclub.github.io/palettable](https://jiffyclub.github.io/palettable/).
  ColorBrewer/Tol в Python.
- cmcrameri. — [github.com/callumrollo/cmcrameri](https://github.com/callumrollo/cmcrameri).
  Scientific colour maps в matplotlib.
- lifelines. — [lifelines.readthedocs.io](https://lifelines.readthedocs.io/).
  Kaplan–Meier, Cox, log-rank.
- scikit-learn. — [scikit-learn.org](https://scikit-learn.org/).
  ROC/PR, калибровка, модели.
- SHAP. — [shap.readthedocs.io](https://shap.readthedocs.io/).
  Интерпретация моделей.
- ArviZ. — [python.arviz.org](https://python.arviz.org/).
  Байесовская диагностика.
- Plotly. — [plotly.com/python](https://plotly.com/python/).
  Интерактив и web-экспорт.
- Altair. — [altair-viz.github.io](https://altair-viz.github.io/).
  Vega-Lite из Python.
- Bokeh. — [bokeh.org](https://bokeh.org/).
  Интерактивные web-графики.
- SciencePlots. — [github.com/garrettj403/SciencePlots](https://github.com/garrettj403/SciencePlots).
  Готовые journal-стили для matplotlib.
- brokenaxes. — [github.com/bendichter/brokenaxes](https://github.com/bendichter/brokenaxes).
  Разрывы оси без обмана.
- matplotlib-scalebar. — [github.com/ppinard/matplotlib-scalebar](https://github.com/ppinard/matplotlib-scalebar).
  Масштабные линейки для изображений.

## 8.7 Генераторы и low-code инструменты

- Datawrapper. — [datawrapper.de](https://www.datawrapper.de/).
  Быстрые публикационные графики и карты.
- Flourish. — [flourish.studio](https://flourish.studio/).
  Инфографика и анимация.
- RAWGraphs. — [rawgraphs.io](https://www.rawgraphs.io/).
  Много нестандартных типов из CSV.
- Tableau Public. — [public.tableau.com](https://public.tableau.com/).
  Исследовательская визуализация.
- Observable. — [observablehq.com](https://observablehq.com/).
  Notebooks и D3/Plot.
- Vega-Lite. — [vega.github.io/vega-lite](https://vega.github.io/vega-lite/).
  Декларативная грамматика.
- D3. — [d3js.org](https://d3js.org/).
  Полный контроль, высокая цена.
- Chart.js. — [chartjs.org](https://www.chartjs.org/).
  Простые web-графики.
- ggplot2. — [ggplot2.tidyverse.org](https://ggplot2.tidyverse.org/).
  Эталон grammar of graphics.
- R Graph Gallery. — [r-graph-gallery.com](https://r-graph-gallery.com/).
  Рецепты на R.
- Python Graph Gallery. — [python-graph-gallery.com](https://python-graph-gallery.com/).
  Рецепты на Python.
- From Data to Viz. — [data-to-viz.com](https://www.data-to-viz.com/).
  Дерево выбора графика.
- FT Visual Vocabulary. —
  [github.com/Financial-Times/chart-doctor](https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary).
  «Какая задача — какой график».
- Data Viz Project. — [datavizproject.com](https://datavizproject.com/).
  Каталог форм.
- Quarto. — [quarto.org](https://quarto.org/).
  Документы и отчёты из кода.
- Typst. — [typst.app](https://typst.app/).
  Вёрстка этой методички.
- PGFPlots. — [pgfplots.sourceforge.net](https://pgfplots.sourceforge.net/).
  Графики внутри LaTeX.

### Таблица 8.2. Инструменты по задачам

| Инструмент | Тип | Зачем |
|---|---|---|
| Datawrapper | online | быстрый график для публикации |
| Flourish | online | инфографика и анимация |
| RAWGraphs | online | нестандартные типы из CSV |
| Observable Plot | JS | лаконичные web-графики |
| Vega-Lite | JS | декларативные спецификации |
| SciencePlots | Python | journal-стили matplotlib |
| ColorBrewer | palette | проверенные шкалы |
| Viz Palette | palette | проверка палитры |
| From Data to Viz | guide | выбор формы |
| Quarto | docs | отчёты и воспроизводимость |

## 8.8 Публикация, экспорт, вектор

- Nature Portfolio. Final submission guidelines — figures. —
  [nature.com](https://www.nature.com/nature-portfolio/editorial-policies/figures).
- Elsevier. Artwork and media instructions. —
  [elsevier.com](https://www.elsevier.com/researcher/author/tools-and-resources/artwork-guidelines).
- IEEE. Author guidelines — graphics. —
  [journals.ieeeauthorcenter.ieee.org](https://journals.ieeeauthorcenter.ieee.org/).
- ICMJE. Recommendations for the Conduct, Reporting, Editing, and
  Publication of Scholarly Work. —
  [icmje.org](https://www.icmje.org/recommendations/).
- EQUATOR Network. —
  [equator-network.org](https://www.equator-network.org/).
  Reporting guidelines.
- Inkscape. — [inkscape.org](https://inkscape.org/).
  Векторная правка SVG/PDF.
- Adobe Illustrator. —
  [adobe.com](https://www.adobe.com/products/illustrator.html).
  CMYK, bleed, финальная правка.
- Affinity Designer. —
  [affinity.serif.com](https://affinity.serif.com/).
  Альтернатива Illustrator.
- Scribus. — [scribus.net](https://www.scribus.net/).
  Открытая вёрстка.
- ImageMagick. — [imagemagick.org](https://imagemagick.org/).
  Пакетная обработка растров.
- Ghostscript. — [ghostscript.com](https://www.ghostscript.com/).
  PDF/PS, цветовые профили.
- qpdf. — [qpdf.sourceforge.io](https://qpdf.sourceforge.io/).
  Проверка/починка PDF.
- veraPDF. — [verapdf.org](https://verapdf.org/).
  Валидация PDF/A.
- ExifTool. — [exiftool.org](https://exiftool.org/).
  Метаданные изображений.
- Poppler `pdffonts`. —
  [poppler.freedesktop.org](https://poppler.freedesktop.org/).
  Проверка встроенных шрифтов.
- SVGO. — [github.com/svg/svgo](https://github.com/svg/svgo).
  Оптимизация SVG.
- SVGOMG. — [jakearchibald.github.io/svgomg](https://jakearchibald.github.io/svgomg/).
  Визуальная оптимизация SVG.

## 8.9 Web-графика

- MDN. Responsive images. —
  [developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images).
  `srcset`, `sizes`, `<picture>`.
- MDN. `<img>`. —
  [developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img).
  `alt`, `width`, `height`, `loading`.
- web.dev. Learn Images. —
  [web.dev/learn/images](https://web.dev/learn/images/).
  Форматы, сжатие, responsive.
- Can I use. — [caniuse.com](https://caniuse.com/).
  Поддержка WebP/AVIF/SVG.
- WCAG Quick Reference. —
  [w3.org/WAI/WCAG22/quickref](https://www.w3.org/WAI/WCAG22/quickref/).
  Контраст и доступность.
- MDN. `prefers-color-scheme`. —
  [developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme).
  Тёмная тема.
- Squoosh. — [squoosh.app](https://squoosh.app/).
  Сжатие изображений.
- ImageOptim. — [imageoptim.com](https://imageoptim.com/).
  Оптимизация PNG/JPEG.
- Lighthouse. —
  [developer.chrome.com](https://developer.chrome.com/docs/lighthouse/overview/).
  Производительность и доступность.
- axe. — [deque.com/axe](https://www.deque.com/axe/).
  Автоматическая проверка доступности.

## 8.10 Воспроизводимость и инфраструктура

- The Turing Way. —
  [the-turing-way.netlify.app](https://the-turing-way.netlify.app/).
  Практики воспроизводимой науки.
- uv. — [docs.astral.sh/uv](https://docs.astral.sh/uv/).
  Окружение и lock-файл.
- Git. — [git-scm.com](https://git-scm.com/).
  История и ревью.
- DVC. — [dvc.org](https://dvc.org/).
  Версии данных и моделей.
- Zenodo. — [zenodo.org](https://zenodo.org/).
  DOI для данных/кода.
- Jupyter. — [jupyter.org](https://jupyter.org/).
  Ноутбуки и исследование.
- Quarto. — [quarto.org](https://quarto.org/).
  Воспроизводимые документы.
- GNU Make. — [gnu.org/software/make](https://www.gnu.org/software/make/).
  Пайплайн «данные → рисунки → PDF».
- pytest. — [docs.pytest.org](https://docs.pytest.org/).
  Тесты для кода и данных.
- Ruff. — [docs.astral.sh/ruff](https://docs.astral.sh/ruff/).
  Линтер и форматтер.
- pre-commit. — [pre-commit.com](https://pre-commit.com/).
  Хуки перед коммитом.
- Docker. — [docs.docker.com](https://docs.docker.com/).
  Воспроизводимая среда.

## 8.11 Отчётные стандарты

- CONSORT. — [consort-statement.org](http://www.consort-statement.org/).
  РКИ.
- STROBE. — [strobe-statement.org](https://www.strobe-statement.org/).
  Наблюдательные исследования.
- PRISMA. — [prisma-statement.org](https://www.prisma-statement.org/).
  Систематические обзоры.
- SAMPL. — [equator-network.org](https://www.equator-network.org/reporting-guidelines/sampl/).
  Представление данных.
- TRIPOD. — [tripod-statement.org](https://www.tripod-statement.org/).
  Прогностические модели.
- PROBAST. — [probast.org](https://www.probast.org/).
  Риск смещения моделей.
- ICMJE. — [icmje.org](https://www.icmje.org/recommendations/).
  Единые требования к рукописям.

## 8.12 Что не считать источником

- скриншоты чужих графиков без контекста;
- блоги без данных и методов;
- «красивые» галереи без проверки доступности;
- AI-ответы без первоисточника;
- устаревшие требования журнала;
- код без версии и лицензии.

Источник — это то, что можно проверить, датировать и процитировать.

## 8.13 Куда идти дальше

- **Выбор формы:** Wilke → From Data to Viz → раздел 5.
- **Статистика:** Cumming → Harrell/Steyerberg → раздел 6.
- **Цвет:** Okabe–Ito → ColorBrewer → WCAG.
- **Типографика:** Bringhurst → Practical Typography → шрифты.
- **Публикация:** guidelines журнала → раздел 7 → препресс.
- **Воспроизводимость:** The Turing Way → uv/Git/Make.

## 8.14 Как цитировать эту методичку

> GoodGraph. Методичка по научной графике на Python. Версия 0.1,
> 2026. Репозиторий: `GoodGraph`; сборка: `build/metodichka.pdf`.

Для ссылки на конкретный раздел указывайте номер и версию: например,
«раздел 5.14, версия 0.1».
