#!/usr/bin/python
# coding: utf8

import re
import sys
import geocoder

# Unicode type compatible with Python3
is_python3 = sys.version_info.major == 3
if is_python3:
    unicode = str


class Location(object):
    """ Location container """
    lat = None
    lng = None

    def __init__(self, location, **kwargs):
        self.location = location
        self.kwargs = kwargs
        self._check_input(location)

    @property
    def ok(self):
        if self.latlng:
            return True
        else:
            return False

    def _convert_float(self, number):
        try:
            return float(number)
        except ValueError:
            return None

    def _check_input(self, location):
        # Checking for a LatLng String
        if isinstance(location, (str, unicode)):
            expression = r"[-]?\d+[.]?[-]?[\d]+"
            pattern = re.compile(expression)
            match = pattern.findall(location)
            if len(match) == 2:
                lat, lng = match
                self._check_for_list([lat, lng])
            else:
                # Check for string to Geocode using a provider
                provider = self.kwargs.get('provider', 'osm')
                g = geocoder.get(location, provider=provider)
                if g.ok:
                    self.lat, self.lng = g.lat, g.lng

        # Checking for List of Tuple
        elif isinstance(location, (list, tuple)):
            self._check_for_list(location)

        # Checking for Dictionary
        elif isinstance(location, dict):
            self._check_for_dict(location)

        # Checking for a Geocoder Class
        elif hasattr(location, 'latlng'):
            if location.latlng:
                self.lat, self.lng = location.latlng

        # Result into Error
        else:
            print('[ERROR] Please provide a correct location\n'
                  '>>> g = geocoder.location("Ottawa ON")\n'
                  '>>> g = geocoder.location([45.23, -75.12])\n'
                  '>>> g = geocoder.location("45.23, -75.12")\n'
                  '>>> g = geocoder.location({"lat": 45.23, "lng": -75.12})')
            sys.exit()

    def _check_for_list(self, location):
        # Standard LatLng list or tuple with 2 number values
        if len(location) == 2:
            lat = self._convert_float(location[0])
            lng = self._convert_float(location[1])
            condition_1 = isinstance(lat, float)
            condition_2 = isinstance(lng, float)

            # Check if input are Floats
            if bool(condition_1 and condition_2):
                condition_3 = lat <= 90 and lat >= -90
                condition_4 = lng <= 180 and lng >= -180

                # Check if inputs are within the World Geographical
                # boundary (90,180,-90,-180)
                if bool(condition_3 and condition_4):
                    self.lat = lat
                    self.lng = lng
                    return self.lat, self.lng
                else:
                    print("[ERROR] Coords are not within the world's geographical boundary\n"
                          'Latitudes must be within -90 to 90 degrees\n'
                          'Longitude must be within -180 to 180 degrees')
                    sys.exit()
            else:
                print("[ERROR] Coordinates must be numbers.\n"
                      '>>> g = geocoder.location("Ottawa ON")\n'
                      '>>> g = geocoder.location([45.23, -75.12])\n'
                      '>>> g = geocoder.location("45.23, -75.12")\n'
                      '>>> g = geocoder.location({"lat": 45.23, "lng": -75.12})')
                sys.exit()

    def _check_for_dict(self, location):
        # Standard LatLng list or tuple with 2 number values
        if bool('lat' in location and 'lng' in location):
            lat = location.get('lat')
            lng = location.get('lng')
            self._check_for_list([lat, lng])

        if bool('y' in location and 'x' in location):
            lat = location.get('y')
            lng = location.get('x')
            self._check_for_list([lat, lng])

    @property
    def latlng(self):
        condition1 = isinstance(self.lat, float)
        condition2 = isinstance(self.lng, float)
        if bool(condition1 and condition2):
            return [self.lat, self.lng]
        return []

    @property
    def xy(self):
        condition1 = isinstance(self.lat, float)
        condition2 = isinstance(self.lng, float)
        if bool(condition1 and condition2):
            return [self.lng, self.lat]
        return []

    def __str__(self):
        if self.ok:
            return '{0}, {1}'.format(self.lat, self.lng)
        return ''

if __name__ == '__main__':
    l = Location("Ottawa, ON")
    print(l.latlng)