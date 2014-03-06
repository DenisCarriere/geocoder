# -*- coding: utf-8 -*-
from geocoder import Geocoder
from google import Google


class Location(object):
    """ Location container """

    lat = None
    lng = None
    latlng = None

    def __init__(self, location):
        self.name = location

        # Functions
        self.lat, self.lng = self.check_input(location)
        self.other_format()
        
    def __repr__(self):
        return '<Location [{0}]>'.format(self.name)

    def other_format(self):
        if bool(self.lat and self.lng):
            self.latlng = self.lat, self.lng

    def convert_float(self, number):
        try:
            return float(number)
        except ValueError:
            print '<ERROR - Input not a number>'
            return None

    def check_input(self, location):
        lat, lng = 0.0, 0.0

        # Checking for a String
        if isinstance(location, str):
            lat, lng = Geocoder(Google(location)).latlng

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
    c = {'lat':45.4215296, 'lng':-75.69719309999999}
    b = (45.4215296, -75.69719309999999)
    a = Location(c)
    print a.latlng

