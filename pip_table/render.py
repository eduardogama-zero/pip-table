# -*- coding: utf-8 -*-
"""Renderiza a página inteira (index.html) a partir dos dados, via Jinja2."""

import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from .data import elements, LEGEND

_TEMPLATES = Path(__file__).resolve().parent / "templates"


def render_page():
    """Devolve o HTML final como string, gerado 100% em Python."""
    els = elements()
    env = Environment(
        loader=FileSystemLoader(str(_TEMPLATES)),
        autoescape=select_autoescape(enabled_extensions=("html", "j2", "html.j2")),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    tmpl = env.get_template("page.html.j2")
    return tmpl.render(
        elements=els,
        legend=LEGEND,
        elements_json=json.dumps(els, ensure_ascii=False),
    )
