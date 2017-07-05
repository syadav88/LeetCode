# departments highest salary

select d.name as Department, e.name as Employee, e.salary as salary
from employee e, department d
where e.departmentid = d.id
and (departmentid, salary) in (select departmentid, max(salary) from employee group by departmentid)

Select Department.Name as Department, emp1.Name as Employee, emp1.Salary as Salary from 
Employee emp1 join Department on emp1.DepartmentId = Department.Id
where emp1.Salary = (Select Max(Salary) from Employee emp2 where emp2.DepartmentId = emp1.DepartmentId);