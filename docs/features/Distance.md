# Distance Tool

The distance tool measures the Great Circle distance between the surface of the earth between two or multiple points.

![Distance Tool](https://pbs.twimg.com/media/CAbDTPKW8AAQ68l.png:large)

***

## Examples

### Python & CLI

Simply add as many locations into the `distance` function, to change the units of measurement include the `units` parameter.

When entering a location string it will geocode it automatically using the given `provider` parameter. Some warning errors might occur when trying to geocode too many string locations, this is a combination of rate limits or a lost URL connection.

When using the CLI, simply raise the `--distance` flag to use the distance tool.

#### Simple use

```python
>>> from geocoder import distance
>>> d = distance("Ottawa, ON", "Toronto, ON")
>>> print(d)
353.80
>>> type(d)
float
```

```bash
$ geocode "Ottawa, ON", "Toronto, ON" --distance
353.80
```

#### Select a Geocoder provider

```python
# Default provider="bing"
>>> distance("Ottawa, ON", "Toronto, ON", provider="google")
353.80
```

```bash
$ geocode "Ottawa, ON", "Toronto, ON" --distance --provider="google"
353.80
```

#### Define Units of measurements

```python
# Default units='kilometers'
# Ex: kilometers, miles, feet, meters
>>> distance("Ottawa, ON", "Toronto, ON", units="miles")
219.84
```

```bash
$ geocode "Ottawa, ON", "Toronto, ON" --distance --units="miles"
219.84
```

#### Using LatLng strings or lists

```python
>>> distance([45.07, -75.49], "43.30, -80.15")
351.94
```

```bash
$ geocode "[45.07, -76.49]", "43.30, -80.15" --distance
351.94
```

#### 3 or more locations

```python
>>> distance("Ottawa, ON", "Toronto, ON", "Montreal, QC")
521.18
```

```bash
$ geocode "Ottawa, ON", "Toronto, ON", "Montreal, QC" --distance
521.18
```

#### Input Geocoder objects

```python
>>> import geocoder
>>> point1 = geocoder.google("Ottawa, ON")
>>> point2 = geocoder.bing("Toronto, ON")
>>> geocoder.distance(point1, point2)
353.80
```

## Parameters

- `location` : Your search  locations you want geocoded. (min 2x locations)
- `units` :  Unit of measurement. (default=kilometers)
    - kilometers
    - miles
    - feet
    - meters