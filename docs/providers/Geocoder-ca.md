# Geocoder.ca

Geocoder.ca - A Canadian and US location geocoder.
Using Geocoder you can retrieve Geolytica's geocoded data from Geocoder.ca.

## Python Example

```python
>>> import geocoder # pip install geocoder
>>> g = geocoder.geolytica('<address>')
>>> g.lat, g.lng
45.413140 -75.656703
...
```

## Geocoder Attributes

* address
* lat
* lng
* locality
* location
* postal
* provider
* route
* state
* status
* street_number

## References

* [GitHub Repo](https://github.com/DenisCarriere/geocoder)
* [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
* [Geocoder.ca](http://geocoder.ca/?api=1)