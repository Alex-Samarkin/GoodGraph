"""Палитры для научной графики.

Почему не «просто красивые цвета»:

* **Okabe–Ito** — палитра, различимая при протанопии и дейтеранопии;
  рекомендована Color Universal Design (Okabe, Ito, 2008).
* **Paul Tol** — наборы bright/muted, проверенные на различимость,
  в том числе в оттенках серого.
* Последовательные шкалы ``viridis``, ``cividis`` воспринимаются
  равномерно и остаются читаемыми при дальтонизме.

Все палитры возвращаются в виде списков HEX-строк, чтобы их можно было
передавать в matplotlib, seaborn и plotnine без преобразований.
"""

from __future__ import annotations

from collections import OrderedDict

# Классическая палитра Okabe–Ito (2008).
# Порядок выбран так, чтобы первые 3–4 цвета хорошо различались.
OKABE_ITO: OrderedDict[str, str] = OrderedDict(
    [
        ("orange", "#E69F00"),
        ("sky_blue", "#56B4E9"),
        ("bluish_green", "#009E73"),
        ("yellow", "#F0E442"),
        ("blue", "#0072B2"),
        ("vermillion", "#D55E00"),
        ("reddish_purple", "#CC79A7"),
        ("black", "#000000"),
    ]
)

# Paul Tol, bright: универсальная качественная палитра.
TOL_BRIGHT: list[str] = [
    "#4477AA",
    "#EE6677",
    "#228833",
    "#CCBB44",
    "#66CCEE",
    "#AA3377",
    "#BBBBBB",
]

# Paul Tol, muted: спокойные цвета для больших заливок и слайдов.
TOL_MUTED: list[str] = [
    "#CC6677",
    "#332288",
    "#DDCC77",
    "#117733",
    "#88CCEE",
    "#882255",
    "#44AA99",
    "#999933",
    "#AA4499",
    "#DDDDDD",
]

# Семантические роли, а не «цвета вообще»: серый — контроль/фон,
# синий — основной результат, вермилион — акцент/второй результат.
CONTROL_GREY = "#8C8C8C"
PRIMARY_BLUE = "#0072B2"
ACCENT_VERMILLION = "#D55E00"
SECONDARY_GREEN = "#009E73"
TEXT_GREY = "#333333"
LIGHT_GRID = "#E6E6E6"


def okabe_ito(n: int | None = None, *, include_black: bool = False) -> list[str]:
    """Вернуть первые *n* цветов палитры Okabe–Ito.

    Parameters
    ----------
    n:
        Сколько цветов нужно. ``None`` — все доступные.
    include_black:
        Добавлять ли чёрный. Обычно чёрный лучше оставить для текста,
        осей и подписей, а не для серий данных.
    """
    palette = list(OKABE_ITO.values())
    if not include_black:
        palette = [c for c in palette if c != OKABE_ITO["black"]]
    return palette if n is None else palette[:n]


def tol_bright(n: int | None = None) -> list[str]:
    """Вернуть первые *n* цветов палитры Paul Tol bright."""
    return TOL_BRIGHT if n is None else TOL_BRIGHT[:n]
