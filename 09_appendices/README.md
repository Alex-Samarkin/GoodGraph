# Приложения A–F: R, Julia, Excel/LibreOffice

Краткий обзор трёх сред и по шесть корректных графиков в каждой.
Все примеры используют один учебный набор `data/09_appendix_dataset.csv`
(150 пациентов, 3 группы, 600 строк), чтобы сравнение было честным.

## Файлы

| Файл | Назначение |
|---|---|
| [`appendices.md`](appendices.md) | текст приложений в Markdown |
| [`appendices.typ`](appendices.typ) | Typst-дубликат |
| [`scripts/make_data.py`](scripts/make_data.py) | общий датасет |
| [`r/six_plots.R`](r/six_plots.R) | шесть графиков на R |
| [`julia/six_plots.jl`](julia/six_plots.jl) | шесть графиков на Julia |
| [`julia_env/`](julia_env/) | Project/Manifest для Julia |
| [`excel/make_workbook.py`](excel/make_workbook.py) | шесть графиков Excel → `.xlsx` → PDF/PNG |

## Запуск

```bash
# данные
uv run python 09_appendices/scripts/make_data.py

# R
Rscript 09_appendices/r/six_plots.R

# Julia
JULIA_DEPOT_PATH="$PWD/.julia:$HOME/.julia" \
julia --project=09_appendices/julia_env 09_appendices/julia/six_plots.jl

# Excel/LibreOffice
uv run python 09_appendices/excel/make_workbook.py
```

Или одной командой: `make appendices` (нужны `Rscript`, `julia`, `soffice`).

## Что внутри

- **A** — сравнение R, Julia, Excel/LibreOffice и Python: сильные стороны,
  пакеты, ограничения, воспроизводимость.
- **B** — R: линия с 95 % CI, scatter + LOESS, box + jitter, столбцы с CI,
  heatmap, Kaplan–Meier.
- **C** — Julia: линия + ribbon, scatter, точки + медиана, столбцы с ошибками,
  heatmap, KM.
- **D** — Excel: линия, scatter + тренд, столбцы, stacked, pie, bar.
- **E** — что выбрать под задачу.
- **F** — чек-лист переноса графика между средами.

## Результаты

- `images/09_r_six.png`
- `images/09_julia_six.png`
- `images/09_excel_six.png`
