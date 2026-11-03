# Раздел 2. Python-инструментарий и настройка среды

Раздел о том, чем рисовать графики и как сделать результат воспроизводимым:
matplotlib, seaborn, plotnine, uv и общий стиль `goodgraph`.

## Файлы

| Файл | Назначение |
|---|---|
| [`python.md`](python.md) | основной текст раздела в Markdown |
| [`python.typ`](python.typ) | тот же текст для сборки PDF через Typst |
| [`scripts/make_data.py`](scripts/make_data.py) | генерация данных → `data/02_python_dataset.csv` |
| [`scripts/compare_libraries.py`](scripts/compare_libraries.py) | один набор данных — три библиотеки |

## Данные

Раздел создаёт **свой набор данных**:
[`data/02_python_dataset.csv`](../data/02_python_dataset.csv) — 132 пациента,
HbA1c до и после 12 недель. Генератор — [`scripts/make_data.py`](scripts/make_data.py);
скрипт построения читает только этот CSV и не зависит от данных раздела 1.

## Рисунки

| Рисунок | Файлы | Что показывает |
|---|---|---|
| 2.1A | `images/02_matplotlib_scatter.svg`, `.png` | HbA1c scatter в matplotlib |
| 2.1B | `images/02_seaborn_scatter.svg`, `.png` | HbA1c scatter в seaborn |
| 2.1C | `images/02_plotnine_scatter.svg`, `.png` | HbA1c scatter в plotnine |

Все панели — 54 × 62 мм; три панели с промежутками дают ширину около 170 мм.
Цвет и форма маркера дублируют друг друга, поэтому панели читаются
и в оттенках серого.

## Запуск

```bash
# из корня репозитория
uv sync
uv run python 02_python/scripts/make_data.py
uv run python 02_python/scripts/compare_libraries.py
```

Или:

```bash
make figures
```

## Что важно в разделе

- matplotlib — императивный контроль, seaborn — данные и статистика,
  plotnine — грамматика графики;
- все три библиотеки в итоге рисуют через matplotlib;
- `uv` фиксирует Python и зависимости, `uv.lock` коммитится;
- стиль вынесен в `goodgraph`, поэтому библиотеки не диктуют оформление;
- типичные ошибки: `plt.show()` в скрипте, глобальное состояние `pyplot`,
  `sns.set_theme()` после `apply_style()`, `bbox_inches="tight"` и точная
  ширина, единицы plotnine (дюймы, не миллиметры).

## Сборка PDF

```bash
typst compile --root . 02_python/python.typ build/02_python.pdf
```

Флаг `--root .` обязателен: иначе Typst не пустит файл из `02_python/`
к картинкам в `../images/`.

## Связь с другими разделами

- Требования к цвету, шрифтам и размерам — раздел 3.
- Обзор видов графиков — раздел 4.
- Полные примеры «данные → плохо → хорошо» — раздел 5.
- Подготовка к публикации — раздел 7.
