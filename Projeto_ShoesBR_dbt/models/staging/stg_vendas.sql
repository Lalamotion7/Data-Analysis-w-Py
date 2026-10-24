WITH source AS (
    SELECT *
    FROM {{ source('landing', 'vendas') }}
),

renamed AS (
    SELECT
        CAST (purchase_id AS INT) AS purchase_id,
        CAST (customer_id AS INT) AS customer_id,
        CAST (product_id AS INT) AS product_id,
        CAST (date AS DATE) AS purchase_date,
        CAST (quantity AS INT) AS quantity,
        CAST (total_price AS DECIMAL(10,2)) AS total_price,
        payment_method
    FROM source
)

SELECT * FROM renamed