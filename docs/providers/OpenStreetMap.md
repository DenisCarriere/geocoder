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

Setting up your own offline Nominatim server is possible, using Ubuntu 14.04 as your OS and following the [Nominatim Install] instructions. This enables you to request as much geocoding as your little heart desires!

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

## OSM Addresses

The [addr tag] is the prefix for several `addr:`* keys to describe addresses.

This format is meant to be saved as a CSV and imported into JOSM.

**Python**

```python
>>> g = geocoder.osm('11 Wall Street, New York')
>>> g.osm
...
```

**CLI**

```bash
$ geocode "11 Wall Street, New York" -p osm --output osm | jq .
```

**JSON**

```json
{
    "addr:housenumber": "11",
    "addr:street": "Wall Street",
    "addr:postal": "10005",
    "addr:city": "New York",
    "addr:state": "New York",
    "addr:country": "United States",
    "y": 40.7069226,
    "x": -74.0111421
}
```

## Parameters

* `location`: Your search location you want geocoded.
* `url`: Custom OSM Server (ex: localhost)

## References

* [GitHub Repo](https://github.com/DenisCarriere/geocoder)
* [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
* [Nominatim](http://wiki.openstreetmap.org/wiki/Nominatim)
* [Nominatim Install]

[Nominatim Install]: http://wiki.openstreetmap.org/wiki/Nominatim/Installation
[addr tag]: http://wiki.openstreetmap.org/wiki/Key:addr