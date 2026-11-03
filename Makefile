# Команды проекта. Запускать из корня репозитория.
#
# В обычном окружении достаточно `make`.
# В песочнице с read-only домашним кешем:
#   make UV="env UV_CACHE_DIR=$PWD/.uv-cache UV_PYTHON_INSTALL_DIR=$PWD/.uv-python uv"
#
# Переменные можно переопределить:
#   make UV=/path/to/uv TYPST=/path/to/typst

UV ?= uv
PYTHON ?= $(UV) run python
TYPST ?= typst

.PHONY: all sync data figures pdf check clean

all: figures pdf

sync:
	$(UV) sync

data:
	$(PYTHON) 01_principles/scripts/make_data.py
	$(PYTHON) 02_python/scripts/make_data.py
	$(PYTHON) 05_charts/01_line/scripts/make_data.py
	$(PYTHON) 05_charts/02_step/scripts/make_data.py
	$(PYTHON) 05_charts/03_area/scripts/make_data.py
	$(PYTHON) 05_charts/04_small_multiples/scripts/make_data.py
	$(PYTHON) 05_charts/05_scatter/scripts/make_data.py
	$(PYTHON) 05_charts/06_hexbin/scripts/make_data.py
	$(PYTHON) 05_charts/07_contour/scripts/make_data.py
	$(PYTHON) 05_charts/08_loess/scripts/make_data.py
	$(PYTHON) 05_charts/09_histogram/scripts/make_data.py
	$(PYTHON) 05_charts/10_ecdf/scripts/make_data.py
	$(PYTHON) 05_charts/11_box/scripts/make_data.py
	$(PYTHON) 05_charts/12_violin/scripts/make_data.py
	$(PYTHON) 05_charts/13_strip/scripts/make_data.py
	$(PYTHON) 05_charts/14_dot_ci/scripts/make_data.py
	$(PYTHON) 05_charts/15_bar/scripts/make_data.py
	$(PYTHON) 05_charts/16_forest/scripts/make_data.py
	$(PYTHON) 05_charts/17_slope/scripts/make_data.py
	$(PYTHON) 05_charts/18_paired_dot/scripts/make_data.py
	$(PYTHON) 05_charts/19_bland_altman/scripts/make_data.py
	$(PYTHON) 05_charts/20_stacked_bar/scripts/make_data.py
	$(PYTHON) 05_charts/21_bar_100/scripts/make_data.py
	$(PYTHON) 05_charts/22_pie/scripts/make_data.py
	$(PYTHON) 05_charts/23_treemap/scripts/make_data.py
	$(PYTHON) 05_charts/24_heatmap/scripts/make_data.py
	$(PYTHON) 05_charts/25_clustermap/scripts/make_data.py
	$(PYTHON) 05_charts/26_corr_matrix/scripts/make_data.py
	$(PYTHON) 05_charts/27_kaplan_meier/scripts/make_data.py
	$(PYTHON) 05_charts/28_cumulative_incidence/scripts/make_data.py
	$(PYTHON) 05_charts/29_roc/scripts/make_data.py
	$(PYTHON) 05_charts/30_precision_recall/scripts/make_data.py
	$(PYTHON) 05_charts/31_calibration/scripts/make_data.py
	$(PYTHON) 05_charts/32_caterpillar/scripts/make_data.py
	$(PYTHON) 05_charts/33_funnel/scripts/make_data.py

