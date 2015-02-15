# GeoOttawa

This data was collected in the field using GPS software on handheld computers. Not all information has been verified for accuracy and therefore should only be used in an advisory capacity. Forestry Services reserves the right to revise the data pursuant to further inspection/review. If you find any errors or omissions, please report them to 3-1-1. 

[GeoOttawa Map](http://maps.ottawa.ca/geoottawa/)

## Python Example

```python
>>> import geocoder
>>> g = geocoder.ottawa("453 Booth Street")
>>> g.json
...
```

## JSON Output

```json
{
    "status": "OK", 
    "city": "Ottawa", 
    "ok": true, 
    "country": "Canada", 
    "provider": "ottawa", 
    "state": "Ontario", 
    "location": "453 Booth Street", 
    "address": "453 BOOTH ST, K1R7K9", 
    "lat": 45.40490114288874, 
    "lng": -75.70755144879519, 
    "postal": "K1R7K9", 
    "housenumber": 453, 
    "accuracy": 100
}
```