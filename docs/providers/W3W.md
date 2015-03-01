# what3words

what3words is a global grid of 57 trillion 3mx3m squares.
Each square has a 3 word address that can be communicated quickly,
easily and with no ambiguity.

> **Addressing the world**
> Everyone and everywhere now has an address

## Python Example

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

## Parameters

> :param **location**: Your search location you want geocoded.
> :param **key**: W3W API key.
> :param **method**: Chose a method (geocode, method)

## References

<i class="icon-doc"></i> [API Reference](http://developer.what3words.com/)
<i class="icon-key"></i> [Get W3W key](http://developer.what3words.com/api-register/)
