# PIP-TABLE 3000 ☢

Tabela periódica interativa em estilo **Fallout / Pip-Boy** para tela **TFT touch (800×480)**.
Protótipo web (HTML/CSS/JS puro, arquivo único) que serve de espelho visual para o produto físico.

![status](https://img.shields.io/badge/status-prot%C3%B3tipo-41ff8a)
![elementos](https://img.shields.io/badge/elementos-118-41ff8a)

## ✨ Recursos

- **118 elementos** com número atômico, massa, grupo/período, categoria, configuração eletrônica e descrição (PT-BR).
- **Estética Pip-Boy**: fósforo verde, scanlines de CRT, flicker, fonte monoespaçada, moldura RobCo.
- **Toque em qualquer elemento** → ficha completa com **átomo de Bohr animado** (núcleo pulsante com prótons/nêutrons + camadas eletrônicas reais orbitando).
- **Elementos radioativos** (Tc, Pm e do Po em diante) ganham selo ☢, vibração do núcleo e "Geiger".
- **Menu "LEDS DA MESA"**: comanda os LEDs da tabela **física** (Verde / Colorido / Branco / Standby).
  A TFT permanece sempre verde; o menu só dispara o comando para o controlador.

## 🚀 Rodar localmente

Abra o `index.html` em qualquer navegador. Sem dependências, sem build.

> Projetado para **800×480**. Em desktop, use a janela nesse tamanho para ver o layout final.

## 🌐 Demo online (GitHub Pages)

Após publicar, ative em **Settings → Pages → Branch: `main` / root**.
A demo fica em: `https://<seu-usuario>.github.io/pip-table/`

## 🔌 Integração com o hardware

O menu chama `sendToTable(modo)` (em `index.html`), que hoje só faz `console.log`.
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

Os dados dos elementos vivem em `src/elements.json` e são **embutidos** no `index.html`.
Para regenerar após editar:

```bash
cd src
python3 gen_data.py      # (re)cria elements.json com massas, posições e camadas
python3 build_html.py     # injeta os dados e escreve ../index.html  (ajuste o caminho de saída)
```

> `build_html.py` foi escrito para o ambiente do protótipo; ajuste os caminhos absolutos no topo do arquivo para o seu diretório antes de rodar.

## 📁 Estrutura

```
index.html            → app completo (dados embutidos)
src/gen_data.py       → gera os dados dos 118 elementos (+ camadas eletrônicas)
src/elements.json     → base de dados dos elementos
src/build_html.py     → monta o index.html a partir do template + dados
LICENSE               → MIT
```

## 🗺️ Roadmap

- [ ] Comando real dos LEDs via ESP32/serial (WS2812)
- [ ] Órbitas reativas ao toque (segurar acelera; toque = salto de elétron)
- [ ] Busca / filtro por categoria
- [ ] Modo isótopos no núcleo

---

Feito por **Eduardo Gama** · MIT License