figures: data
	$(PYTHON) 01_principles/scripts/bad_plot.py
	$(PYTHON) 01_principles/scripts/good_plot.py
	$(PYTHON) 02_python/scripts/compare_libraries.py
	$(PYTHON) 03_requirements/scripts/plot_palettes.py
	$(PYTHON) 03_requirements/scripts/plot_cvd.py
	$(PYTHON) 03_requirements/scripts/plot_fonts.py
	$(PYTHON) 04_overview/scripts/plot_chart_map.py
	$(PYTHON) 05_charts/01_line/scripts/bad_plot.py
	$(PYTHON) 05_charts/01_line/scripts/good_plot.py
	$(PYTHON) 05_charts/02_step/scripts/bad_plot.py
	$(PYTHON) 05_charts/02_step/scripts/good_plot.py
	$(PYTHON) 05_charts/03_area/scripts/bad_plot.py
	$(PYTHON) 05_charts/03_area/scripts/good_plot.py
	$(PYTHON) 05_charts/04_small_multiples/scripts/bad_plot.py
	$(PYTHON) 05_charts/04_small_multiples/scripts/good_plot.py
	$(PYTHON) 05_charts/05_scatter/scripts/bad_plot.py
	$(PYTHON) 05_charts/05_scatter/scripts/good_plot.py
	$(PYTHON) 05_charts/06_hexbin/scripts/bad_plot.py
	$(PYTHON) 05_charts/06_hexbin/scripts/good_plot.py
	$(PYTHON) 05_charts/07_contour/scripts/bad_plot.py
	$(PYTHON) 05_charts/07_contour/scripts/good_plot.py
	$(PYTHON) 05_charts/08_loess/scripts/bad_plot.py
	$(PYTHON) 05_charts/08_loess/scripts/good_plot.py
	$(PYTHON) 05_charts/09_histogram/scripts/bad_plot.py
	$(PYTHON) 05_charts/09_histogram/scripts/good_plot.py
	$(PYTHON) 05_charts/10_ecdf/scripts/bad_plot.py
	$(PYTHON) 05_charts/10_ecdf/scripts/good_plot.py
	$(PYTHON) 05_charts/11_box/scripts/bad_plot.py
	$(PYTHON) 05_charts/11_box/scripts/good_box_points.py
	$(PYTHON) 05_charts/11_box/scripts/good_violin_box.py
	$(PYTHON) 05_charts/11_box/scripts/good_box_hist.py
	$(PYTHON) 05_charts/12_violin/scripts/bad_plot.py
	$(PYTHON) 05_charts/12_violin/scripts/good_violin_quart.py
	$(PYTHON) 05_charts/12_violin/scripts/good_violin_box.py
	$(PYTHON) 05_charts/13_strip/scripts/bad_plot.py
	$(PYTHON) 05_charts/13_strip/scripts/good_plot.py
	$(PYTHON) 05_charts/14_dot_ci/scripts/bad_plot.py
	$(PYTHON) 05_charts/14_dot_ci/scripts/good_plot.py
	$(PYTHON) 05_charts/15_bar/scripts/bad_plot.py
	$(PYTHON) 05_charts/15_bar/scripts/good_plot.py
	$(PYTHON) 05_charts/16_forest/scripts/bad_plot.py
	$(PYTHON) 05_charts/16_forest/scripts/good_plot.py
	$(PYTHON) 05_charts/17_slope/scripts/bad_plot.py
	$(PYTHON) 05_charts/17_slope/scripts/good_plot.py
	$(PYTHON) 05_charts/18_paired_dot/scripts/bad_plot.py
	$(PYTHON) 05_charts/18_paired_dot/scripts/good_plot.py
	$(PYTHON) 05_charts/19_bland_altman/scripts/bad_plot.py
	$(PYTHON) 05_charts/19_bland_altman/scripts/good_plot.py
	$(PYTHON) 05_charts/20_stacked_bar/scripts/bad_plot.py
	$(PYTHON) 05_charts/20_stacked_bar/scripts/good_plot.py
	$(PYTHON) 05_charts/21_bar_100/scripts/bad_plot.py
	$(PYTHON) 05_charts/21_bar_100/scripts/good_plot.py
	$(PYTHON) 05_charts/22_pie/scripts/bad_plot.py
	$(PYTHON) 05_charts/22_pie/scripts/good_plot.py
	$(PYTHON) 05_charts/23_treemap/scripts/bad_plot.py
	$(PYTHON) 05_charts/23_treemap/scripts/good_plot.py
	$(PYTHON) 05_charts/24_heatmap/scripts/bad_plot.py
	$(PYTHON) 05_charts/24_heatmap/scripts/good_plot.py
	$(PYTHON) 05_charts/25_clustermap/scripts/bad_plot.py
	$(PYTHON) 05_charts/25_clustermap/scripts/good_plot.py
	$(PYTHON) 05_charts/26_corr_matrix/scripts/bad_plot.py
	$(PYTHON) 05_charts/26_corr_matrix/scripts/good_plot.py
	$(PYTHON) 05_charts/27_kaplan_meier/scripts/bad_plot.py
	$(PYTHON) 05_charts/27_kaplan_meier/scripts/good_plot.py
	$(PYTHON) 05_charts/28_cumulative_incidence/scripts/bad_plot.py
	$(PYTHON) 05_charts/28_cumulative_incidence/scripts/good_plot.py
	$(PYTHON) 05_charts/29_roc/scripts/bad_plot.py
	$(PYTHON) 05_charts/29_roc/scripts/good_plot.py
	$(PYTHON) 05_charts/30_precision_recall/scripts/bad_plot.py
	$(PYTHON) 05_charts/30_precision_recall/scripts/good_plot.py
	$(PYTHON) 05_charts/31_calibration/scripts/bad_plot.py
	$(PYTHON) 05_charts/31_calibration/scripts/good_plot.py
	$(PYTHON) 05_charts/32_caterpillar/scripts/bad_plot.py
	$(PYTHON) 05_charts/32_caterpillar/scripts/good_plot.py
	$(PYTHON) 05_charts/33_funnel/scripts/bad_plot.py
	$(PYTHON) 05_charts/33_funnel/scripts/good_plot.py

pdf:
	$(TYPST) compile --root . typst/main.typ build/metodichka.pdf

check:
	$(UV) run ruff check .

clean:
	rm -f build/*.png build/*.tmp build/*.aux build/*.log

# Удаляет и PDF — используйте осознанно.
distclean: clean
	rm -f build/*.pdf
