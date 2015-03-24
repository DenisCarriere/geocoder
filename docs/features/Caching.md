## Caching

Caching feature in the Geocoder.

The CLI would look something like this:

**Simple Case**

```bash
$ geocode "Ottawa ON" --cache
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
$ geocode "Ottawa ON" --provider "google" \
                      --cache "geocoder" \
                      --db "mongodb" \
                      --username "Denis" \
                      --password "Password"
```

**Using it in Python**

```python
>>> import geocoder
>>> g = geocoder.google("Ottawa ON", cache=True)
>>> g.json
{...}
```

**Extra parameters**

```python
>>> g = geocoder.google("Ottawa ON",
                        cache="geocoder",
                        db="mongodb",
                        username="Denis",
                        password="Password")
```