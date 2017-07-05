# delete duplicate  - self join

delete table2
	from emailtable table1, emailtable table2
	where table2.id>table1.id
	and table2.email = table1.email