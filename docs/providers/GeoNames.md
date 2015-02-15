# GeoNames

GeoNames is mainly using REST webservices. Find nearby postal codes / reverse geocoding
This service comes in two flavors.You can either pass the lat/long or a postalcode/placename.

Using Geocoder you can retrieve GeoNames's geocoded data from GeoNames REST Web Services.

## Python Example

```python
>>> import geocoder # pip install geocoder
>>> g = geocoder.geonames('<address>')
>>> g.lat, g.lng
45.413140 -75.656703
...
```

## Geocoder Attributes

* address
* country
* lat
* lng
* location
* population
* provider
* quality
* state
* status

## Parameters

* :param ``location``: Your search location you want geocoded.
* :param ``username``: (required) needs to be passed with each request.

## References

* [GitHub Repo](https://github.com/DenisCarriere/geocoder)
* [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
* [GeoNames REST Web Services](http://www.geonames.org/export/web-services.html)