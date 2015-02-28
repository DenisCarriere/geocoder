# GeoJSON Support

GeoJSON is a format for encoding a variety of geographic data structures. A complete GeoJSON data structure is always an object (in JSON terms). In GeoJSON, an object consists of a collection of name/value pairs -- also called members. For each member, the name is always a string. Member values are either a string, number, object, array or one of the literals: true, false, and null.

[GeoJSON Specification](http://geojson.org/geojson-spec.html)

## Python Example

```python
>>> import geocoder
>>> g = geocoder.google("New York City")
>>> g.geojson
...
```

## GeoJSON Output

The difference between the GeoJSON and JSON response is the `geometry` attribute is in accordance with GeoJSON specification; All attributes are nested in the `properties` attribute and the `bbox` (bounding box) is formatted to the GeoJSON spec.

```json
{
    "geometry": {
        "type": "Point",
        "coordinates": [
            -74.0059413,
            40.7127837
        ]
    },
    "type": "Feature",
    "properties": {
        "status": "OK",
        "city": "New York",
        "confidence": 1,
        "ok": true,
        "country": "United States",
        "provider": "google",
        "location": "New York City",
        "state": "New York",
        "address": "New York, NY, USA",
        "lat": 40.7127837,
        "lng": -74.0059413,
        "quality": "locality",
        "accuracy": "APPROXIMATE"
    },
    "bbox": [
        -74.25908989999999,
        40.4913686,
        -73.70027209999999,
        40.91525559999999
    ]
}
```
