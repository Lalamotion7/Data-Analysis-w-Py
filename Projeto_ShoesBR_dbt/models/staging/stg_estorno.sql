WITH source AS (
    SELECT *
    FROM {{ source('landing', 'estorno') }}
),

renamed AS (
    SELECT 
        CAST(purchase_id AS INT) AS purchase_id,
        CAST(customer_id AS INT) AS customer_id,
        CAST(product_id AS INT) AS product_id,
        CAST(refund_date AS DATE) AS refund_date,
        refund_reason,
        CAST(refund_amount AS DECIMAL(10,2)) AS refund_amount
    FROM source
)

SELECT * FROM renamed