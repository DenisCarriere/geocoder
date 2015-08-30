#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base
from geocoder.keys import mapbox_access_token


class Mapbox(Base):
    """
    Mapbox Geocoding
    ================
    The Mapbox Geocoding API lets you convert location text into
    geographic coordinates (1600 Pennsylvania Ave NW → -77.0366,38.8971).

    API Reference
    -------------
    https://www.mapbox.com/developers/api/geocoding/

    Get Mapbox Access Token
    -----------------------
    https://www.mapbox.com/account
    """
    provider = 'mapbox'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.location = location
        access_token = kwargs.get('key', mapbox_access_token)
        if not access_token:
            raise ValueError('Provide access token')
        self.url = 'https://api.mapbox.com/v4/geocode/' \
                   'mapbox.places/{0}.json'.format(location)
        proximity = kwargs.get('proximity')
        self.params = {
            'proximity': proximity,
            'access_token': access_token,
        }
        self._initialize(**kwargs)

    def _exceptions(self):
        # Build intial Tree with results
        features = self.parse['features']
        if features:
            self._build_tree(features[0])

            for item in self.parse['context']:
                if '.' in item['id']:
                    # attribute=country & text=Canada
                    attribute = item['id'].split('.')[0]
                    self.parse[attribute] = item['text']

    @property
    def lat(self):
        coord = self.parse['geometry']['coordinates']
        if coord:
            return coord[1]

    @property
    def lng(self):
        coord = self.parse['geometry']['coordinates']
        if coord:
            return coord[0]

    @property
    def address(self):
        return self.parse.get('place_name')

    @property
    def housenumber(self):
        return self.parse.get('address')

    @property
    def street(self):
        return ''

    @property
    def city(self):
        return self.parse.get('place')

    @property
    def state(self):
        return self.parse.get('region')

    @property
    def country(self):
        return self.parse.get('country')

    @property
    def postal(self):
        return self.parse.get('postcode')

    @property
    def accuracy(self):
        if self.interpolated:
            return "interpolated"

    @property
    def quality(self):
        return self.parse.get('relevance')

    @property
    def interpolated(self):
        return self.parse['geometry'].get('interpolated')

    @property
    def bbox(self):
        if self.parse['bbox']:
            west = self.parse['bbox'][0]
            south = self.parse['bbox'][1]
            east = self.parse['bbox'][2]
            north = self.parse['bbox'][3]
            return self._get_bbox(south, west, north, east)

if __name__ == '__main__':
    g = Mapbox('453 Booth street, Ottawa Ontario')
    g.debug()
