// Раздел 5.14. Dot + CI: оценка и неопределённость.
// Сборка: typst compile --root . 05_charts/14_dot_ci/dot_ci.typ build/05_14_dot_ci.pdf

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

#heading(level: 1)[5.14 Dot + CI: оценка и неопределённость]

Dot + CI — это точка оценки и доверительный интервал вокруг неё.
Такой график отвечает не только «сколько», но и «насколько точно».
Он честнее столбца с одной высотой: видно, что оценка — случайная
величина с неопределённостью.

Разница принципиальная: *CI — это не SD*. Стандартное отклонение
описывает разброс наблюдений, доверительный интервал — точность
оценки. Для доли используют интервал Уилсона, для среднего —
t-интервал или бутстрэп.

#heading(level: 2)[5.14.1 Сфера применения]

Dot + CI отвечает на вопрос: *какова оценка в каждой группе
и насколько она точна?*

Где это пригодится:

- доля осложнений/смертности по центрам;
- средние показатели по больницам с 95 % CI;
- результаты подгрупп перед forest plot (5.16);
- сравнение центров без ложного ранжирования;
- оценка эффекта с неопределённостью.

Когда dot + CI *не* нужен:

- нужны все наблюдения — strip/box;
- нужна одна сводка без сравнения — таблица;
- групп много и CI пересекаются — forest plot;
- оценка без интервала — описательная статистика;
- время до события — Kaplan–Meier.

#heading(level: 2)[5.14.2 Данные]

Сценарий: 600 пациентов, шесть центров, по 100 человек. Исход —
осложнение (1/0). Для каждой доли — 95 % ДИ Уилсона.

#table(
  columns: (1.4fr, 2.8fr, 1.2fr),
  table.header([*Колонка*], [*Смысл*], [*Единица*]),
  [`patient_id`], [идентификатор пациента], [—],
  [`center`], [центр], [—],
  [`complication`], [осложнение (1/0)], [—],
)

Доли: 9–19 %; общая — 14,7 %. Интервалы широкие (≈ 5–28 %)
из-за _n_ = 100 на центр.

Генератор: `05_charts/14_dot_ci/scripts/make_data.py` → `data/14_dataset.csv`.

#heading(level: 2)[5.14.3 Плохой график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_14_bad_dot_ci.png", width: 84%)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.14.1. Плохой dot + CI: вместо ДИ — SD, обрезанная ось 0–15,
    радуга, нет общей доли и n.
  ]]
]

Код: `05_charts/14_dot_ci/scripts/bad_plot.py`.

Что не так:

+ *Вместо 95 % ДИ — стандартное отклонение.* Усы выглядят
  как «интервалы», но это разброс бинарного исхода; их нельзя
  интерпретировать как точность оценки.
+ *Ось X обрезана до 0–15 %.* Центры с долей 18–19 % вообще
  не видны.
+ *Радужные точки и усы.* CVD, декор.
+ *Тяжёлая сетка, полная рамка.*
+ *Нет общей доли, n и единиц.*
+ *Заголовок «Осложнения по центрам».* Не сообщает,
  что показана неопределённость.

#heading(level: 2)[5.14.4 Правильный график]

#block(breakable: false)[
  #align(center)[#image("../../images/05_14_good_dot_ci.png", width: 85mm)]
  #v(2pt)
  #align(center)[#text(size: 8.5pt, style: "italic")[
    Рисунок 5.14.2. Правильный dot + CI: 95 % ДИ Уилсона, полный
    диапазон 0–35, общая доля, n = 100.
  ]]
]

Код: `05_charts/14_dot_ci/scripts/good_plot.py`.

Что изменилось:

+ *95 % ДИ Уилсона* для каждой доли — корректная
  неопределённость.
+ *Полный диапазон 0–35 %.* Все центры видны.
+ *Один цвет.* Точки и усы не конкурируют.
+ *Общая доля 14,7 %* — пунктирная линия и подпись.
+ *Сортировка по доле.* Легче читать, но CI показывают,
  что различия неочевидны.
