# 📊 Pipeline Analítico: Comportamento de Compra de Clientes

Neste projeto, desenvolvi um pipeline de dados completo (End-to-End) focado em entender os padrões de consumo e os geradores de receita de uma loja de varejo. O objetivo foi transformar dados brutos em um dashboard estratégico para tomada de decisão.

## 🛠️ Stack Tecnológico
* **Python (Pandas & SQLAlchemy):** Limpeza, higienização e carga automatizada de dados (ETL).
* **PostgreSQL:** Análise exploratória avançada com CTEs e Window Functions.
* **Power BI:** Modelagem, DAX e Data Storytelling com foco em UI/UX (Dark Mode).

## 🖼️ O Dashboard Final
O resultado das análises gerou esta visualização interativa, construída para apresentar os dados de forma clara e direta para gestores:

![Projeto_Comportamento_Clientes]([https://github.com/Lalamotion7/Data-Analysis-w-Py/blob/main/Projeto_Comportamento_Clientes/Dashboard.png?raw=true])

## 🔍 Principais Insights Extraídos (SQL & Python)
1. **Recorrência e Retenção:** Identificamos através de queries no banco relacional como o status de assinatura impacta o volume de compras repetidas.
2. **Receita por Categoria:** Mapeamento de quais tipos de produtos (ex: Clothing, Accessories) trazem maior retorno financeiro isolado e agrupado.
3. **Padrão de Envio:** Cruzamento entre o método de envio (Standard vs Express) e o ticket médio dos clientes.

## 📁 Estrutura dos Arquivos
* `Comportamentos_Compra_Clientes.ipynb`: Script de extração e tratamento inicial em Python.
* `Comportamento_Clientes_Queries.sql`: Consultas avançadas utilizadas para responder às perguntas de negócio.

* ## 🔒 Segurança e Boas Práticas (Data Ops)
Para garantir a integridade e a segurança do pipeline, a conexão do script Python com o banco de dados PostgreSQL foi estruturada utilizando variáveis de ambiente (`.env` e `python-dotenv`). Isso assegura que as credenciais e rotas do servidor não fiquem expostas no código-fonte público (prática de *Secret Management*).

---
*Projeto desenvolvido para consolidar a transição de carreira para Análise de Dados, aplicando práticas de mercado na resolução de problemas de negócio.*
