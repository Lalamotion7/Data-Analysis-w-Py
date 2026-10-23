WITH source AS (
    SELECT *
    FROM {{ ref('stg_estorno') }}
)

SELECT * FROM source