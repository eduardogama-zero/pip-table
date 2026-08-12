# CLAUDE.md — PIP-TABLE 3000

Contexto para o Claude Code manter este projeto.

## O que é
Tabela periódica interativa estilo **Fallout / Pip-Boy** para **tela TFT touch 800×480**.
A **página é gerada 100% em Python** (template Jinja2); `index.html` é o artefato/preview
e espelha o produto físico (uma tabela periódica real com LEDs endereçáveis atrás dos elementos).

## Arquitetura / fonte da verdade
- **`pip_table/data.py`** — ÚNICA fonte de dados dos 118 elementos (lista `E`). `elements()`
  devolve os dicts já com os campos derivados `shells` (aufbau), `protons`, `neutrons`, `radioactive`.
- **`pip_table/templates/page.html.j2`** — a página inteira: CSS + a **grade renderizada
  server-side por Jinja** (`{% for e in elements %}`) + o JS de interação. É aqui que se mexe em visual/UI.
- **`pip_table/render.py`** — carrega os dados e renderiza o template (Jinja2, autoescape).
- **`pip_table/builder.py`** / **`build.py`** — escrevem `index.html`.
- **`index.html`** — artefato gerado. **Não editar à mão**; é sobrescrito pelo build.
  Marcado como `linguist-generated` no `.gitattributes` (não conta como linguagem no GitHub).

### Divisão Python × JavaScript
- **Python (Jinja) gera o conteúdo estático**: células dos 118 elementos, marcadores 57-71/89-103,
  legenda, rodapé. Antes isso era montado por JS no cliente — agora é HTML no `index.html`.
- **JS só faz comportamento** (não dá para gerar em Python): animação do átomo em `<canvas>`,
  abertura da ficha ao toque, menu de LEDs e navegação por teclado. Os dados para essas
  interações continuam embutidos como JSON (`const ELEMENTS = ...`) renderizado pelo template.

### Pipeline de build
```bash
pip install -r requirements.txt   # Jinja2 (1ª vez)
python build.py                    # regera ../index.html a partir de data.py + page.html.j2
```

## Regras importantes
- Alterou dados de elemento (massa, categoria, descrição, posição)? → editar a lista `E` em
  `pip_table/data.py` e rodar `python build.py`.
- Alterou visual/UI/lógica (CSS, canvas do átomo, menu, grade)? → editar `pip_table/templates/page.html.j2`
  e rodar `python build.py`.
- Nunca editar `index.html` à mão; será sobrescrito.
- Após mudar, confira: `index.html` deve ter 118 ocorrências de `class="cell cat-`, `id="atom"`
  presente e nenhum `{{` residual (Jinja não renderizado).

## Estética (não quebrar)
Verde fósforo (`--green:#41ff8a`), scanlines CRT, flicker, fonte monoespaçada, moldura RobCo.
A **TFT é sempre verde**. O menu "LEDS DA MESA" (Verde/Colorido/Branco/Standby) só comanda os
LEDs da tabela **física** via `sendToTable(modo)` — hoje um `console.log`; no hardware vira
comando serial/WiFi para fita WS2812/SK6812: `{"leds":"green|color|white|standby"}`.

## Átomo (ficha do elemento)
Modelo de Bohr animado em `<canvas>`: núcleo pulsante (símbolo + p/n) e camadas reais (`e.shells`)
com elétrons orbitando. Radioativos (`e.radioactive`) vibram + selo ☢ + "Geiger".

## Git
Repositório `main`, remoto `origin` → github.com/eduardogama-zero/pip-table.
```bash
git add -A && git commit -m "..."
git push
```
Para publicar demo: GitHub Pages → branch `main` / root → https://eduardogama-zero.github.io/pip-table/

## Roadmap (ver README)
LEDs reais via ESP32; órbitas reativas ao toque; busca/filtro; modo isótopos.
