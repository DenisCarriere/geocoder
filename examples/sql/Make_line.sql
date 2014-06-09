DELETE FROM lines;

INSERT INTO lines (provider, location, address, geom, distance)
SELECT p1.provider, p2.location, p1.address, ST_MakeLine(ST_Union(p1.geom),ST_Centroid(ST_Union(p2.geom))), ST_Length(ST_MakeLine(ST_Union(p1.geom),ST_Centroid(ST_Union(p2.geom))), True)
FROM geocoder as p1
LEFT JOIN kingston as p2
ON p1.location = p2.location
GROUP BY p1.provider, p2.location, p1.address