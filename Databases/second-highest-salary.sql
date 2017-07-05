# select nth highest record

# highest
select max(salary) from employee # highest

# second highest
select max(salary)
from employee
where salary < (select max(salary) from employee)

# Nth highest from the last
select (
  select distinct Salary from Employee order by Salary Desc limit 1 offset 1
)as second

# limit 1 only returns one record
# offset strips the number of records mentioned from top/bottom - in given case top most one record and hence gives second highest number