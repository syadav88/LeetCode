# self join

select employee.name
from employee
join manager 
on employee.managerid = manager.id
where employee.salary>manager.salary

select emp.name
from employee emp, employee man
where emp.managerid = man.id and emp.salary>man.salary