# TomTom

The Geocoding API gives developers access to TomTom’s first class geocoding service.
Developers may call this service through either a single or batch geocoding request.
This service supports global coverage, with house number level matching in over 50 countries,
and address point matching where available.
Using Geocoder you can retrieve TomTom's geocoded data from Geocoding API.

## Python Example

```python
>>> import geocoder # pip install geocoder
>>> g = geocoder.tomtom('<address>')
>>> g.lat, g.lng
45.413140 -75.656703
...
```

## Geocoder Attributes

* address
* country
* lat
* lng
* locality
* location
* postal
* provider
* quality
* route
* state
* status
* street_number

## Parameters

* :param ``location``: Your search location you want geocoded.
* :param ``key``: (optional) use your own API Key from TomTom.

## References

* [GitHub Repo](https://github.com/DenisCarriere/geocoder)
* [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
* [Geocoding API](http://developer.tomtom.com/products/geocoding_api)
