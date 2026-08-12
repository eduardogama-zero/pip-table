# -*- coding: utf-8 -*-
"""Renderiza a página inteira (index.html) a partir dos dados.

Templating em Python puro (stdlib) — sem dependências externas. O template é
``templates/page.html`` com marcadores ``__CELLS__``, ``__LEGEND__``,
``__COUNT__`` e ``__ELEMENTS_JSON__``, substituídos aqui.
"""

import html
import json
from pathlib import Path

from .data import elements, LEGEND

_TEMPLATE = Path(__file__).resolve().parent / "templates" / "page.html"


def _cell(e):
    return (
        f'    <div class="cell cat-{e["cat"]}" '
        f'style="grid-column:{e["x"]};grid-row:{e["y"]}" data-n="{e["n"]}">'
        f'<span class="num">{e["n"]}</span>'
        f'<span class="sym">{html.escape(e["sym"])}</span>'
        f'<span class="nm">{html.escape(e["name"])}</span></div>'
    )


def _legend_row(code, label):
    return f'      <span><i class="sw cat-{code}"></i>{html.escape(label)}</span>'


def render_page():
    """Devolve o HTML final como string, gerado 100% em Python."""
    els = elements()
    cells = "\n".join(_cell(e) for e in els)
    legend = "\n".join(_legend_row(code, label) for code, label in LEGEND)
    tmpl = _TEMPLATE.read_text(encoding="utf-8")
    return (
        tmpl
        .replace("__CELLS__", cells)
        .replace("__LEGEND__", legend)
        .replace("__COUNT__", str(len(els)))
        .replace("__ELEMENTS_JSON__", json.dumps(els, ensure_ascii=False))
    )
