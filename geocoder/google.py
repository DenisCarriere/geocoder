#!/usr/bin/python
# coding: utf8

import ratelim
import requests
from base import Base


class Google(Base):
    """
    Google Geocoding API
    ====================
    Geocoding is the process of converting addresses (like "1600 Amphitheatre Parkway,
    Mountain View, CA") into geographic coordinates (like latitude 37.423021 and
    longitude -122.083739), which you can use to place markers or position the map.

    API Reference
    -------------
    https://developers.google.com/maps/documentation/geocoding/

    OSM Quality (6/6)
    -----------------
    [x] addr:housenumber
    [x] addr:street
    [x] addr:city
    [x] addr:state
    [x] addr:country
    [x] addr:postal

    Attributes (19/21)
    ------------------
    [x] accuracy
    [x] address
    [x] bbox
    [x] city
    [x] confidence
    [x] country
    [x] county
    [x] housenumber
    [x] lat
    [x] lng
    [x] location
    [x] neighborhood
    [x] ok
    [x] postal
    [x] provider
    [x] quality
    [x] state
    [x] status
    [x] street
    [ ] sublocality
    [ ] subpremise
    """
    provider = 'google'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'https://maps.googleapis.com/maps/api/geocode/json'
        self.location = location
        self.short_name = kwargs.get('short_name', False)
        self.params = {
            'sensor': 'false',
            'address': location,
            'key': kwargs.get('key', ''),
        }
        self._initialize(**kwargs)
        self._google_catch_errors()

    @staticmethod
    @ratelim.greedy(2500, 60*60*24)
    @ratelim.greedy(5, 1)
    def rate_limited_get(*args, **kwargs):
        return requests.get(*args, **kwargs)

    def _google_catch_errors(self):
        status = self.parse['status']
        if not status == 'OK':
            self.error = status

    def _exceptions(self):
        # Build intial Tree with results
        if self.parse['results']:
            self._build_tree(self.parse['results'][0])

            # Build Geometry
            self._build_tree(self.parse['geometry'])

            # Parse address components with short & long names
            for item in self.parse['address_components']:
                for category in item['types']:
                    self.parse[category]['long_name'] = item['long_name'].encode('utf-8')
                    self.parse[category]['short_name'] = item['short_name'].encode('utf-8')

    @property
    def lat(self):
        return self.parse['location']['lat']

    @property
    def lng(self):
        return self.parse['location']['lng']

    @property
    def quality(self):
        return self.parse['types'][0]

    @property
    def accuracy(self):
        return self.parse['location_type']

    @property
    def bbox(self):
        south = self.parse['southwest']['lat']
        west = self.parse['southwest']['lng']
        north = self.parse['northeast']['lat']
        east = self.parse['northeast']['lng']
        return self._get_bbox(south, west, north, east)

    @property
    def address(self):
        return self.parse['formatted_address']

    @property
    def postal(self):
        if self.short_name:
            return self.parse['postal_code']['short_name']
        else:
            return self.parse['postal_code']['long_name']

    @property
    def subpremise(self):
        if self.short_name:
            return self.parse['subpremise']['short_name']
        else:
            return self.parse['subpremise']['long_name']

    @property
    def housenumber(self):
        if self.short_name:
            return self.parse['street_number']['short_name']
        else:
            return self.parse['street_number']['long_name']

    @property
    def street(self):
        if self.short_name:
            return self.parse['route']['short_name']
        else:
            return self.parse['route']['long_name']

    @property
    def neighborhood(self):
        if self.short_name:
            return self.parse['neighborhood']['short_name']
        else:
            return self.parse['neighborhood']['long_name']

    @property
    def sublocality(self):
        if self.short_name:
            return self.parse['sublocality']['short_name']
        else:
            return self.parse['sublocality']['long_name']

    @property
    def city(self):
        if self.short_name:
            return self.parse['locality']['short_name']
        else:
            return self.parse['locality']['long_name']

    @property
    def county(self):
        if self.short_name:
            return self.parse['administrative_area_level_2']['short_name']
        else:
            return self.parse['administrative_area_level_2']['long_name']

    @property
    def state(self):
        if self.short_name:
            return self.parse['administrative_area_level_1']['short_name']
        else:
            return self.parse['administrative_area_level_1']['long_name']

    @property
    def country(self):
        if self.short_name:
            return self.parse['country']['short_name']
        else:
            return self.parse['country']['long_name']

if __name__ == '__main__':
    g = Google('453 Booth street, Ottawa')
    g.debug()