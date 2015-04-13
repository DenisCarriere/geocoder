# HERE

Send a request to the geocode endpoint to find an address using a combination of
country, state, county, city, postal code, district, street and house number.
Using Geocoder you can retrieve geocoded data from the HERE Geocoder REST API.

## Python Example

```python
>>> import geocoder
>>> g = geocoder.here('Espoo, Finland')
>>> g.json
...
```

## Using your own API Key

If you want to use your own `app_id` & `app_code`, you must register an app at the [HERE Developer](https://developer.here.com/geocoder).

```python
>>> g = geocoder.here('Espoo, Finland',
                    app_id='<YOUR APP ID>',
                    app_code='<YOUR APP CODE>')
```

## Reverse Geocoding

```python
>>> g = geocoder.here([45.123, -75.123], method='reverse')
>>> g.json
...
```

** Command Line Interface **

```bash
$ geocode 'Espoo, Finland' --provider here
$ geocode '45.15, -75.14' --provider here --method reverse
```

## Parameters

- `location`: Your search location you want geocoded.
- `app_code`: (optional) use your own Application Code from HERE.
- `app_id`: (optional) use your own Application ID from HERE.
- `method`: (optional) default=geocode, reverse

## References

* [GitHub Repo](https://github.com/DenisCarriere/geocoder)
* [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
* [HERE Geocoder REST API](https://developer.here.com/rest-apis/documentation/geocoder)
