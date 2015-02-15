FreeGeoIP.net
=============
freegeoip.net provides a public HTTP API for software developers to 
search the geolocation of IP addresses. It uses a database of IP addresses 
that are associated to cities along with other relevant information like 
time zone, latitude and longitude.

You're allowed up to 10,000 queries per hour by default. Once this 
limit is reached, all of your requests will result in HTTP 403, 
forbidden, until your quota is cleared. 

API Reference
-------------
http://freegeoip.net/

OSM Quality (4/6)
-----------------
- [ ] addr:housenumber
- [ ] addr:street
- [x] addr:city
- [x] addr:state
- [x] addr:country
- [x] addr:postal

Examples
--------
**CLI**

```bash
$ geocode '99.240.181.199' --provider freegeoip --pretty --geojson
$ geocode '99.240.181.199' --provider freegeoip --pretty --json
$ geocode '99.240.181.199' --provider freegeoip --pretty --osm
```
**iPython**

```python
$ ipython
>>> import geocoder
>>> g = geocoder.freegeoip('99.240.181.199')
<[OK] Freegeoip - Geocode [Ottawa, Ontario Canada]>
>>> g.geojson
>>> g.json
>>> g.osm
```
GeoJSON
-------
```json
{
    "geometry": {
        "type": "Point", 
        "coordinates": [
            -75.691, 
            45.413
        ]
    }, 
    "type": "Feature", 
    "properties": {
        "status": "OK", 
        "city": "Ottawa", 
        "ip": "99.240.181.199", 
        "address": "Ottawa, Ontario Canada", 
        "provider": "freegeoip", 
        "time_zone": "America/Toronto", 
        "state": "Ontario", 
        "location": "99.240.181.199", 
        "country": "Canada", 
        "postal": "K2P"
    }
}
```
JSON
----
```json
{
    "status": "OK", 
    "city": "Ottawa", 
    "ip": "99.240.181.199", 
    "address": "Ottawa, Ontario Canada", 
    "provider": "freegeoip", 
    "time_zone": "America/Toronto", 
    "state": "Ontario", 
    "location": "99.240.181.199", 
    "country": "Canada", 
    "lat": 45.413, 
    "lng": -75.691, 
    "postal": "K2P"
}
```
OSM
---
```json
{
    "addr:postal": "K2P", 
    "addr:city": "Ottawa", 
    "addr:state": "Ontario", 
    "y": 45.413, 
    "x": -75.691, 
    "addr:country": "Canada"
}
```