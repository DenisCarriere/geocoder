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