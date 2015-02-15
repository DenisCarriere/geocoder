# OpenStreetMap

Address information can be added to OpenStreetMap using a variety of methods, such as adding a simple node containing an address, adding address information to a building or site outline, or alternatively to an entrance node for the building.

[OpenStreetMap Addresses Specification](http://wiki.openstreetmap.org/wiki/Addresses)

## Python Example

```python
>>> import geocoder
>>> g = geocoder.google('11 Wall Street, New York')
>>> g.osm
...
```

## OSM Output

```json
{
    "addr:housenumber": "11",
    "addr:street": "Wall Street",
    "addr:postal": "10005",
    "addr:city": "New York",
    "addr:state": "New York",
    "addr:country": "United States",
    "y": 40.7069226,
    "x": -74.0111421
}
```