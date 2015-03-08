# OpenStreetMap

Nominatim (from the Latin, 'by name') is a tool to search OSM data by name
and address and to generate synthetic addresses of OSM points (reverse geocoding).
Using Geocoder you can retrieve OSM's geocoded data from Nominatim.

## Examples

**Python**

```python
>>> import geocoder
>>> g = geocoder.osm("New York City")
>>> g.json
...
```

**CLI**

```bash
$ geocode "New York City" --provider osm | jq .
```

## Using your own OSM Server

Setting up your own offline Nomimatim server is possible, using Ubuntu 14.04 as your OS and following the [Nomimatim Install](http://wiki.openstreetmap.org/wiki/Nominatim/Installation) instructions. This enables you to request as much geocoding as your little heart desires!

**Python**

```python
### Both urls will work
>>> url = 'http://localhost/nominatim/'
>>> url = 'localhost'
>>> g = geocoder.osm("New York City", url=url)
>>> g.json
...
```

**CLI**

```bash
$ geocode "New York City" -p osm --url localhost| jq .
```

## Parameters

* `location`: Your search location you want geocoded.
* `url`: Custom OSM Server (ex: localhost)

## References

* [GitHub Repo](https://github.com/DenisCarriere/geocoder)
* [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
* [Nominatim](http://wiki.openstreetmap.org/wiki/Nominatim)
* [Nominatim Install](http://wiki.openstreetmap.org/wiki/Nominatim/Installation)