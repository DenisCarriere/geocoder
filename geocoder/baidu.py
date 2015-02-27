#!/usr/bin/python
# coding: utf8

from .base import Base
from .keys import baidu_key


class Baidu(Base):
    """
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
        self._initialize(**kwargs)

    def _exceptions(self):
        # Build intial Tree with results
        sets = self.parse['resourceSets']
        if sets:
            resources = sets[0]['resources']
            if resources:
                self._build_tree(resources[0])

            for item in self.parse['geocodePoints']:
                self._build_tree(item)

    @property
    def lat(self):
        coord = self.parse['point']['coordinates']
        if coord:
            return coord[0] 

    @property
    def lng(self):
        coord = self.parse['point']['coordinates']
        if coord:
            return coord[1]

    @property
    def address(self):
        return self.parse['address'].get('formattedAddress')

    @property
    def housenumber(self):
        if self.street:
            expression = r'\d+'
            pattern = re.compile(expression)
            match = pattern.search(str(self.street))
            if match:
                return match.group(0)

    @property
    def street(self):
        return self.parse['address'].get('addressLine')

    @property
    def city(self):
        return self.parse['address'].get('locality')

    @property
    def state(self):
        return self.parse['address'].get('adminDistrict')

    @property
    def country(self):
        return self.parse['address'].get('countryRegion')

    @property
    def quality(self):
        return self.parse.get('entityType')

    @property
    def accuracy(self):
        return self.parse.get('calculationMethod')

    @property
    def postal(self):
        return self.parse['address'].get('postalCode')

    @property
    def bbox(self):
        if self.parse['bbox']:
            south = self.parse['bbox'][0]
            north = self.parse['bbox'][2]
            west = self.parse['bbox'][1]
            east = self.parse['bbox'][3]
            return self._get_bbox(south, west, north, east)

if __name__ == '__main__':
    g = Baidu('China')
    g.debug()