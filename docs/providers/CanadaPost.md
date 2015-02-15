# CanadaPost

The next generation of address finders, AddressComplete uses intelligent, fast
searching to improve data accuracy and relevancy. Simply start typing a business
name, address or Postal Code and AddressComplete will suggest results as you go.
Using Geocoder you can retrieve CanadaPost's geocoded data from Addres Complete API.

## Python Example

```python
>>> import geocoder
>>> g = geocoder.canadapost('<address>')
>>> g.postal
'K1R 7K9'
...
```

## Geocoder Attributes

* address
* country
* key
* locality
* location
* ok
* postal
* provider
* quality
* route
* state
* status
* street_number

## Parameters

* :param ``location``: Your search location you want geocoded.
* :param ``key``: (optional) use your own API Key from CanadaPost Address Complete.

## References

* [GitHub Repo](https://github.com/DenisCarriere/geocoder)
* [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
* [Addres Complete API](https://www.canadapost.ca/pca/)