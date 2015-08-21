# IpinfoIo (IP Address)

## Python Example

```python
>>> import geocoder
>>> g = geocoder.ipinfoio('199.7.157.0')
>>> g.latlng
[45.413140, -75.656703]
>>> g.city
'Toronto'
...
```

To retrieve your own IP address, simply have `''` as the input.

```python
>>> import geocoder
>>> g = geocoder.ipinfoio('')
>>> g.latlng
[45.413140, -75.656703]
>>> g.ip
'199.7.157.0'
...
```

## Geocoder Attributes

```
g.address        g.ip          g.postal         g.y
g.city           g.json        g.lat            g.provider
g.content        g.latlng      g.state
g.country        g.lng         g.status
g.debug          g.location    g.status_code
g.error          g.ok          g.url
g.geometry       g.params      g.wkt
g.headers        g.parse       g.x
```

## Parameters

* :param location: Your search IP Address you want geocoded.
* :param location: (optional) `''` will return your current IP address's location.

## References

* [GitHub Repo](https://github.com/DenisCarriere/geocoder)
* [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
* [IpinfoIo](https://www.ipinfo.io)
