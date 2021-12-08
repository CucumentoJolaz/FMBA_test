select goods_type.goods_type_id, goods_type_name, qty_of_cat from 
(select SUM(qty_of_product) as "qty_of_cat", goods_type_id  from

(select SUM(total) as "qty_of_product", goods_id
from orders 
group by goods_id 
order by 1 desc) sub_query join goods
on sub_query.goods_id = goods.goods_id
group by goods_type_id 
order by qty_of_cat desc) cat_qty join goods_type
on cat_qty.goods_type_id = goods_type.goods_type_id
where qty_of_cat = (select max(qty_of_cat) from (select SUM(qty_of_product) as "qty_of_cat", goods_type_id  from

(select SUM(total) as "qty_of_product", goods_id
from orders 
group by goods_id 
order by 1 desc) sub_query join goods
on sub_query.goods_id = goods.goods_id
group by goods_type_id 
order by qty_of_cat desc) o
				   )
order by qty_of_cat
desc