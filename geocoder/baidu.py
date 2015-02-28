#!/usr/bin/python
# coding: utf8

from base import Base
from keys import baidu_key


class Baidu(Base):
    """
    Baidu Geocoding API
    ===================
    Baidu Maps Geocoding API is a free open the API, the default quota
    one million times / day.

    API Reference
    -------------
    http://developer.baidu.com/map/index.php?
    title=webapi/guide/webservice-geocoding

    Get Baidu key
    ------------
    http://lbsyun.baidu.com/apiconsole/key

    OSM Quality (0/6)
    -----------------
    - [ ] addr:housenumber
    - [ ] addr:street
    - [ ] addr:city
    - [ ] addr:state
    - [ ] addr:country
    - [ ] addr:postal

    Attributes (8/18)
    -----------------
    - [ ] accuracy
    - [ ] address
    - [ ] bbox
    - [ ] city
    - [ ] confidence
    - [ ] country
    - [x] encoding
    - [ ] housenumber
    - [x] lat
    - [x] lng
    - [x] location
    - [x] ok
    - [ ] postal
    - [x] provider
    - [x] quality
    - [ ] state
    - [x] status
    - [ ] street

    """
    provider = 'baidu'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'http://api.map.baidu.com/geocoder/v2/'
        self.location = location
        self.params = {
            'address': location,
            'output': 'json',
            'ak': kwargs.get('key', baidu_key),
        }
        self.headers = {
            'Referer': kwargs.get('referer', 'http://developer.baidu.com'),
        }
        self._initialize(**kwargs)

    @property
    def lat(self):
        return self.parse['location'].get('lat')

    @property
    def lng(self):
        return self.parse['location'].get('lng')

    @property
    def quality(self):
        return self.parse['result'].get('level')

    @property
    def accuracy(self):
        return self.parse['result'].get('confidence')

if __name__ == '__main__':
    g = Baidu('中国')
    import json
    print(json.dumps(g.json, indent=4))
    g.debug()
