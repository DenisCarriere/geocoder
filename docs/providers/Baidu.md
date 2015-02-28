# Baidu

Baidu Maps Geocoding API is a free open the API, the default quota
one million times / day.

## Python Example

```python
>>> import geocoder
>>> g = geocoder.baidu('中国')
>>> g.latlng
[37.550339474591, 104.11412925348]
...
```

## Geocoder Attributes

- encoding
- lat
- lng
- location
- ok
- provider
- quality
- status

## Parameters

* :param location: Your search location you want geocoded.
* :param key: Baidu API key.
* :param referer: Baidu API referer website.

## References

- [API Reference](http://developer.baidu.com/map/index.php?title=webapi/guide/webservice-geocoding)
- [Get Baidu key](http://lbsyun.baidu.com/apiconsole/key)