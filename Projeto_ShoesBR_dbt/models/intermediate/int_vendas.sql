WITH vendas AS (
    SELECT * FROM {{ ref('stg_vendas') }}
),

estornos AS (
    SELECT purchase_id, refund_amount, refund_reason
    FROM {{ ref('stg_estorno') }}
)

SELECT 
    v.purchase_id,
    v.customer_id,
    v.product_id,
    v.purchase_date,
    v.quantity,
    v.total_price,
    v.payment_method,
    COALESCE(e.refund_amount, 0) AS valor_estornado,
    e.refund_reason
FROM vendas v
LEFT JOIN estornos e ON v.purchase_id = e.purchase_id
