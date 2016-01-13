#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base
from geocoder.mapbox import Mapbox
from geocoder.keys import mapbox_access_token
from geocoder.location import Location


class MapboxReverse(Mapbox, Base):
    """
    Mapbox Reverse Geocoding
    ========================
    Reverse geocoding lets you reverse this process, turning a
    pair of lat/lon coordinates into a meaningful place name
    (-77.036,38.897 → 1600 Pennsylvania Ave NW).

    API Reference
    -------------
    https://www.mapbox.com/developers/api/geocoding/

    Get Mapbox Access Token
    -----------------------
    https://www.mapbox.com/account
    """
    provider = 'mapbox'
    method = 'reverse'

    def __init__(self, location, **kwargs):
        self.location = str(Location(location))
        lat, lng = Location(location).latlng
        self.url = 'https://api.mapbox.com/geocoding/v5/mapbox.places/'\
                   '{lng},{lat}.json'.format(lng=lng, lat=lat)
        self.params = {
            'access_token': self._get_api_key(mapbox_access_token, **kwargs),
            'country': kwargs.get('country'),
            'proximity': self._get_proximity(),
            'types': kwargs.get('types'),
        }
        self._initialize(**kwargs)

    @property
    def ok(self):
        return bool(self.address)

if __name__ == '__main__':
    g = MapboxReverse([45.4049053, -75.7077965])
    g.debug()
