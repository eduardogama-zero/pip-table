# PIP-TABLE 3000 ☢

Tabela periódica interativa em estilo **Fallout / Pip-Boy** para tela **TFT touch (800×480)**.
Protótipo web que serve de espelho visual para o produto físico — a **página é gerada 100% em Python**
(stdlib pura, **sem dependências externas**), e a preview é o `index.html` resultante.

![status](https://img.shields.io/badge/status-prot%C3%B3tipo-41ff8a)
![elementos](https://img.shields.io/badge/elementos-118-41ff8a)
![python](https://img.shields.io/badge/gerado%20em-Python%203-41ff8a)
![deps](https://img.shields.io/badge/depend%C3%AAncias-0-41ff8a)

## ✨ Recursos

- **118 elementos** com número atômico, massa, grupo/período, categoria, configuração eletrônica e descrição (PT-BR).
- **Estética Pip-Boy**: fósforo verde, fonte monoespaçada, moldura RobCo e camada de **efeitos CRT sutis** — scanlines, flicker, grão de fósforo, reflexo de vidro e barra de varredura rolando.
- **Sons de interface** sintetizados na hora (Web Audio, **sem arquivos**): bip ao selecionar, cliques nos botões, e um **Geiger de fundo sutil** que crepita enquanto a ficha de um elemento radioativo está aberta (para ao fechar ou ao ir para um estável).
- **Toque em qualquer elemento** → ficha completa com **átomo animado** (núcleo pulsante com prótons/nêutrons + camadas eletrônicas reais orbitando), em **dois modelos alternáveis** pelo botão MODELO: *Atômico* (elipses inclinadas cruzando, estilo era-atômica — padrão) e *Bohr* (órbitas circulares).
- **Elementos radioativos** (Tc, Pm e do Po em diante) ganham selo ☢, vibração do núcleo e "Geiger".
- **Painel de configurações** (ícone de engrenagem ⚙ no cabeçalho) recolhe os controles para não poluir a tela: liga/desliga do **som** e o **"LEDS DA MESA"** (Verde / Colorido / Branco / Standby), que comanda os LEDs da tabela **física**. A TFT permanece sempre verde; o menu só dispara o comando para o controlador. Fecha ao clicar fora.

## 🐍 Como funciona (100% Python, zero dependências)

Toda a página é montada por Python — a grade dos 118 elementos, os marcadores dos
lantanídeos/actinídeos e a legenda são **renderizados** no template e injetados por
`render.py` (stdlib pura, sem bibliotecas externas), não construídos por JavaScript no navegador.

O JavaScript embutido cuida apenas do que é *comportamento* e não existe sem navegador:
a animação do átomo em `<canvas>`, a abertura da ficha ao toque, o menu de LEDs e o teclado.

> **Roda numa TFT?** O que vai para o hardware é só o `index.html` — um único arquivo
> **auto-contido** (sem CDN, sem fetch, sem fonte externa; só fontes de sistema). O Python é
> ferramenta de *build* na sua máquina; **nada dele vai para a tela**.

```
pip_table/data.py            → fonte única dos 118 elementos (+ camadas, prótons, nêutrons, radioativo)
pip_table/templates/         → page.html (a página: CSS + marcadores + JS de interação)
pip_table/render.py          → injeta grade/legenda/dados no template (stdlib pura)
pip_table/builder.py         → escreve o index.html
build.py                     → entrada: `python build.py`
index.html                   → artefato gerado (a preview / o que roda na TFT)
```

## 🚀 Rodar localmente

Abra o `index.html` em qualquer navegador — a preview já está pronta no repositório.

> Projetado para **800×480**. Em desktop, use a janela nesse tamanho para ver o layout final.

## 🔧 Regenerar a página

Requer só **Python 3.8+** (nenhuma dependência para instalar).

```bash
python build.py   # regera o index.html a partir dos dados + template
```

## 🌐 Demo online (GitHub Pages)

Ative em **Settings → Pages → Branch: `main` / root**.
A demo fica em: `https://eduardogama-zero.github.io/pip-table/`

## 🔌 Integração com o hardware

O menu chama `sendToTable(modo)` (no template `page.html`), que hoje só faz `console.log`.
No hardware, troque esse corpo por um comando serial/WiFi para a fita de LED endereçável (WS2812/SK6812):

```json
{ "leds": "green" | "color" | "white" | "standby" }
```

Sugestão de mapeamento:
- **color** → cor por categoria/elemento (a mesma paleta da legenda)
- **white** → todos os canais em branco
- **standby** → PWM/brilho baixo para economia
- **green** → verde padrão Pip-Boy

## 🛠️ Editar os dados

Os dados dos elementos vivem em `pip_table/data.py` (a lista `E`). Para alterar massa,
categoria, descrição ou posição, edite a tupla do elemento e rode `python build.py`.
Para mudar o visual/UI/lógica (CSS, canvas do átomo, menu), edite `pip_table/templates/page.html`.

## 🗺️ Roadmap

- [ ] Comando real dos LEDs via ESP32/serial (WS2812)
- [ ] Órbitas reativas ao toque (segurar acelera; toque = salto de elétron)
- [ ] Busca / filtro por categoria
- [ ] Modo isótopos no núcleo

---

Feito por **Eduardo Gama** · MIT License
