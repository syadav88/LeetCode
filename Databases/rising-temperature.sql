# one day difference between dates

select table2.temperature
from weather table1, weather table2
where table2.temperature>table1.temperature
and to_days(table2.date)-to_days(table1.date) = 1