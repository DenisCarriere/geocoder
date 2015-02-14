# Opencage

OpenCage Geocoder simple, easy, and open geocoding for the entire world
Our API combines multiple geocoding systems in the background.
Each is optimized for different parts of the world and types of requests.We aggregate the best results from open data sources and algorithms so you don't have to.
Each is optimized for different parts of the world and types of requests.
Using Geocoder you can retrieve opencage's geocoded data from OpenCage Geocoding Services.

## Python Example

```python
>>> import geocoder # pip install geocoder
>>> g = geocoder.opencage('<address>')
>>> g.lat, g.lng
45.413140 -75.656703
...
```

## Geocoder Attributes

* accuracy
* address
* city
* country
* district
* housenumber
* lat
* license
* lng
* location
* neighborhood
* postal
* provider
* route
* state
* status
* w3w

## Parameters

* :param ``location``: Your search location you want geocoded.
* :param ``key``: (optional) use your own API Key from OpenCage.

## References

* [GitHub Repo](https://github.com/DenisCarriere/geocoder)
* [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
* [OpenCage Geocoding Services](http://geocoder.opencagedata.com/api.html)
