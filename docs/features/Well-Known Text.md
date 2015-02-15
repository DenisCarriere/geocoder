# Well Known Text

Well-known text (WKT) is a text markup language for representing vector geometry objects on a map, spatial reference systems of spatial objects and transformations between spatial reference systems. A binary equivalent, known as well-known binary (WKB), is used to transfer and store the same information on databases, such as PostGIS, Microsoft SQL Server and DB2. The formats were originally defined by the Open Geospatial Consortium (OGC) and described in their Simple Feature Access and Coordinate Transformation Service specifications.

[Wikipedia WKT](http://en.wikipedia.org/wiki/Well-known_text)

# Python Example

```python
>>> import geocoder
>>> g = geocoder.google('New York City')
>>> g.wkt
'POINT(-74.0111421 40.7069226)'
```