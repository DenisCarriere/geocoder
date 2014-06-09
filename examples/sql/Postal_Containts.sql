select kingston.location, postal.fsa
from kingston, postal
WHERE ST_Contains(postal.geom, kingston.geom)