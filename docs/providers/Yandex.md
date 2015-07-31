.. _yandex:

# Yandex

Yandex (Russian: Яндекс) is a Russian Internet company
which operates the largest search engine in Russia with
about 60% market share in that country.

The Yandex home page has been rated as the most popular website in Russia.

## Examples

### Python & CLI

**Simple Geocoding**

```python
>>> import geocoder
>>> g = geocoder.yandex('Moscow Russia')
>>> g.json
...
```

```bash
$ geocode 'Moscow Russia' --provider yandex
```


**Reverse Geocoding**

```python
>>> import geocoder
>>> g = geocoder.yandex([45.15, -75.14], method='reverse')
>>> g.json
...
```

```bash
$ geocode '45.15, -75.14' --provider yandex --method reverse
```

## Parameters

- `location`: Your search location you want geocoded.
- `lang`: Chose the following language:
    - **ru-RU** — Russian (by default)
    - **uk-UA** — Ukrainian
    - **be-BY** — Belarusian
    - **en-US** — American English
    - **en-BR** — British English
    - **tr-TR** — Turkish (only for maps of Turkey)
- `kind`: Type of toponym (only for reverse geocoding):
    - **house** — house or building
    - **street** — street
    - **metro** — subway station
    - **district** — city district
    - **locality** — locality (city, town, village, etc.)

## References

- [API Reference](http://api.yandex.com/maps/doc/geocoder/desc/concepts/input_params.xml)
