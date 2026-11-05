// Раздел 5.18. Paired dot: индивидуальные изменения.
// Сборка: typst compile --root . 05_charts/18_paired_dot/paired_dot.typ build/05_18_paired_dot.pdf

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
#set table(stroke: 0.5pt + luma(190), inset: (x: 5pt, y: 4pt))
#show table: set text(size: 9pt)
#show raw: set text(font: "DejaVu Sans Mono", size: 8.2pt)
#show raw.where(block: true): it => block(fill: luma(247), inset: 8pt, radius: 2pt, width: 100%, stroke: 0.5pt + luma(220), breakable: false, it)

#heading(level: 1)[5.18 Paired dot: индивидуальные изменения]

Paired dot — это линии, соединяющие два измерения одного и того же
пациента: «до» и «после». В отличие от slope plot средних, здесь
виден *каждый* пациент: у кого эффект большой, у кого маленький,
у кого его нет.

График хорош для 10–50 пар. При сотнях пар линии превращаются
в spaghetti; тогда нужны средние/CI или распределение разниц.

#heading(level: 2)[5.18.1 Сфера применения]

Paired dot отвечает на вопрос: *как изменился показатель у каждого
пациента и каково среднее изменение?*

Где это пригодится:

- до/после лечения в одной группе;
- парные измерения биомаркера;
- индивидуальный ответ на вмешательство;
- проверка, не скрывает ли среднее разнородность;
- малые выборки, где важна каждая пара.

Когда paired dot *не* нужен:

- наблюдения непарные;
- пар слишком много (spaghetti);
- нужны только средние — slope/dot+CI;
- нужна динамика многих точек — line;
- нужно распределение — histogram/ECDF.

#heading(level: 2)[5.18.2 Данные]

Сценарий: 30 пациентов, гемоглобин (г/л) до и через 8 недель лечения
анемии. Парные наблюдения.

#table(
  columns: (1.6fr, 2.6fr, 1.2fr),
  table.header([*Колонка*], [*Смысл*], [*Единица*]),
  [`patient_id`], [идентификатор пациента], [—],
  [`hemoglobin_before`], [гемоглобин до], [г/л],
  [`hemoglobin_after`], [гемоглобин после], [г/л],
)

Среднее до — 93,4 г/л; после — 105,8 г/л; средний прирост —
+12,4 ± 5,8 г/л. У всех 30 пациентов уровень вырос, но величина
прироста различается.

Генератор: `05_charts/18_paired_dot/scripts/make_data.py` → `data/18_dataset.csv`.

#heading(level: 2)[5.18.3 Плохой график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_18_bad_paired_dot.png", width: 84%)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.18.1. Плохой paired dot: 30 радужных линий без точек
    и средних, обрезанная ось 85–115.
  ]]
]

Код: `05_charts/18_paired_dot/scripts/bad_plot.py`.

Что не так:

+ *30 радужных линий.* Непонятно, где отдельный пациент;
  цвет не помогает.
+ *Нет точек и средних.* Видны только линии, нет сводки.
+ *Ось Y обрезана до 85–115.* Высокие значения после лечения
  скрыты.
+ *Тяжёлая сетка, полная рамка.*
+ *Заголовок «Гемоглобин до и после».* Не сообщает вывод.
+ *Нет единиц, n и среднего изменения.*

#heading(level: 2)[5.18.4 Правильный график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_18_good_paired_dot.png", width: 85mm)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.18.2. Правильный paired dot: серые линии, точки,
    среднее изменение +12,4 г/л, полный диапазон.
  ]]
]

Код: `05_charts/18_paired_dot/scripts/good_plot.py`.

Что изменилось:

+ *Серые линии для отдельных пациентов.* Видна каждая пара,
  но линии не конкурируют.
+ *Точки на обоих концах.* Видны исходные значения и выбросы.
+ *Среднее до/после — цветная толстая линия.*
  Подписано «среднее +12,4 г/л».
+ *Полный диапазон 70–145 г/л.*
+ *«До/После», единицы, n = 30.*
+ *Заголовок-вывод, 85 мм.*

Paired dot показывает индивидуальную изменчивость, но не
статистическую значимость. Для вывода нужен парный тест
(Уилкоксон/парный t) и CI среднего изменения.

#heading(level: 2)[5.18.5 Было и стало]

#table(
  columns: (1.5fr, 2fr, 2fr),
  table.header([*Что было*], [*Почему плохо*], [*Что сделано*]),
  [радужные линии], [непонятно, где кто], [серые линии],
  [нет точек], [не видно значений], [точки на концах],
  [нет средних], [нет сводки], [цветная средняя линия],
  [ось Y 85–115], [высокие значения скрыты], [70–145],
  [нет единиц], [«гемоглобин» без г/л], [«г/л»],
  [сетка по X и Y], [шум], [сетка только по Y],
  [полная рамка], [визуальный шум], [только левая и нижняя оси],
  [«Гемоглобин до и после»], [нет вывода], [заголовок-вывод],
  [нет n], [непонятна точность], [n = 30],
)

#heading(level: 2)[5.18.6 Чек-лист paired dot]

- ☐ Пары действительно парные.
- ☐ Видны отдельные линии и точки.
- ☐ Среднее/медиана изменения показаны.
- ☐ Ось не обрезает диапазон.
- ☐ Указаны единицы и _n_.
- ☐ Линии не радужные без смысла.
- ☐ При больших _n_ — не spaghetti.
- ☐ Есть парный тест/CI для вывода.
- ☐ Выбросы не скрыты.
- ☐ Рисунок проверен в конечном размере 85 мм.

#heading(level: 2)[5.18.7 Как воспроизвести]

```bash
uv sync
uv run python 05_charts/18_paired_dot/scripts/make_data.py
uv run python 05_charts/18_paired_dot/scripts/bad_plot.py
uv run python 05_charts/18_paired_dot/scripts/good_plot.py
```

Вот как это выглядит в коде:

```python
for b, a in zip(before, after, strict=True):
    ax.plot([0, 1], [b, a], color="#8A8A8A", alpha=0.45, linewidth=0.9)
    ax.scatter([0, 1], [b, a], s=8, color=PRIMARY_BLUE, alpha=0.45)

ax.plot([0, 1], [before.mean(), after.mean()],
        color=ACCENT_VERMILLION, linewidth=2.2, marker="o")
```

Для формального вывода используйте `scipy.stats.wilcoxon` или
`ttest_rel` и CI среднего изменения.

#heading(level: 2)[5.18.8 Что дальше]

Следующий график — *5.19 Bland–Altman*: согласие двух методов
измерения. У него будет свой генератор и свой `data/19_dataset.csv`.

#heading(level: 2)[Источники]

- Bland J. M., Altman D. G. Statistical Methods for Assessing Agreement
  between Two Methods of Clinical Measurement #text("//") _The Lancet_. 1986. —
  #link("https://doi.org/10.1016/S0140-6736(86)90837-8")[doi:10.1016/S0140-6736(86)90837-8]
- Wilke C. O. _Fundamentals of Data Visualization_. 2019. —
  #link("https://clauswilke.com/dataviz/")[clauswilke.com/dataviz]
- Matplotlib: `plot`/`scatter` —
  #link("https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html")[matplotlib.org]