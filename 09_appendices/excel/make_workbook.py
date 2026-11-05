#!/usr/bin/env python3
"""Приложение D. Шесть графиков в Excel/LibreOffice.

Скрипт собирает .xlsx с шестью листами-графиками и скрытыми данными.
Затем workbook конвертируется в PDF (LibreOffice), страницы собираются
в один contact sheet: images/09_excel_six.png.

Запуск: uv run python 09_appendices/excel/make_workbook.py
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import pandas as pd
from openpyxl import Workbook
from openpyxl.chart import BarChart, LineChart, PieChart, Reference, ScatterChart
from openpyxl.chart.data_source import AxDataSource, NumDataSource, NumRef
from openpyxl.chart.label import DataLabelList
from openpyxl.chart.marker import DataPoint
from openpyxl.chart.series import Series
from openpyxl.chart.shapes import GraphicalProperties
from openpyxl.chart.trendline import Trendline
from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "09_appendix_dataset.csv"
BUILD = ROOT / "build"
IMAGES = ROOT / "images"
XLSX = BUILD / "09_appendices.xlsx"
PDF = BUILD / "09_appendices.pdf"

GROUPS = ["Контроль", "Препарат A", "Препарат B"]
COLORS = {"Контроль": "7F7F7F", "Препарат A": "0072B2", "Препарат B": "D55E00"}
ADVERSE = ["нет", "лёгкое", "серьёзное"]
ADVERSE_COLORS = ["0072B2", "E69F00", "D55E00"]


def add_data_sheet(wb: Workbook, name: str, rows: list[list]) -> None:
    ws = wb.create_sheet(name)
    for row in rows:
        ws.append(row)
    ws.sheet_state = "hidden"


def style_axis(chart) -> None:
    chart.x_axis.delete = False
    chart.y_axis.delete = False
    chart.x_axis.title = chart.x_axis.title or " "
    chart.y_axis.majorGridlines = None
    if chart.legend is not None:
        chart.legend.position = "b"
        chart.legend.overlay = False


def chart_sheet(wb: Workbook, name: str, chart) -> None:
    ws = wb.create_sheet(name)
    ws.sheet_view.showGridLines = False
    ws.sheet_view.showRowColHeaders = False
    chart.height = 13.5
    chart.width = 20
    chart.style = 2
    ws.add_chart(chart, "A1")
    ws.page_setup.orientation = "landscape"
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 1
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_margins.left = 0.1
    ws.page_margins.right = 0.1
    ws.page_margins.top = 0.1
    ws.page_margins.bottom = 0.1


def line_chart(wb: Workbook, df: pd.DataFrame) -> None:
    means = df.groupby(["week", "group"], as_index=False)["sbp_mm_hg"].mean()
    piv = means.pivot(index="week", columns="group", values="sbp_mm_hg").reset_index()
    rows = [["week"] + GROUPS] + [[int(w)] + [round(float(piv.loc[i, g]), 1) for g in GROUPS]
                                 for i, w in enumerate(piv["week"])]
    add_data_sheet(wb, "data_line", rows)
    ws = wb["data_line"]
    ch = LineChart()
    ch.title = "A. САД по неделям"
    ch.x_axis.title = "Неделя"
    ch.y_axis.title = "САД, мм рт. ст."
    ch.y_axis.scaling.min = 120
    ch.y_axis.scaling.max = 170
    ch.y_axis.majorUnit = 10
    ch.x_axis.majorUnit = 4
    data = Reference(ws, min_col=2, max_col=4, min_row=1, max_row=len(rows))
    cats = Reference(ws, min_col=1, min_row=2, max_row=len(rows))
    ch.add_data(data, titles_from_data=True)
    ch.set_categories(cats)
    for i, g in enumerate(GROUPS):
        s = ch.series[i]
        s.graphicalProperties.line.solidFill = COLORS[g]
        s.graphicalProperties.line.width = 22000
        s.marker.symbol = "circle"
        s.marker.size = 4
        s.marker.graphicalProperties = GraphicalProperties(solidFill=COLORS[g])
        s.smooth = False
    style_axis(ch)
    chart_sheet(wb, "A_line", ch)


def scatter_chart(wb: Workbook, patients: pd.DataFrame) -> None:
    rows = [["BMI", "Глюкоза"]] + [
        [float(r.bmi_kg_m2), float(r.glucose_mmol_l)] for r in patients.itertuples()
    ]
    add_data_sheet(wb, "data_scatter", rows)
    ws = wb["data_scatter"]
    ch = ScatterChart()
    ch.title = "B. BMI и глюкоза"
    ch.x_axis.title = "BMI, кг/м²"
    ch.y_axis.title = "Глюкоза, ммоль/л"
    ch.x_axis.scaling.min = 15
    ch.x_axis.scaling.max = 45
    ch.y_axis.scaling.min = 3
    ch.y_axis.scaling.max = 12
    ch.legend = None
    xvalues = Reference(ws, min_col=1, min_row=2, max_row=len(rows))
    yvalues = Reference(ws, min_col=2, min_row=2, max_row=len(rows))
    s = Series()
    s.yVal = NumDataSource(numRef=NumRef(f=str(yvalues)))
    s.xVal = AxDataSource(numRef=NumRef(f=str(xvalues)))
    ch.series.append(s)
    s.graphicalProperties = GraphicalProperties(solidFill="0072B2")
    s.graphicalProperties.line.noFill = True
    s.marker.symbol = "circle"
    s.marker.size = 4
    s.marker.graphicalProperties = GraphicalProperties(solidFill="0072B2")
    s.trendline = Trendline(trendlineType="linear", dispEq=False, dispRSqr=False)
    ch.x_axis.delete = False
    ch.y_axis.delete = False
    ch.y_axis.majorGridlines = None
    chart_sheet(wb, "B_scatter", ch)


def column_chart(wb: Workbook, change: pd.DataFrame) -> None:
    rows = [["group", "mean"]] + [[g, round(float(change[g]), 1)] for g in GROUPS]
    add_data_sheet(wb, "data_column", rows)
    ws = wb["data_column"]
    ch = BarChart()
    ch.type = "col"
    ch.title = "C. Среднее Δ САД к 12-й неделе"
    ch.x_axis.title = "Группа"
    ch.y_axis.title = "Δ САД, мм"
    ch.y_axis.scaling.min = -25
    ch.y_axis.scaling.max = 5
    ch.y_axis.majorUnit = 5
    data = Reference(ws, min_col=2, min_row=1, max_row=len(rows))
    cats = Reference(ws, min_col=1, min_row=2, max_row=len(rows))
    ch.add_data(data, titles_from_data=True)
    ch.set_categories(cats)
    ser = ch.series[0]
    ser.graphicalProperties = GraphicalProperties(solidFill="0072B2")
    ser.data_points = [
        DataPoint(idx=i, spPr=GraphicalProperties(solidFill=COLORS[g]))
        for i, g in enumerate(GROUPS)
    ]
    ch.legend = None
    style_axis(ch)
    chart_sheet(wb, "C_column", ch)


def stacked_chart(wb: Workbook, patients: pd.DataFrame) -> None:
    counts = pd.crosstab(patients["group"], patients["adverse_event"]).reindex(
        index=GROUPS, columns=ADVERSE, fill_value=0
    )
    rows = [["group"] + ADVERSE] + [[g] + [int(counts.loc[g, a]) for a in ADVERSE] for g in GROUPS]
    add_data_sheet(wb, "data_stacked", rows)
    ws = wb["data_stacked"]
    ch = BarChart()
    ch.type = "col"
    ch.grouping = "stacked"
    ch.overlap = 100
    ch.title = "D. Нежелательные явления по группам"
    ch.x_axis.title = "Группа"
    ch.y_axis.title = "Пациенты"
    data = Reference(ws, min_col=2, max_col=4, min_row=1, max_row=len(rows))
    cats = Reference(ws, min_col=1, min_row=2, max_row=len(rows))
    ch.add_data(data, titles_from_data=True)
    ch.set_categories(cats)
    for i, color in enumerate(ADVERSE_COLORS):
        ch.series[i].graphicalProperties = GraphicalProperties(solidFill=color)
    style_axis(ch)
    chart_sheet(wb, "D_stacked", ch)


def pie_chart(wb: Workbook, patients: pd.DataFrame) -> None:
    counts = patients["adverse_event"].value_counts().reindex(ADVERSE, fill_value=0)
    rows = [["outcome", "n"]] + [[a, int(counts[a])] for a in ADVERSE]
    add_data_sheet(wb, "data_pie", rows)
    ws = wb["data_pie"]
    ch = PieChart()
    ch.title = "E. Структура нежелательных явлений"
    data = Reference(ws, min_col=2, min_row=1, max_row=len(rows))
    cats = Reference(ws, min_col=1, min_row=2, max_row=len(rows))
    ch.add_data(data, titles_from_data=True)
    ch.set_categories(cats)
    ch.dataLabels = DataLabelList()
    ch.dataLabels.showPercent = True
    ch.dataLabels.showVal = False
    ch.dataLabels.showCatName = False
    ch.dataLabels.showSerName = False
    ch.dataLabels.showLegendKey = False
    for i, color in enumerate(ADVERSE_COLORS):
        pt = DataPoint(idx=i, spPr=GraphicalProperties(solidFill=color))
        ch.series[0].data_points = getattr(ch.series[0], "data_points", []) + [pt]
    ch.legend.position = "r"
    chart_sheet(wb, "E_pie", ch)


def bar_chart(wb: Workbook, patients: pd.DataFrame) -> None:
    rates = (
        patients.assign(severe=(patients["adverse_event"] == "серьёзное").astype(int))
        .groupby("group")["severe"].mean().reindex(GROUPS) * 100
    )
    rows = [["group", "severe_pct"]] + [[g, round(float(rates[g]), 1)] for g in GROUPS]
    add_data_sheet(wb, "data_bar", rows)
    ws = wb["data_bar"]
    ch = BarChart()
    ch.type = "bar"
    ch.title = "F. Серьёзные явления, %"
    ch.x_axis.title = "%"
    ch.y_axis.title = "Группа"
    ch.x_axis.scaling.min = 0
    ch.x_axis.scaling.max = 30
    ch.x_axis.majorUnit = 10
    data = Reference(ws, min_col=2, min_row=1, max_row=len(rows))
    cats = Reference(ws, min_col=1, min_row=2, max_row=len(rows))
    ch.add_data(data, titles_from_data=True)
    ch.set_categories(cats)
    ch.series[0].graphicalProperties = GraphicalProperties(solidFill="0072B2")
    ch.series[0].data_points = [
        DataPoint(idx=i, spPr=GraphicalProperties(solidFill=COLORS[g]))
        for i, g in enumerate(GROUPS)
    ]
    ch.dataLabels = DataLabelList()
    ch.dataLabels.showVal = True
    ch.dataLabels.showCatName = False
    ch.dataLabels.showSerName = False
    ch.dataLabels.showPercent = False
    ch.dataLabels.showLegendKey = False
    ch.legend = None
    style_axis(ch)
    chart_sheet(wb, "F_bar", ch)


def build_workbook() -> None:
    df = pd.read_csv(DATA)
    patients = df.drop_duplicates("patient_id").reset_index(drop=True)
    wide = df.pivot(index=["patient_id", "group"], columns="week", values="sbp_mm_hg").reset_index()
    wide["change"] = wide[12] - wide[0]
    change = wide.groupby("group")["change"].mean()

    wb = Workbook()
    wb.remove(wb.active)
    line_chart(wb, df)
    scatter_chart(wb, patients)
    column_chart(wb, change)
    stacked_chart(wb, patients)
    pie_chart(wb, patients)
    bar_chart(wb, patients)
    wb.save(XLSX)
    print("saved:", XLSX)


def export_images() -> None:
    profile = BUILD / "lo_profile_appendix"
    subprocess.run(
        ["soffice", f"-env:UserInstallation=file://{profile}", "--headless",
         "--convert-to", "pdf", "--outdir", str(BUILD), str(XLSX)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    prefix = BUILD / "excel_page"
    for old in BUILD.glob("excel_page-*.png"):
        old.unlink()
    subprocess.run(
        ["pdftoppm", "-png", "-r", "220", str(PDF), str(prefix)],
        check=True, stdout=subprocess.DEVNULL,
    )
    pages = sorted(BUILD.glob("excel_page-*.png"))
    crops = []
    for page in pages:
        im = Image.open(page).convert("RGB")
        bg = Image.new("RGB", im.size, "white")
        diff = ImageChops.difference(im, bg)
        bbox = diff.getbbox()
        if bbox:
            im = im.crop((max(0, bbox[0] - 15), max(0, bbox[1] - 15),
                          min(im.width, bbox[2] + 15), min(im.height, bbox[3] + 15)))
        crops.append(im)
    crops = crops[:6]
    cell_w = max(i.width for i in crops)
    cell_h = max(i.height for i in crops)
    gap = 20
    canvas = Image.new("RGB", (cell_w * 3 + gap * 2, cell_h * 2 + gap), "white")
    for idx, im in enumerate(crops):
        x = (idx % 3) * (cell_w + gap)
        y = (idx // 3) * (cell_h + gap)
        canvas.paste(im, (x, y))
    out = IMAGES / "09_excel_six.png"
    canvas.save(out)
    print("saved:", out)


if __name__ == "__main__":
    BUILD.mkdir(exist_ok=True)
    IMAGES.mkdir(exist_ok=True)
    build_workbook()
    export_images()
