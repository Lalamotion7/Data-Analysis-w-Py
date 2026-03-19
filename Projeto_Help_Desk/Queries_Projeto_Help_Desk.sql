create table help_desk_tickets_clean as
select 
    id_chamado,
    data_abertura,
    data_fechamento,
    categoria,
    prioridade,
    status,
    satisfacao_usuario,
    -- Criando a nova coluna de SLA
    case 
        when data_fechamento is not null then 
            ROUND((extract(EPOCH from (data_fechamento - data_abertura)) / 3600)::numeric, 2)
        else null 
    end as tempo_resolucao_horas
from help_desk_tickets;

-- Checando a nova tabela
select * from help_desk_tickets_clean limit 5


-- Qual é o tempo médio de resolução para cada nível de Prioridade?
select 
    prioridade,
    ROUND(avg(tempo_resolucao_horas), 2) as media_horas_resolucao
from help_desk_tickets_clean
where tempo_resolucao_horas is not null -- Ignora o backlog de chamados abertos
group by prioridade
order by media_horas_resolucao asc; -- Ordena do mais rápido para o mais lento

-- Qual categoria de chamado é a que mais leva tempo para ser resolvida?
select
	categoria,
	round(avg(tempo_resolucao_horas), 2) as media_horas_resolucao
from help_desk_tickets_clean
where tempo_resolucao_horas is not null
group by categoria
order by media_horas_resolucao desc;

-- Qual a média de chamados por categoria?
select
	categoria,
	count(id_chamado) as qtd_chamados
from help_desk_tickets_clean
group by categoria
order by qtd_chamados desc

-- Qual a nota média de avaliação de usuários aos nossos serviços?
select
	round(avg(satisfacao_usuario)::numeric, 2) as nota_media_avaliacao
from help_desk_tickets_clean

-- Avaliação média por categoria de chamado
select * from help_desk_tickets_clean limit 1
select
	categoria,
	round(avg(satisfacao_usuario)::numeric, 2) as nota_media_avaliacao
from help_desk_tickets_clean
group by categoria
order by nota_media_avaliacao desc