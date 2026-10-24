
  
    

  create  table "shoesbr"."marts"."fct_vendas__dbt_tmp"
  
  
    as
  
  (
    WITH vendas AS (
    SELECT * FROM "shoesbr"."intermediate"."int_vendas"
),

estornos AS (
    SELECT * FROM "shoesbr"."intermediate"."int_estorno"
),

clientes AS (
    SELECT * FROM "shoesbr"."intermediate"."int_clientes"
),

produtos AS (
    SELECT * FROM "shoesbr"."intermediate"."int_produtos"
)

SELECT 
    v.purchase_id,
    v.customer_id,
    c.customer_name,
    c.customer_email,
    v.product_id,
    p.name_product,
    v.purchase_date,
    v.quantity,
    v.total_price,
    v.payment_method,
    COALESCE(e.refund_amount, 0) AS valor_estornado,
    e.refund_reason,
    (v.total_price - COALESCE(e.refund_amount, 0)) AS receita_liquida
FROM vendas v
LEFT JOIN estornos e ON v.purchase_id = e.purchase_id
LEFT JOIN clientes c ON v.customer_id = c.customer_id
LEFT JOIN produtos p ON v.product_id = p.product_id
  );
  