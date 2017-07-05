# type of triangle

select case
when (A+B>C) or (B+C>A) or (C+A>B) then
	case
	when (A=B) and (B=C) then "Equilateral"
	when (A=B) or (B=C) or (C=A) then "Isoceles"
	else "Scalene"
else "Not a trainagle"
end
from triangles;
