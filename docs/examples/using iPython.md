# Using iPython

```bash
$ pip install ipython
$ ipython
```

Using the **TAB** key after entering '.' you will see all the available **providers**.

```python
>>> import geocoder
>>> g = geocoder.
geocoder.api             geocoder.geolytica       geocoder.mapquest
geocoder.arcgis          geocoder.geonames        geocoder.nokia
geocoder.base            geocoder.get             geocoder.osm
geocoder.bing            geocoder.google          geocoder.timezone
geocoder.canadapost      geocoder.ip              geocoder.yahoo
geocoder.cli             geocoder.keys            geocoder.tomtom
geocoder.elevation       geocoder.location 
...       
```

Using the **TAB** key again, you can see all the available **attributes**.

```python
>>> g = geocoder.google('Ottawa')
>>> g.
g.accuracy            g.latlng              g.south
g.address             g.lng                 g.southeast
g.api                 g.locality            g.southwest
g.attributes          g.location            g.state
g.bbox                g.neighborhood        g.status
g.content             g.north               g.status_code
g.country             g.northeast           g.status_description
g.county              g.northwest           g.street_number
g.debug               g.ok                  g.sublocality
g.east                g.params              g.subpremise
g.error               g.parse               g.url
g.geometry            g.postal              g.west
g.headers             g.provider            g.wkt
g.help                g.quality             g.x
g.json                g.route               g.y
g.lat                 g.short_name
...    
```