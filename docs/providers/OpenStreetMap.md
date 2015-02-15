[<< Back to Home](http://deniscarriere.github.io/geocoder/)

# OpenStreetMap

Nominatim (from the Latin, 'by name') is a tool to search OSM data by name 
and address and to generate synthetic addresses of OSM points (reverse geocoding).
Using Geocoder you can retrieve OSM's geocoded data from Nominatim.

## Python Example

```python
>>> import geocoder # pip install geocoder
>>> g = geocoder.osm('11 Wall Street, New York')
>>> g.json
...
```

## Using your own OSM Server

```python
>>> g = geocoder.osm('11 Wall Street, New York', 
                  url='http://nominatim.openstreetmap.org/search')
```

## Parameters

* `location`: Your search location you want geocoded.
* `url`: Custom OSM Server URL location

## JSON Output

```json
{
    "status": "OK", 
    "city": "NYC", 
    "confidence": 10, 
    "neighborhood": "Southbridge Towers", 
    "quality": "house", 
    "encoding": "utf-8", 
    "country": "United States of America", 
    "osm_id": "2824828203", 
    "provider": "osm", 
    "county": "New York", 
    "osm_type": "node", 
    "state": "New York", 
    "street": "Wall Street", 
    "bbox": {
        "northeast": [
            40.7071907, 
            -74.010815
        ], 
        "southwest": [
            40.7070907, 
            -74.010915
        ]
    }, 
    "address": "11, Wall Street, Southbridge Towers...", 
    "lat": "40.7071407", 
    "ok": true, 
    "lng": "-74.010865", 
    "postal": "10005", 
    "housenumber": "11", 
    "location": "11 Wall street, New York"
}
```

## References

* [GitHub Repo](https://github.com/DenisCarriere/geocoder)
* [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
* [Nominatim](http://wiki.openstreetmap.org/wiki/Nominatim)