+ *n = 100 в каждом центре, единицы, 85 мм.*

Пересекающиеся интервалы — важный сигнал: нельзя ранжировать
центры без формального сравнения. Dot + CI как раз показывает,
что разница между 9 % и 19 % при _n_ = 100 может быть случайной.

#heading(level: 2)[5.14.5 Было и стало]

#table(
  columns: (1.5fr, 2fr, 2fr),
  table.header([*Что было*], [*Почему плохо*], [*Что сделано*]),
  [SD вместо CI], [не та неопределённость], [95 % ДИ Уилсона],
  [ось X 0–15], [центры 18–19 % скрыты], [0–35],
  [радуга], [CVD, декор], [один цвет],
  [нет общей доли], [нет ориентира], [линия 14,7 %],
  [нет сортировки], [трудно читать], [сортировка по доле],
  [сетка по X и Y], [шум], [сетка только по X],
  [полная рамка], [визуальный шум], [только левая и нижняя оси],
  [«Осложнения по центрам»], [нет сообщения], [заголовок о 95 % ДИ],
  [нет n], [непонятна точность], [n = 100],
)

#heading(level: 2)[5.14.6 Чек-лист dot + CI]

- ☐ Указано, что такое интервал: 95 % CI, а не SD/SE.
- ☐ Для долей — Уилсон/точный интервал, не нормальное приближение.
- ☐ Ось не обрезает интервалы.
- ☐ Указаны единицы и _n_ по группам.
- ☐ Есть общая оценка/референс, если она нужна.
- ☐ Сортировка не выдаёт себя за статистический вывод.
- ☐ Пересечение CI не игнорируется.
- ☐ Цвет не дублирует ось.
- ☐ Сетка не конкурирует с усами.
- ☐ Рисунок проверен в конечном размере 85 мм.

#heading(level: 2)[5.14.7 Как воспроизвести]

```bash
uv sync
uv run python 05_charts/14_dot_ci/scripts/make_data.py
uv run python 05_charts/14_dot_ci/scripts/bad_plot.py
uv run python 05_charts/14_dot_ci/scripts/good_plot.py
```

Вот как это выглядит в коде:

```python
def wilson_ci(successes, n, z=1.96):
    p = successes / n
    denominator = 1 + z**2 / n
    center = (p + z**2 / (2 * n)) / denominator
    half = z * np.sqrt(p * (1 - p) / n + z**2 / (4 * n**2)) / denominator
    return (center - half) * 100, (center + half) * 100

low, high = wilson_ci(successes, n)
ax.errorbar(p, y, xerr=[[p - low], [high - p]], fmt="o", color=PRIMARY_BLUE)
```

Для средних используйте t-интервал или бутстрэп; для долей
Уилсон устойчивее нормального приближения при малых _n_ и крайних
долях.

#heading(level: 2)[5.14.8 Что дальше]

Следующий график — *5.15 bar*: столбцы для сравнения величин
и их типичные ошибки. У него будет свой генератор и свой
`data/15_dataset.csv`.

#heading(level: 2)[Источники]

- Wilson E. B. Probable Inference, the Law of Succession, and Statistical
  Inference #text("//") _JASA_. 1927. —
  #link("https://doi.org/10.1080/01621459.1927.10502953")[doi:10.1080/01621459.1927.10502953]
- Cumming G. _Understanding the New Statistics_. Routledge, 2012. —
  #link("https://www.routledge.com/Understanding-the-New-Statistics-Effect-Sizes-Confidence-Intervals-and-Meta-Analysis/Cumming/p/book/9780415879682")[routledge.com]
- Wilke C. O. _Fundamentals of Data Visualization_. 2019. —
  #link("https://clauswilke.com/dataviz/")[clauswilke.com/dataviz]
- Matplotlib: `errorbar` —
  #link("https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html")[matplotlib.org]