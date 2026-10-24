
    
    

select
    purchase_id as unique_field,
    count(*) as n_records

from "shoesbr"."staging"."stg_estorno"
where purchase_id is not null
group by purchase_id
having count(*) > 1


