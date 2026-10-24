WITH source AS (
    SELECT *
    FROM {{source ('landing', 'produtos')}}
),

renamed AS (
    SELECT
        CAST (product_id AS INT) AS product_id,
        name AS name_product,
        price as price_product
    FROM source
)

SELECT * FROM renamed