#!/usr/bin/python
# coding: utf8

from .base import Base
from .keys import mapquest_key
from .mapquest import Mapquest
from .location import Location


class MapquestReverse(Mapquest, Base):
    """
    MapQuest
    ========
    The geocoding service enables you to take an address and get the
    associated latitude and longitude. You can also use any latitude 
    and longitude pair and get the associated address. Three types of 
    geocoding are offered: address, reverse, and batch.

    API Reference
    -------------
    http://www.mapquestapi.com/geocoding/
    
    """
    provider = 'mapquest'
    method = 'reverse'

    def __init__(self, location, **kwargs):
        self.url = 'http://www.mapquestapi.com/geocoding/v1/address'
        self.location = Location(location).latlng
        self.headers = {
            'referer':'http://www.mapquestapi.com/geocoding/',
            'host': 'www.mapquestapi.com',
        }
        self.params = {
            'key': kwargs.get('key', mapquest_key),
            'location': self.location,
            'maxResults': 1,
        }
        self._initialize(**kwargs)

    @property
    def ok(self):
        return bool(self.quality)

if __name__ == '__main__':
    g = MapquestReverse([45.50,-76.05])
    g.debug()