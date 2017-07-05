select class from courses
group by class
having count(distinct student) >= 5

select class from courses
group by class
having count(student) >= 5