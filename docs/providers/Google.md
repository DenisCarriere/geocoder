# Google

Geocoding is the process of converting addresses (like "1600 Amphitheatre Parkway, 
Mountain View, CA") into geographic coordinates (like latitude 37.423021 and 
longitude -122.083739), which you can use to place markers or position the map.
Using Geocoder you can retrieve google's geocoded data from Google Geocoding API.

## Python Example

```python
>>> import geocoder # pip install geocoder
>>> g = geocoder.google('<address>')
>>> g.lat, g.lng
45.413140 -75.656703
...
```

## Geocoder Attributes

* accuracy
* address
* country
* county
* error
* lat
* lng
* locality
* location
* neighborhood
* postal
* provider
* quality
* route
* state
* status
* street_number
* sublocality
* subpremise

## Parameters

* :param ``location``: Your search location you want geocoded.
* :param ``short_name``: (optional) if ``False`` will retrieve the results with Long names.

## References

* [GitHub Repo](https://github.com/DenisCarriere/geocoder)
* [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
* [Google Geocoding API](https://developers.google.com/maps/documentation/geocoding/)