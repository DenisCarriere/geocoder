# MaxMind (IP Address)

MaxMind's GeoIP2 products enable you to identify the location, 
organization, connection speed, and user type of your Internet 
visitors. The GeoIP2 databases are among the most popular and 
accurate IP geolocation databases available.
Using Geocoder you can retrieve Maxmind's geocoded data from MaxMind's GeoIP2.

## Python Example

```python
>>> import geocoder
>>> g = geocoder.ip('199.7.157.0')
>>> g.latlng
[45.413140, -75.656703]
>>> g.city
'Toronto'
...
```

To retrieve your own IP address, simply have `'me'` as the input.

```python
>>> import geocoder
>>> g = geocoder.ip('me')
>>> g.latlng
[45.413140, -75.656703]
>>> g.ip
'199.7.157.0'
...
```

Auto detection of IP address for flexible inputs.

```python
>>> import geocoder
>>> g = geocoder.ip('This is my ip 74.125.226.99')
<[OK] Ip - Geocode [Mountain View, California United States]>
>>> g = geocoder.ip('No IP address in string')
<[ERROR - IP Address Invalid] Ip - Geocode []>
```

## Geocoder Attributes

```
g.address      g.error        g.latlng       g.state
g.api          g.geometry     g.lng          g.status
g.city         g.headers      g.location     g.status_code
g.content      g.help         g.ok           g.url
g.continent    g.ip           g.params       g.wkt
g.country      g.isp          g.parse        g.x
g.debug        g.json         g.postal       g.y
g.domain       g.lat          g.provider     
```

## Parameters

* :param location: Your search IP Address you want geocoded.
* :param location: (optional) `'me'` will return your current IP address's location.

## References

* [GitHub Repo](https://github.com/DenisCarriere/geocoder)
* [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
* [MaxMind's GeoIP2](https://www.maxmind.com/en/geolocation_landing)