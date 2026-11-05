# Раздел 7. Подготовка рисунков к публикации

Журнальные требования, собственный датасет и двухпанельный рисунок,
таблица настроек, модуль `journal_style.py`, интерактивный генератор
темы, экспорт SVG/PDF/PNG/TIFF и настройки для web/HTML.

## Файлы

| Файл | Назначение |
|---|---|
| [`publication.md`](publication.md) | текст раздела в Markdown |
| [`publication.typ`](publication.typ) | Typst-дубликат |
| [`scripts/make_data.py`](scripts/make_data.py) | генерация → `data/07_publication_dataset.csv` |
| [`scripts/journal_style.py`](scripts/journal_style.py) | пресеты, экспорт, web-настройки |
| [`scripts/plot_journal.py`](scripts/plot_journal.py) | рисунок 170 × 95 мм и web 960 px |
| [`scripts/make_journal_style.py`](scripts/make_journal_style.py) | генератор темы в диалоге |

## Данные

`data/07_publication_dataset.csv` — 90 пациентов, 3 группы, САД на
0/4/8/12-й неделе (360 строк).

## Рисунки

| Рисунок | Файлы | Что показывает |
|---|---|---|
| 7.1 | `images/07_journal_figure.svg/.pdf/.png/.tiff` | журнальный рисунок 170 × 95 мм |
| 7.2 | `images/07_journal_web.png`, `@2x` | web 960 × 480 px |

## Запуск

```bash
uv sync
uv run python 07_publication/scripts/make_data.py
uv run python 07_publication/scripts/plot_journal.py
uv run python 07_publication/scripts/make_journal_style.py --interactive
```

Генератор темы пишет `build/journal_style_generated.py` и `.json`;
без диалога: `--preset nature`. Быстрый запуск: `make journal-style`.