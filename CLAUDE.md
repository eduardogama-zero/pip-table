# CLAUDE.md — PIP-TABLE 3000

Contexto para o Claude Code manter este projeto.

## O que é
Tabela periódica interativa estilo **Fallout / Pip-Boy** para **tela TFT touch 800×480**.
Protótipo web de arquivo único (`index.html`) que serve de espelho visual do produto físico
(uma tabela periódica real com LEDs endereçáveis atrás dos elementos).

## Arquitetura / fonte da verdade
- **`src/gen_data.py`** — ÚNICA fonte de dados dos 118 elementos. Gera `src/elements.json`
  com: `n, sym, name(pt), mass, cat, x, y, cfg, desc` **e** os campos derivados
  `shells` (camadas eletrônicas via aufbau), `protons`, `neutrons`, `radioactive`.
- **`src/build_html.py`** — injeta `src/elements.json` no template HTML e escreve `index.html` na raiz.
- **`index.html`** — app final (dados embutidos). **Não editar dados aqui**; editar em `gen_data.py`.

### Pipeline de build (sempre nesta ordem)
```bash
cd src
python3 gen_data.py     # (re)gera src/elements.json
python3 build_html.py   # regenera ../index.html a partir do template + dados
```
Caminhos são relativos ao script — roda em qualquer máquina, sem dependências além do Python 3.

## Regras importantes
- Alterou dados de elemento (massa, categoria, descrição, posição)? → editar `E=[...]` em `gen_data.py` e rodar o pipeline.
- Alterou visual/UI/lógica (CSS, canvas do átomo, menu)? → editar o template dentro de `build_html.py` (variável `html`) e rodar `build_html.py`.
- Nunca editar `index.html` à mão para conteúdo que venha do pipeline; será sobrescrito.
- Após qualquer mudança, confira: `index.html` deve ter ~47KB, `id="atom"` presente e 118 ocorrências de `"n":`.

## Estética (não quebrar)
Verde fósforo (`--green:#41ff8a`), scanlines CRT, flicker, fonte monoespaçada, moldura RobCo.
A **TFT é sempre verde**. O menu "LEDS DA MESA" (Verde/Colorido/Branco/Standby) só comanda os
LEDs da tabela **física** via `sendToTable(modo)` — hoje um `console.log`; no hardware vira
comando serial/WiFi para fita WS2812/SK6812: `{"leds":"green|color|white|standby"}`.

## Átomo (ficha do elemento)
Modelo de Bohr animado em `<canvas>`: núcleo pulsante (símbolo + p/n) e camadas reais (`e.shells`)
com elétrons orbitando. Radioativos (`e.radioactive`) vibram + selo ☢ + "Geiger".

## Git
Repositório já inicializado (branch `main`). Fluxo de manutenção:
```bash
git add -A && git commit -m "..."      # commitar mudanças
git remote add origin <url>            # 1ª vez
git push -u origin main
```
Para publicar demo: GitHub Pages → branch `main` / root → https://<user>.github.io/pip-table/

## Roadmap (ver README)
LEDs reais via ESP32; órbitas reativas ao toque; busca/filtro; modo isótopos.
