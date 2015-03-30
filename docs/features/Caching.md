## Caching

Caching feature in the Geocoder.

The CLI would look something like this:

**Simple Case**

```bash
$ geocode "Ottawa ON" --cache
```

```python
>>> import geocoder
>>> g = geocoder.google("Ottawa ON", cache="<database>")
>>> g.json
{...}
```

**Batch geocode**

```bash
# Linux
$ cat "foo.txt" | geocode --cache
```

```bash
# Windows
C:\> type "foo.txt" | geocode --cache
```


**Extra parameters**

```bash
$ geocode "Ottawa ON" --cache "<database>" \
                      --username "<user>" \
                      --password "<pass>" \
                      --host "<host>" \
                      --port 28015
```

```python
>>> g = geocoder.google("Ottawa ON",
                        cache="<database>",
                        username="<user>",
                        password="<pass>",
                        host="<host>",
                        port=28015)
```

### Parameters

|Params   |Description       |Default            |
|:--------|:-----------------|:------------------|
|db       |SQLAlchemy DB     |sqlite:///:memory: |
|location |Query Location    |                   |
|provider |Geocoder Provider |bing               |
|method   |Geocoder Method   |geocode            |
|output   |json/geojson/osm  |json               |

### Using Cache.py

```python
# User Variables
location = 'Orleans, Ottawa'

# Geocode Address
g = geocoder.bing(location)

# Create Cache Databse
cache = Cache('sqlite:///:memory:')

# Insert into Database
values = {
    'location': location,
    'provider': 'bing',
    'lat': 45.34,
    'lng': -75.123
}
cache.insert(values)

# Find results with a Query
print(cache.find(location))
```
