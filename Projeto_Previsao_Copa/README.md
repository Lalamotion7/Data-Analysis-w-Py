# 🏆 Motor Preditivo Copa 2026 | Data Analytics Dashboard

![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

Um pipeline de dados *end-to-end* e dashboard analítico construído para simular probabilidades reais dos confrontos da Copa do Mundo. 

O projeto nasceu de uma brincadeira para o bolão do setor de TI, mas evoluiu para uma aplicação robusta focada em contornar bloqueios de extração de dados e aplicar modelagem matemática avançada (abandonando análises superficiais de "vitória/derrota").

## 📸 Prévia do Projeto

![Dashboard Preview](img/dashboard.png)

## 🧠 Arquitetura e Modelagem de Dados

Aplicativos comuns de prognósticos usam estatísticas superficiais. Este motor foca no que realmente dita o ritmo do jogo, cruzando três variáveis pesadas no algoritmo em JavaScript:

* **Expected Goals (xG):** Ignoramos a sorte. A matemática olha para a qualidade real das chances criadas, não apenas para o placar final.
* **Força Cúbica (Strength of Schedule):** Algoritmo de correção que esmaga as estatísticas infladas de seleções medianas que jogam contra times muito fracos nas eliminatórias.
* **Semelhança Tática:** O motor identifica times com métricas de posse e criação parecidas para calcular a tendência real de anulação (empate) no meio-campo.
* **Blindagem de Ponto Flutuante:** Lógica matemática rigorosa que garante a distribuição das probabilidades em exatos `100%`, evitando o clássico erro de arredondamento de front-end.

## 🛠️ Tecnologias Utilizadas

### Engenharia de Dados (Back-end)
* **Python 3**
* **curl_cffi:** Utilizado para bypass avançado de segurança (TLS Fingerprinting) da API do Sofascore.
* **Selenium:** Automação de navegação para raspar o calendário dinâmico e histórico de jogos.
* **JSON:** Estruturação e tratamento de dados ausentes (Missing Data) em partidas sem cobertura de xG.

### Front-end Analytics (Single Page Application)
* **HTML5 / CSS3:** Interface com efeito *Glassmorphism*, paleta dark mode e construções táticas (campo de futebol e jogadores) criadas puramente via CSS.
* **JavaScript (Vanilla):** Motor matemático principal, geração de gráficos em SVG puro (Radar Tático e Sparklines) sem dependência de bibliotecas externas como Chart.js.

## 🚀 Como Executar o Projeto Localmente

Como o dashboard consome arquivos `.json` locais, abri-lo diretamente com um duplo clique no arquivo `.html` causará um erro de CORS no navegador. É necessário rodar um servidor local:

1. Clone ou baixe este repositório.
2. Abra o terminal na pasta do projeto.
3. Inicie o servidor embutido do Python:
   ```bash
   python -m http.server 8000
