# CanadaPost

The next generation of address finders, AddressComplete uses intelligent, fast
searching to improve data accuracy and relevancy. Simply start typing a business
name, address or Postal Code and AddressComplete will suggest results as you go.
Using Geocoder you can retrieve CanadaPost's geocoded data from Addres Complete API.

## Examples

**Getting Postal Code**

```python
>>> import geocoder
>>> g = geocoder.canadapost('453 Booth Street, Ottawa')
>>> g.postal
'K1R 7K9'
>>> g.json
...
```

**Command Line Interface**

```bash
$ geocode '453 Booth Street, Ottawa' --provider canadapost
```

## Parameters

- `location`: Your search location you want geocoded.
- `key`: (optional) API Key from CanadaPost Address Complete.

## References

- [Addres Complete API](https://www.canadapost.ca/pca/)