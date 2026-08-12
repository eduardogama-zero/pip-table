#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Entrada canônica do build: `python build.py` gera ../index.html na raiz do repo."""

from pathlib import Path

from pip_table.builder import build

if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    out, size, n = build(root)
    print(f"wrote {out} — {size} bytes, {n} elementos")
