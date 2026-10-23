WITH produtos AS (
    SELECT * FROM {{ ref('stg_produtos') }}
),

vendas AS (
    SELECT product_id, 
    SUM(quantity) AS total_vendido, 
    SUM(total_price) AS total_faturado
    FROM {{ ref('stg_vendas') }}
    GROUP BY product_id
)

SELECT 
    p.product_id,
    p.name_product,
    p.price_product,
    COALESCE(v.total_vendido, 0) AS total_vendido,
    COALESCE(v.total_faturado, 0) AS total_faturado
FROM produtos p
LEFT JOIN vendas v ON p.product_id = v.product_id
ORDER BY total_faturado DESC