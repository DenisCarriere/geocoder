#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.mapbox import MapboxResult, MapboxQuery
from geocoder.location import Location


class MapboxReverseResult(MapboxResult):

    @property
    def ok(self):
        return bool(self.address)


class MapboxReverse(MapboxQuery):
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

    _URL = 'https://api.mapbox.com/geocoding/v5/mapbox.places/{lng},{lat}.json'

    def _build_params(self, location, provider_key, **kwargs):
        return {
            'access_token': provider_key,
            'country': kwargs.get('country'),
            'types': kwargs.get('types'),
        }

    def _before_initialize(self, location, **kwargs):
        self.location = str(Location(location))
        lat, lng = Location(location).latlng
        self.url = self.url.format(lng=lng, lat=lat)


if __name__ == '__main__':
    g = MapboxReverse([45.4049053, -75.7077965])
    g.debug()
