#!/usr/bin/python
# coding: utf8

import ratelim
import requests
from .base import Base


class Google(Base):
    """
    Google Geocoding API
    ====================
    Geocoding is the process of converting addresses into geographic
    coordinates (like latitude 37.423021 and longitude -122.083739),
    which you can use to place markers or position the map.

    API Reference
    -------------
    https://developers.google.com/maps/documentation/geocoding

    Parameters
    ----------
    :param location: Your search location you want geocoded.
    :param method: (default=geocode) Use the following:
        > geocode
        > reverse
        > batch
        > timezone
        > elevation
    """
    provider = 'google'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'https://maps.googleapis.com/maps/api/geocode/json'
        self.location = location
        self.params = {
            'sensor': 'false',
            'address': location,
            'key': kwargs.get('key', ''),
        }
        self._initialize(**kwargs)
        self._google_catch_errors()

    @staticmethod
    @ratelim.greedy(2500, 60 * 60 * 24)
    @ratelim.greedy(5, 1)
    def rate_limited_get(*args, **kwargs):
        return requests.get(*args, **kwargs)

    def _google_catch_errors(self):
        status = self.parse.get('status')
        if not status == 'OK':
            self.error = status

    def _exceptions(self):
        # Build intial Tree with results
        if self.parse['results']:
            self._build_tree(self.parse.get('results')[0])

            # Build Geometry
            self._build_tree(self.parse.get('geometry'))

            # Parse address components with short & long names
            for item in self.parse['address_components']:
                for category in item['types']:
                    self.parse[category]['long_name'] = self._encode(item['long_name'])
                    self.parse[category]['short_name'] = self._encode(item['short_name'])

    @property
    def lat(self):
        return self.parse['location'].get('lat')

    @property
    def lng(self):
        return self.parse['location'].get('lng')

    @property
    def quality(self):
        quality = self.parse.get('types')
        if quality:
            return quality[0]

    @property
    def accuracy(self):
        return self.parse.get('location_type')

    @property
    def bbox(self):
        south = self.parse['southwest'].get('lat')
        west = self.parse['southwest'].get('lng')
        north = self.parse['northeast'].get('lat')
        east = self.parse['northeast'].get('lng')
        return self._get_bbox(south, west, north, east)

    @property
    def address(self):
        return self.parse.get('formatted_address')

    @property
    def postal(self):
        return self.parse['postal_code'].get('short_name')

    @property
    def subpremise(self):
        return self.parse['subpremise'].get('short_name')

    @property
    def housenumber(self):
        return self.parse['street_number'].get('short_name')

    @property
    def street(self):
        return self.parse['route'].get('short_name')

    @property
    def road_long(self):
        return self.parse['route'].get('long_name')

    @property
    def neighborhood(self):
        return self.parse['neighborhood'].get('short_name')

    @property
    def sublocality(self):
        return self.parse['sublocality'].get('short_name')

    @property
    def city(self):
        return self.parse['locality'].get('short_name')

    @property
    def city_long(self):
        return self.parse['locality'].get('long_name')

    @property
    def county(self):
        return self.parse['administrative_area_level_2'].get('short_name')

    @property
    def state(self):
        return self.parse['administrative_area_level_1'].get('short_name')

    @property
    def state_long(self):
        return self.parse['administrative_area_level_1'].get('long_name')

    @property
    def country(self):
        return self.parse['country'].get('short_name')

    @property
    def country_long(self):
        return self.parse['country'].get('long_name')

if __name__ == '__main__':
    g = Google('11 Wall Street, New York')
