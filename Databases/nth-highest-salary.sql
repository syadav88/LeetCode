# Nth highest number

select distinct salary
from employee
order by salary desc
limit 1
offset (N-1)

# for second highest, you want to offset by highest - 1
# for third highest, you need to offset by top 2 and, so on