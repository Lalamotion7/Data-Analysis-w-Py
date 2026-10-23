WITH clientes AS (
    SELECT * FROM {{ ref('int_clientes') }}
),

vendas AS (
    SELECT * FROM {{ ref('int_vendas') }}
),

estornos AS (
    SELECT * FROM {{ ref('int_estorno') }}
)

SELECT 
    c.customer_id,
    c.customer_name,
    c.customer_email,
    c.customer_phone,
    c.customer_address,
    COALESCE(SUM(v.total_price), 0) AS total_gasto,
    COUNT(v.purchase_id) AS total_compras,
    COUNT(DISTINCT v.product_id) AS diversidade_produtos,
    COUNT(e.purchase_id) AS total_estornos
FROM clientes c
LEFT JOIN vendas v ON c.customer_id = v.customer_id
LEFT JOIN estornos e ON v.purchase_id = e.purchase_id
GROUP BY c.customer_id, c.customer_name, c.customer_email, c.customer_phone, c.customer_address