select p.firstname, p.lastname, a.city, a.state
from person p
left join address a # cannot use inner join as it only returns the common values and we intend to have all relevant values returned
on p.personid = a.personid


select Person.FirstName, Person.LastName, Address.City, Address.State
from Person
left join Address
on Person.PersonId = Address.PersonId