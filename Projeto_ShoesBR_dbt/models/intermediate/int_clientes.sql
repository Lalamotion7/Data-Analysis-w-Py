WITH clientes AS (
    SELECT * FROM {{ ref('stg_clientes') }}
),

vendas AS (
    SELECT customer_id, SUM(total_price) AS total_gasto, COUNT(*) AS total_compras
    FROM {{ ref('stg_vendas') }}
    GROUP BY customer_id
)

SELECT 
    c.customer_id,
    c.customer_name,
    c.customer_address,
    c.customer_phone,
    c.customer_email,
    COALESCE(v.total_gasto, 0) AS total_gasto,
    COALESCE(v.total_compras, 0) AS total_compras
FROM clientes c
LEFT JOIN vendas v ON c.customer_id = v.customer_id
ORDER BY total_compras DESC
