# consective same records

select log1.Num as "ConsectiveNums"
from log log1, log log2, log log3
where (log2.id - log1.id = 1 and log3.id - log2.id = 1)
and (log1.Num = log2.Num and log2.Num = log3.Num)