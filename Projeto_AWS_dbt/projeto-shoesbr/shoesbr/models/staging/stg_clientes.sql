WITH source AS (
    SELECT *
    FROM {{ source('landing', 'clientes') }}
),

renamed AS (
    SELECT 
        CAST(customer_id AS INT) AS customer_id,
        name AS customer_name,
        address AS customer_address,
        phone AS customer_phone,
        email AS customer_email
    FROM source
)

SELECT * FROM renamed