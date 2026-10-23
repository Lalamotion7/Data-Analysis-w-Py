
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    

select
    purchase_id as unique_field,
    count(*) as n_records

from "shoesbr"."staging"."stg_vendas"
where purchase_id is not null
group by purchase_id
having count(*) > 1



  
  
      
    ) dbt_internal_test