#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base


class Komoot(Base):
    """
    Komoot REST API
    =======================

    API Reference
    -------------
    http://photon.komoot.de
    """
    provider = 'komoot'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'http://photon.komoot.de/api'
        self.location = location
        self.params = {
            'q': location,
            'limit': kwargs.get('result', 1),
            'lang': 'en',
        }
        self._initialize(**kwargs)

    def _exceptions(self):
        # Only retrieve the first feature
        features = self.parse['features']
        if features:
            self._build_tree(self.parse['features'][0])

    def __iter__(self):
        for item in self.content['features']:
            yield item

    @property
    def lat(self):
        return self.parse['geometry']['coordinates'][1]

    @property
    def lng(self):
        return self.parse['geometry']['coordinates'][0]

    @property
    def bbox(self):
        extent = self.parse['properties']['extent']
        if extent:
            west = extent[0]
            north = extent[1]
            east = extent[2]
            south = extent[3]
            return self._get_bbox(south, west, north, east)

    @property
    def address(self):
        # Ontario, Canada
        address = ', '.join([self.state, self.country])

        # 453 Booth street, Ottawa ON, Canada
        if self.housenumber:
            middle = ', '.join([self.street, self.city])
            address = ' '.join([self.housenumber, middle, address])

        # 453 Booth street, Ottawa ON, Canada
        elif self.street:
            middle = ', '.join([self.street, self.city])
            address = ' '.join([middle, address])

        # Ottawa ON, Canada
        elif self.city:
            address = ' '.join([self.city, address])

        return address

    @property
    def country(self):
        return self.parse['properties'].get('country', '')

    @property
    def state(self):
        if self.osm_value == 'state':
            return self.parse['properties'].get('name', '')
        return self.parse['properties'].get('state', '')

    @property
    def city(self):
        if self.osm_value == 'city':
            return self.parse['properties'].get('name', '')
        return self.parse['properties'].get('city', '')

    @property
    def street(self):
        return self.parse['properties'].get('street', '')

    @property
    def housenumber(self):
        return self.parse['properties'].get('housenumber', '')

    @property
    def postal(self):
        return self.parse['properties'].get('postcode', '')

    @property
    def osm_id(self):
        return self.parse['properties'].get('osm_id', '')

    @property
    def osm_value(self):
        return self.parse['properties'].get('osm_value', '')

    @property
    def osm_key(self):
        return self.parse['properties'].get('osm_key', '')

    @property
    def osm_type(self):
        return self.parse['properties'].get('osm_type', '')

if __name__ == '__main__':
    g = Komoot('Ottawa Ontario', result=3)
    g.debug()
