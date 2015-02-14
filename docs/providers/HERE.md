[<< Back to Home](/)

# HERE

Send a request to the geocode endpoint to find an address using a combination of
country, state, county, city, postal code, district, street and house number.
Using Geocoder you can retrieve geocoded data from the HERE Geocoder REST API.

## Python Example

```python
>>> import geocoder # pip install geocoder
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
>>> g = geocoder.here('Espoo, Finland', method='reverse')
```

## Parameters

- `location`: Your search location you want geocoded.
- `app_code`: (optional) use your own Application Code from HERE.
- `app_id`: (optional) use your own Application ID from HERE.
- `method`: (optional) default=geocode, reverse

## JSON Output

```json
{
    "status": "OK", 
    "city": "Espoo", 
    "confidence": 1, 
    "ok": true, 
    "encoding": "utf-8", 
    "country": "FIN", 
    "provider": "here", 
    "county": "Uusimaa", 
    "state": "Etelä-Suomi", 
    "bbox": {
        "northeast": [
            60.3625, 
            24.87
        ], 
        "southwest": [
            60.05958, 
            24.49933
        ]
    }, 
    "address": "Espoo, Etelä-Suomi, Suomi", 
    "lat": 60.20678, 
    "lng": 24.65578, 
    "postal": "02770", 
    "quality": "city", 
    "location": "Espoo, Finland"
}
```

## References

* [GitHub Repo](https://github.com/DenisCarriere/geocoder)
* [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
* [HERE Geocoder REST API](https://developer.here.com/rest-apis/documentation/geocoder)