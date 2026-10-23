{% docs __overview__ %}

# Bem-vindo ao Data Warehouse do E-commerce ShoesBR 🛒👟

## 📌 Sobre este projeto
Este projeto utiliza o **dbt (Data Build Tool)** para transformar e modelar os dados do e-commerce ShoesBR, organizando-os em **camadas estruturadas** para análise de negócios.

## 🔄 Estrutura de Transformação
1️⃣ **Staging** → Extração e padronização dos dados brutos.  
2️⃣ **Intermediate** → Modelos normalizados para facilitar agregações.  
3️⃣ **Marts** → Modelos finais otimizados para BI e análise.

## 📊 Modelos Principais
- `mart_clientes` → Consolida os clientes e seu total de compras.  
- `mart_produtos` → Agrega os produtos, total vendido e faturamento.  
- `mart_vendas` → Junta vendas com estornos para análise financeira.

## 🚀 Como Executar
- `dbt seed` → Executa os seeds (dados estáticos)
- `dbt run` → Executa todos os modelos
- `dbt test`  → Testa a integridade dos dados
- `dbt docs generate`  → Gera a documentação
- `dbt docs serve`  → Serve a documentação interativa
{% enddocs %}