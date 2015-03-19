# what3words

what3words is a global grid of 57 trillion 3mx3m squares.
Each square has a 3 word address that can be communicated quickly,
easily and with no ambiguity.

**Addressing the world**

Everyone and everywhere now has an address

## Examples

**Geocoding 3 Words**

```python
>>> import geocoder
>>> g = geocoder.w3w('embedded.fizzled.trial')
>>> g.json
...
```

**Reverse Geocoding**

```python
>>> import geocoder
>>> g = geocoder.w3w([45.15, -75.14], method='reverse')
>>> g.json
...
```

**Command Line Interface**

```bash
$ geocode 'embedded.fizzled.trial' --provider w3w
$ geocode '45.15, -75.14' --provider w3w --method reverse
```

## Parameters

- `location`: Your search location you want geocoded.
- `key`: W3W API key.
- `method`: Chose one of the following methods:
    * geocode
    * reverse

## References

- [API Reference](http://developer.what3words.com/)
- [Get W3W key](http://developer.what3words.com/api-register/)
