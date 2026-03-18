# 🚚 Visão Executiva: Performance de Supply Chain

![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

## 📌 Contexto do Projeto
Este projeto é um dashboard executivo focado em **Logística e Supply Chain**, desenvolvido para monitorar o SLA de entregas, mapear gargalos operacionais e analisar o impacto financeiro de atrasos e sinistros (extravios/danos). 

O objetivo principal foi transformar uma base de dados transacional bruta em insights acionáveis para a diretoria de operações, respondendo a perguntas críticas de negócio, como o custo-benefício dos diferentes tipos de frete e a performance de transportadoras parceiras.

## 🛠️ Arquitetura e Tecnologias Utilizadas
O pipeline de dados foi construído de ponta a ponta:
* **Python (Pandas/Faker):** Geração e simulação de uma base de dados realista com 8.000 registros de pedidos, aplicando regras lógicas de negócio (SLA de frete Padrão vs. Expresso, variação de estados e percentuais de extravio).
* **PostgreSQL:** Armazenamento estruturado dos dados, simulando um ambiente de Data Warehouse / ERP.
* **Power BI & Power Query (ETL):** Conexão com o banco de dados, limpeza de colunas (tipagem de datas), criação de medidas avançadas em DAX e modelagem do painel.
* **Figma / PowerPoint:** UI/UX Design do background (estilo Glassmorphism) para criar uma interface limpa, intuitiva e focada na experiência do usuário.

## 💡 Principais Insights e Decisões de Negócio
Durante a análise exploratória e visual, identificamos pontos críticos na operação:

1. **O Ralo Financeiro do Frete Expresso:** O dashboard revelou que as taxas de atraso entre o Frete Padrão (29,32%) e o Frete Expresso (28,99%) são estatisticamente semelhantes. *Decisão de negócio sugerida:* Revisão imediata dos contratos de SLA com as transportadoras focadas em frete Expresso, pois o custo mais elevado não está se refletindo em eficiência na ponta para o cliente.
2. **Geografia dos Atrasos:** O mapa de calor destaca gargalos logísticos específicos, permitindo que a equipe de roteirização atue proativamente nos estados com maior saturação de atrasos.
3. **Análise de Sinistros:** A implementação de *tooltips* customizadas permite auditar a volumetria absoluta por trás das taxas percentuais, evitando falsas interpretações onde transportadoras com menor volume pareciam ter a pior performance de extravio.

## 📊 Visualização do Dashboard
O painel foi estruturado com foco em "Data-Ink Ratio" (Razão Dados-Tinta), priorizando a clareza e a interatividade:
* **Cabeçalho:** Filtros dinâmicos por Centro de Distribuição/Fábrica.
* **Linha Executiva:** KPIs de Total de Pedidos, Custo de Frete, Tempo Médio de Trânsito, Taxa de Atraso e Taxa de Extravio.
* **Corpo Analítico:** Rankings de ofensores (Transportadoras), evolução temporal (Mês/Ano) contínua e detalhamento de performance por tipo de frete.

## 👨‍💻 Contato
Projeto desenvolvido para demonstração de portfólio em Análise de Dados.
* **LinkedIn:** Laércio | linkedin.com/in/lalamotion7/
