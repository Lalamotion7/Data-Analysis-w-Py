
  create view "shoesbr"."intermediate"."int_estorno__dbt_tmp"
    
    
  as (
    WITH source AS (
    SELECT *
    FROM "shoesbr"."staging"."stg_estorno"
)

SELECT * FROM source
  );