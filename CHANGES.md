# Changes

## Geocoder 0.8.4 - 2014/10/20

- Added OpenCage as a provider

- JSON Data attributes are consistently (City > State > Country)

- W3W is a new attribute from OpenCage


## Geocoder 0.8.1 - 2014/09/27

- CLI called geocode
```python
geocode "123 Address, City" --output results.json --provider google
```
- geocode function in the core API
```python
g = geocoder.geocode('<address>', provider='bing')
```
- Reverse geocoding with Google & Bing, Canada post (not working at the moment)
```python
g = geocoder.canadapost('<address>', reverse=True)
g = geocoder.bing('<address>', reverse=True)
g = geocoder.google('<address>', reverse=True)
```
- Added geocoder.**latlng** field to the core attributes.
