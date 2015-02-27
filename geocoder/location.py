#!/usr/bin/python
# coding: utf8
import re


class Location(object):
    """ Location container """

    def __init__(self, location):
        self._check_input(location)

    def __repr__(self):
        return '<[{0}] Location [{1}]>'.format(self.status, self.latlng)

    @property
    def ok(self):
        if self.latlng:
            return True
        else:
            return False

    @property
    def status(self):
        if self.ok:
            return 'OK'
        elif self.error:
            return self.error

    def _convert_float(self, number):
        try:
            return float(number)
        except ValueError:
            return None

    def _check_input(self, location):
        # Checking for a String
        if isinstance(location, str):
            expression = r"[-]?\d+[.]?[-]?[\d]+"
            pattern = re.compile(expression)
            match = pattern.findall(location)
            if len(match) == 2:
                lat, lng = match
                self._check_for_list([lat, lng])

        # Checking for List of Tuple
        if isinstance(location, (list, tuple)):
            self._check_for_list(location)

        # Checking for Dictionary
        elif isinstance(location, dict):
            self._check_for_dict(location)

        # Checking for a Geocoder Class
        elif hasattr(location, 'latlng'):
            self.lat, self.lng = location.latlng

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

                # Check if inputs are within the World Geographical boundary (90,180,-90,-180)
                if bool(condition_3 and condition_4):
                    self.lat = lat
                    self.lng = lng
                    return self.lat, self.lng
                else:
                    self.error = 'ERROR - Lat & Lng are not within the world\'s geographical boundary.'
            else:
                self.error = 'ERROR - Lat & Lng are not floats.'

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
            return '{0}, {1}'.format(self.lat, self.lng)


if __name__ == '__main__':
    l = Location('45.123, 0.0')
    print(l.latlng)