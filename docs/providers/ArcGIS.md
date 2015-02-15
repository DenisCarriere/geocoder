# ArcGIS REST API

The World Geocoding Service finds addresses and places in all supported countries
from a single endpoint. The service can find point locations of addresses,
business names, and so on.  The output points can be visualized on a map,
inserted as stops for a route, or loaded as input for a spatial analysis.
an address, retrieving imagery metadata, or creating a route.

## Python Example

```python
>>> import geocoder
>>> g = geocoder.arcgis('New York City')
>>> g.json
...
```

## API Reference

https://developers.arcgis.com/rest/geocode/api-reference/geocoding-find.htm

## OSM Quality (1/6)

- [ ] addr:housenumber
- [ ] addr:street
- [ ] addr:city
- [ ] addr:state
- [ ] addr:country
- [x] **addr:postal**

## Attributes (12/18)

- [ ] accuracy
- [x] **address**
- [x] **bbox**
- [ ] city
- [x] **confidence**
- [ ] country
- [ ] housenumber
- [x] **lat**
- [x] **lng**
- [x] **location**
- [x] **ok**
- [x] **postal**
- [x] **provider**
- [x] **quality**
- [x] **score**
- [ ] state
- [x] **status**
- [ ] street