
    
    

with all_values as (

    select
        refund_reason as value_field,
        count(*) as n_records

    from "shoesbr"."staging"."stg_estorno"
    group by refund_reason

)

select *
from all_values
where value_field not in (
    'Produto com defeito','Arrependimento','Entrega atrasada','Produto incorreto','Outro'
)


