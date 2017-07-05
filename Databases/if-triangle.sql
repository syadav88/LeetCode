# if this is a triangle

select case
when
(A+B<=C) or (B+C<=A) or (C+A<=B) then "False"
else "True"
end
from triangles;