📊 Dashboard Analítico: Auditoria de Help Desk & Qualidade (NOC)
📝 Sobre o Projeto
Este projeto foi desenvolvido para transformar dados brutos de um sistema de Help Desk em inteligência operacional pura. O foco vai muito além de "contar chamados": o objetivo é combater o "Efeito Melancia" (indicadores verdes que escondem insatisfação) identificando gargalos reais de produtividade, falhas de SLA e a causa raiz das reclamações dos usuários finais.

Baseado em uma volumetria de 5.000 chamados, o painel simula uma operação real de suporte, entregando ao coordenador de TI uma ferramenta de investigação acionável para tomada de decisão.

🚀 Principais Funcionalidades & Insights de Negócio

Auditoria de Detratores (Drill-through): O grande diferencial do painel. Uma página oculta de auditoria que, com um clique, cruza notas baixas (1 e 2) com o status do SLA, gerando uma lista nominal dos IDs dos chamados ofensores para o gestor atuar.

Alertas Visuais de Gargalo: Formatação condicional destacando em vermelho SLAs "Estourados" diretamente na tabela de auditoria.

Monitoramento de SLA & Tooltips: Acompanhamento dinâmico que revela se a insatisfação do cliente foi causada por atraso de processo ou falha no atendimento humano.

Análise de Produtividade e Sazonalidade: Comparativo para identificação de picos de demanda, permitindo otimização de escalas de plantão.

🛠️ Stack Tecnológico (O que usei)

Python (Pandas): Pipeline de ETL, limpeza de dados complexos e correção de inconsistências temporais (virada de ano calendário).

PostgreSQL: Armazenamento, estruturação e consultas SQL para modelagem da base de dados.

Power BI (DAX Avançado): Modelagem Star Schema (Fato e Dimensões), criação de dCalendario dinâmica, medidas de Desvio de Satisfação e relacionamentos complexos.

UI/UX Design (Figma): Background desenvolvido do zero em Dark Mode, navegação via sidebar retrátil, garantindo a usabilidade de um "sistema web" e não apenas de uma planilha.

📸 Visual do Dashboard <div align="center">
  <img src="https://github.com/Lalamotion7/Data-Analysis-w-Py/blob/main/Projeto_Help_Desk/Dashboard_Help_Desk.JPG?raw=true">
</div>
<div align="center">
  <img src="https://github.com/Lalamotion7/Data-Analysis-w-Py/blob/main/Projeto_Help_Desk/Drill-Through.JPG?raw=true">
</div>

👨‍💻 Autor
Laércio
Especialista em Suporte TI | Analista de Dados
linkedin.com/in/lalamotion7/
