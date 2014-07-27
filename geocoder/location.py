#!/usr/bin/python
# coding: utf8

from .google import Google


class Location(object):
    """ Location container """

    lat = None
    lng = None
    latlng = None

    def __init__(self, location):
        self.name = location

        # Functions
        self.lat, self.lng = self.check_input(location)

    def __repr__(self):
        return '<Location [{0}]>'.format(self.name)

    def convert_float(self, number):
        try:
            return float(number)
        except ValueError:
            return None

    def check_input(self, location):
        lat, lng = 0.0, 0.0

        # Checking for a String
        if isinstance(location, str):
            g = Google(location)
            lat, lng = g.lat, g.lng

        # Checking for List of Tuple
        if isinstance(location, (list, tuple)):
            lat, lng = self.check_for_list(location)

        # Checking for Dictionary
        elif isinstance(location, dict):
            lat, lng = self.check_for_dict(location)

        # Checking for a Geocoder Class
        elif hasattr(location, 'latlng'):
            lat, lng = location.latlng

        # Return Results
        return lat, lng

    def check_for_list(self, location):
        # Standard LatLng list or tuple with 2 number values
        if len(location) == 2:
            lat = self.convert_float(location[0])
            lng = self.convert_float(location[1])
            if bool(lat and lng):
                return lat, lng

    def check_for_dict(self, location):
        # Standard LatLng list or tuple with 2 number values
        if bool('lat' in location and 'lng' in location):
            lat = self.convert_float(location.get('lat'))
            lng = self.convert_float(location.get('lng'))
            if bool(lat and lng):
                return lat, lng

if __name__ == '__main__':
    pass

