WITH produtos AS (
    SELECT * FROM "shoesbr"."intermediate"."int_produtos"
),

vendas AS (
    SELECT * FROM "shoesbr"."intermediate"."int_vendas"
),

estornos AS (
    SELECT * FROM "shoesbr"."intermediate"."int_estorno"
)

SELECT 
    p.product_id,
    p.name_product,
    p.price_product,
    COALESCE(SUM(v.quantity), 0) AS total_vendido,
    COALESCE(SUM(v.total_price), 0) AS total_faturado,
    COALESCE(SUM(e.refund_amount), 0) AS total_estornado,
    COUNT(DISTINCT e.purchase_id) AS total_estornos
FROM produtos p
LEFT JOIN vendas v ON p.product_id = v.product_id
LEFT JOIN estornos e ON v.purchase_id = e.purchase_id
GROUP BY p.product_id, p.name_product, p.price_product