select * from customer limit 10


-- Qual é a receita total gerada por clientes homens em comparação com clientes mulheres?
select
	gender,
	sum(purchase_amount) as receita
from customer
group by gender

-- Quais clientes usaram desconto, mas ainda assim gastaram mais do que o valor médio de compra?
select
	customer_id,
	purchase_amount
from customer
		where discount_applied = 'Yes'
		and purchase_amount >= (select avg(purchase_amount) from customer)

-- Quais são os 5 produtos com a maior média de avaliação (review rating)?
select * from customer limit 1
select distinct review_rating from customer

select item_purchased,
       round(avg(review_rating::numeric),2) as media_avaliacao_produto
from customer
group by item_purchased
order by media_avaliacao_produto desc
limit 5;

-- Qual é a diferença entre o valor médio de compra usando envio Standard e Express?
select * from customer limit 1
select
	shipping_type,
	round(avg(purchase_amount),2)
from customer
where shipping_type in ('Standard','Express')
group by shipping_type

-- Clientes assinantes gastam mais? Compare o gasto médio e a receita total entre assinantes e não assinantes.
select * from customer limit 1
select
	subscription_status,
	count(customer_id) as total_clientes,
	round(avg(purchase_amount),2) as gasto_medio,
	round(sum(purchase_amount),2) as receita_total
from customer
group by subscription_status
order by receita_total, gasto_medio

-- Quais 5 produtos têm a maior porcentagem de compras com desconto aplicado?
select * from customer limit 1
select
	item_purchased,
	round(100.0 * sum(
	case
		when discount_applied = 'Yes' then 1
		else 0
		end) / count(*),2) as taxa_desconto
from customer
group by item_purchased
order by taxa_desconto desc
limit 5

-- Segmentar os clientes em Novos, Recorrentes e Leais com base no número total de compras anteriores e mostrar a quantidade de clientes em cada segmento.
select * from customer limit 1

with tipo_cliente as (
select
	customer_id,
	previous_purchases,
	case
		when previous_purchases = 1 then 'Novo'
		when previous_purchases between 2 and 10 then 'Recorrente'
		else 'Leal'
		end as segmento_cliente
from customer)

select segmento_cliente,count(*) as "número de clientes" 
from tipo_cliente
group by segmento_cliente;

-- Quais são os 3 produtos mais comprados dentro de cada categoria?
select * from customer limit 1

with contagem_itens as(
	select category,
	item_purchased,
	count(customer_id) as total_pedidos,
	row_number() over (partition by category order by count (customer_id) desc) as classificacao_item
	from customer
	group by category, item_purchased
)

select 
	classificacao_item,
	category,
	item_purchased,
	total_pedidos
from contagem_itens
where classificacao_item <=3

-- Clientes que compram repetidamente (mais de 5 compras anteriores) também têm maior probabilidade de serem assinantes?
select * from customer limit 1

select
	subscription_status,
	count(customer_id) as compras_recorrentes
from customer
where previous_purchases > 5
group by subscription_status

-- Qual é a contribuição de receita de cada faixa etária?
select * from customer limit 1

select 
	age_group,
	sum(purchase_amount) as receita_total
from customer
group by age_group
order by receita_total desc;