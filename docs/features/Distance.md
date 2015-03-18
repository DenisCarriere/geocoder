#Distance Tool

The distance tool measures the Great Circle distance between the surface of the earth between two or multiple points.

***

## Examples

### Python

Simply add as many locations into the `distance` function, to change the units of measurement include the `units` parameter.

When entering a location string it will geocode it automatically using the given `provider` parameter. Some warning errors might occur when trying to geocode too many string locations, this is a combination of rate limits or a lost URL connection.

```python
# Simple use
>>> distance = geocoder.distance("Ottawa, ON", "Toronto, ON")
>>> print(distance)
353.80

# Select a Geocoder provider (default=bing)
>>> geocoder.distance("Ottawa, ON", "Toronto, ON", provider="google")
353.80

# Define Units of measurements (kilometers, miles, feet, meters)
>>> geocoder.distance("Ottawa, ON", "Toronto, ON", provider="google")
353.80

# Using LatLng strings or lists
>>> geocoder.distance([45.42, -75.69], "43.65, -79.38")
352.47

# 2 or more locations
>>> geocoder.distance("Ottawa, ON", "Toronto, ON", "Montreal, QC")
521.18
```

### Command Line Interface

Simply add the `--distance` flag to the `geocode` Command Line Interface, to change the units of measurement include the `--units` parameter.

```bash
# Simple use
$ geocode "Ottawa, ON", "Toronto, ON" --distance
353.80

# Select a Geocoder provider (default=bing)
$ geocode "Ottawa, ON", "Toronto, ON" --distance --provider="google"
353.80

# Define Units of measurements (kilometers, miles, feet, meters)
$ geocode "Ottawa, ON", "Toronto, ON" --distance --units="miles"
219.84

# Using LatLng strings
$ geocode "45.07, -76.49", "43.30, -80.15" --distance
351.94

# 2 or more locations
$ geocode "Toronto, ON", "Ottawa, ON", "Montreal, QC" --distance
521.18
```

## Parameters

- `location` : Your search  locations you want geocoded. (min 2x locations)
- `units` :  Unit of measurement. (default=kilometers)
    - kilometers
    - miles
    - feet
    - meters