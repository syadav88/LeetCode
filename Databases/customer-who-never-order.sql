# sub query

select customer.name
from customer
where customer.id not in (select orders.id from orders)