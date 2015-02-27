# MapQuest

The geocoding service enables you to take an address and get the
associated latitude and longitude. You can also use any latitude
and longitude pair and get the associated address. Three types of
geocoding are offered: address, reverse, and batch.
Using Geocoder you can retrieve MapQuest's geocoded data from Geocoding Service.

## Python Example

```python
>>> import geocoder # pip install geocoder
>>> g = geocoder.mapquest('<address>')
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
* state
* status

## Parameters

* :param ``location``: Your search location you want geocoded.

## References

* [GitHub Repo](https://github.com/DenisCarriere/geocoder)
* [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
* [Geocoding Service](http://www.mapquestapi.com/geocoding/)
