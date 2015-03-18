#Distance Tool

The distance tool measures the Great Circle distance between the surface of the earth between two or multiple points.

***

## Examples

### Python

### Command Line Interface

Simply add the `--distance` flag to the `geocode` Command Line Interface, to change the measurement value include the `--units` parameter.

```bash
# Simple use
$ geocode "Ottawa, ON", "Toronto, ON" --distance
353.805898267

# Select a Geocoder provider (default=bing)
$ geocode "Ottawa, ON", "Toronto, ON" --distance --provider="google"
353.805898267

# Define Units of measurements (kilometers, miles, feet, meters)
$ geocode "Ottawa, ON", "Toronto, ON" --distance --units="miles"
219.844724812

# Using LatLng strings
$ geocode "45.07, -76.49", "43.30, -80.15" --distance
351.94521709

# 2 or more locations
$ geocode "Toronto, ON", "Ottawa, ON", "Montreal, QC" --distance
521.18441474
```

## Parameters

- `location` : Your search  locations you want geocoded. (min 2x locations)
- `units` :  Unit of measurement. (default=kilometers)
    - kilometers
    - miles
    - feet
    - meters