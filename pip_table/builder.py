# -*- coding: utf-8 -*-
"""Escreve o index.html a partir do template Python."""

from pathlib import Path

from .data import elements
from .render import render_page


def build(out_dir):
    """Gera ``index.html`` em ``out_dir`` e devolve (caminho, bytes, nº de elementos)."""
    out_dir = Path(out_dir)
    html = render_page()
    out = out_dir / "index.html"
    out.write_text(html, encoding="utf-8")
    return out, len(html), len(elements())


def main():
    """Ponto de entrada instalado (``pip-table-build``): grava no diretório atual."""
    out, size, n = build(Path.cwd())
    print(f"wrote {out} — {size} bytes, {n} elementos")


if __name__ == "__main__":
    main()
