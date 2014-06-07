SELECT states.name, points.name
FROM states, points
WHERE ST_Contains(states.geom, points.geom)