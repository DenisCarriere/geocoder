# Bing

The Bing™ Maps REST Services Application Programming Interface (API)
provides a Representational State Transfer (REST) interface to
perform tasks such as creating a static map with pushpins, geocoding
an address, retrieving imagery metadata, or creating a route.
Using Geocoder you can retrieve Bing's geocoded data from Bing Maps REST Services.

## Python Example

```python
>>> import geocoder # pip install geocoder
>>> g = geocoder.bing('<address>')
>>> g.lat, g.lng
45.413140 -75.656703
...
```

## Geocoder Attributes

* accuracy
* address
* bbox
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

## Parameters

* :param location: Your search location you want geocoded.
* :param key: (optional) use your own API Key from Bing.

## References

* [GitHub Repo](https://github.com/DenisCarriere/geocoder)
* [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
* [Bing Maps REST Services](http://msdn.microsoft.com/en-us/library/ff701714.aspx)