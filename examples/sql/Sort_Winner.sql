SELECT p1.provider, p1.name, SUM(ST_Distance(p1.geom, p2.geom, true)) as distance
FROM location as p1
LEFT JOIN location as p2
ON p1.name = p2.name and p1.provider <> p2.provider
GROUP BY p1.provider, p1.name
ORDER BY distance