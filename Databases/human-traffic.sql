# more than n consective rows based on a condition

select t.* FROM table t
left join table t1 on t.id-1 = t1.id
left join table t2 on t.id-2 = t2.id
left join table t3 on t.id+1 = t3.id
left join table t4 on t.id+2 = t4.id

where 
(t.people>=100 and t1.people>=100 and t2.people>=100) OR
(t.people>=100 and t3.people>=100 and t4.people>=100) OR
(t.people>=100 and t1.people>=100 and t3.people>=100)
ORDER by id;


SELECT t.* FROM stadium t
    LEFT JOIN stadium p1 ON t.id - 1 = p1.id
    LEFT JOIN stadium p2 ON t.id - 2 = p2.id
    LEFT JOIN stadium n1 ON t.id + 1 = n1.id
    LEFT JOIN stadium n2 ON t.id + 2 = n2.id
WHERE (t.people >= 100 AND p1.people >= 100 AND p2.people >= 100)
     OR (t.people >= 100 AND n1.people >= 100 AND n2.people >= 100)
     OR (t.people >= 100 AND n1.people >= 100 AND p1.people >= 100)
ORDER BY id;
