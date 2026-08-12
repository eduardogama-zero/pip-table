# CLAUDE.md — PIP-TABLE 3000

Contexto para o Claude Code manter este projeto.

## O que é
Tabela periódica interativa estilo **Fallout / Pip-Boy** para **tela TFT touch 800×480**.
A **página é gerada 100% em Python** (stdlib pura, **sem dependências externas**); `index.html`
é o artefato/preview e espelha o produto físico (tabela real com LEDs endereçáveis atrás dos elementos).

## Runtime × build (importante p/ o hardware)
- **Runtime (a TFT)**: só o `index.html` — arquivo único **auto-contido**, sem CDN/fetch/fonte
  externa (só fontes de sistema). É o que roda no hardware. Não adicionar dependências de runtime
  (nada de `<script src>` externo, web fonts, CDNs) — inviabiliza a tela.
- **Build (máquina de dev)**: Python 3, stdlib pura. Gera o `index.html`. Nada disso vai para a TFT.

## Arquitetura / fonte da verdade
- **`pip_table/data.py`** — ÚNICA fonte de dados dos 118 elementos (lista `E`). `elements()`
  devolve os dicts já com os campos derivados `shells` (aufbau), `protons`, `neutrons`, `radioactive`.
- **`pip_table/templates/page.html`** — a página inteira: CSS + os marcadores `__CELLS__`,
  `__LEGEND__`, `__COUNT__`, `__ELEMENTS_JSON__` + o JS de interação. É aqui que se mexe em visual/UI.
- **`pip_table/render.py`** — injeta grade/legenda/contagem/dados no template via `str.replace`
  (stdlib pura, `html.escape` nos textos). Sem Jinja nem qualquer dependência.
- **`pip_table/builder.py`** / **`build.py`** — escrevem `index.html`.
- **`index.html`** — artefato gerado. **Não editar à mão**; é sobrescrito pelo build.
  Marcado como `linguist-generated` no `.gitattributes` (não conta como linguagem no GitHub).

### Divisão Python × JavaScript
- **Python gera o conteúdo estático**: células dos 118 elementos, marcadores 57-71/89-103,
  legenda, rodapé. Antes isso era montado por JS no cliente — agora é HTML no `index.html`.
- **JS só faz comportamento** (não dá para gerar em Python): animação do átomo em `<canvas>`,
  abertura da ficha ao toque, menu de LEDs e navegação por teclado. Os dados para essas
  interações continuam embutidos como JSON (`const ELEMENTS = ...`) injetado pelo template.

### Pipeline de build
```bash
python build.py   # regera ../index.html a partir de data.py + page.html (sem instalar nada)
```

## Regras importantes
- Alterou dados de elemento (massa, categoria, descrição, posição)? → editar a lista `E` em
  `pip_table/data.py` e rodar `python build.py`.
- Alterou visual/UI/lógica (CSS, canvas do átomo, menu, grade)? → editar `pip_table/templates/page.html`
  e rodar `python build.py`.
- Nunca editar `index.html` à mão; será sobrescrito.
- Não introduzir dependências: manter render em stdlib pura; runtime da TFT sem recursos externos.
- Após mudar, confira: `index.html` deve ter 118 ocorrências de `class="cell cat-`, `id="atom"`
  presente e nenhum marcador `__…__` residual (template não substituído).

## Estética (não quebrar)
Verde fósforo (`--green:#41ff8a`), scanlines CRT, flicker, fonte monoespaçada, moldura RobCo.
A **TFT é sempre verde**. O menu "LEDS DA MESA" (Verde/Colorido/Branco/Standby) só comanda os
LEDs da tabela **física** via `sendToTable(modo)` — hoje um `console.log`; no hardware vira
comando serial/WiFi para fita WS2812/SK6812: `{"leds":"green|color|white|standby"}`.

## Átomo (ficha do elemento)
Átomo animado em `<canvas>` com **dois modelos alternáveis** pelo botão MODELO (`toggleModel()`,
var `atomModel`): `drawBohr` (órbitas circulares concêntricas) e `drawEllipse` (elipses inclinadas
que se cruzam, estilo era-atômica; precessão lenta `spin`). Ambos usam as primitivas compartilhadas
`drawNucleus` (núcleo pulsante, símbolo + p/n) e `drawElectron`, e as camadas reais (`e.shells`).
Radioativos (`e.radioactive`) vibram (jitter) + selo ☢ + "Geiger". Default: Atômico (elíptico);
a escolha persiste entre elementos. Ao mudar o default, alinhar `atomModel` (em page.html) com
o rótulo inicial do botão `#modelBtn`.

## Git
Repositório `main`, remoto `origin` → github.com/eduardogama-zero/pip-table.
```bash
git add -A && git commit -m "..."
git push
```
Para publicar demo: GitHub Pages → branch `main` / root → https://eduardogama-zero.github.io/pip-table/

## Roadmap (ver README)
LEDs reais via ESP32; órbitas reativas ao toque; busca/filtro; modo isótopos.
