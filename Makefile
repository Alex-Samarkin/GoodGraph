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

figures: data
	$(PYTHON) 01_principles/scripts/bad_plot.py
	$(PYTHON) 01_principles/scripts/good_plot.py

pdf:
	$(TYPST) compile --root . typst/main.typ build/metodichka.pdf

check:
	$(UV) run ruff check .

clean:
	rm -f build/*.png build/*.tmp build/*.aux build/*.log

# Удаляет и PDF — используйте осознанно.
distclean: clean
	rm -f build/*.pdf
