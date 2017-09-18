#!/usr/bin/python
# coding: utf8

import re
import geocoder
from six import string_types
try:
    from statistics import mean
except ImportError:
    def mean(args):
        return sum(args) / len(args)


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
        return bool(self.latlng)

    @staticmethod
    def _convert_float(number):
        try:
            return float(number)
        except ValueError:
            return None

    def _check_input(self, location):
        # Checking for a LatLng String
        if isinstance(location, string_types):
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
            raise ValueError("Unknown location: %s" % location)

    def _check_for_list(self, location):
        # Standard LatLng list or tuple with 2 number values
        if len(location) == 2:
            lat = self._convert_float(location[0])
            lng = self._convert_float(location[1])
            condition_1 = isinstance(lat, float)
            condition_2 = isinstance(lng, float)

            # Check if input are Floats
            if condition_1 and condition_2:
                condition_3 = -90 <= lat <= 90
                condition_4 = -180 <= lng <= 180

                # Check if inputs are within the World Geographical
                # boundary (90,180,-90,-180)
                if condition_3 and condition_4:
                    self.lat = lat
                    self.lng = lng
                    return self.lat, self.lng
                else:
                    raise ValueError(
                        "Coords are not within the world's geographical boundary")
            else:
                raise ValueError("Coordinates must be numbers")

    def _check_for_dict(self, location):
        # Standard LatLng list or tuple with 2 number values
        if 'lat' in location and 'lng' in location:
            lat = location['lat']
            lng = location['lng']
            self._check_for_list([lat, lng])

        if 'y' in location and 'x' in location:
            lat = location['y']
            lng = location['x']
            self._check_for_list([lat, lng])

    @property
    def latlng(self):
        if isinstance(self.lat, float) and isinstance(self.lng, float):
            return [self.lat, self.lng]
        return []

    @property
    def latitude(self):
        return self.lat

    @property
    def longitude(self):
        return self.lng

    @property
    def xy(self):
        if isinstance(self.lat, float) and isinstance(self.lng, float):
            return [self.lng, self.lat]
        return []

    def __str__(self):
        if self.ok:
            return u'{0}, {1}'.format(self.lat, self.lng)
        return u''


class BBox(object):
    """BBox container"""

    DEGREES_TOLERANCE = 0.5

    @classmethod
    def factory(cls, arg):
        # validate input first
        if not isinstance(arg, (list, dict)):
            raise ValueError(
                "BBox factory only accept a dict or a list as argument")
        # we have a dict... just check which fields are given
        if isinstance(arg, dict):
            if 'southwest' in arg:
                return cls(bounds=arg)
            elif 'bbox' in arg:
                return cls(bbox=arg['bbox'])
            elif 'bounds' in arg:
                return cls(bounds=arg['bounds'])
            elif 'lat' in arg:
                return cls(lat=arg['lat'], lng=arg['lng'])
            elif 'west' in arg:
                return cls(west=arg['west'], south=arg['south'],
                           east=arg['east'], north=arg['north'])
            else:
                raise ValueError(
                    "Could not found valid values in dict to create a bbox")
        # we have a list... guess what to call according to the number of parameters given:
        if len(arg) == 2:
            lat, lng = arg
            return cls(lat=lat, lng=lng)
        elif len(arg) == 4:
            return cls(bbox=arg)
        else:
            raise ValueError(
                "Could not found valid values in list to create a bbox")

    def __init__(self, bbox=None, bounds=None,
                 lat=None, lng=None,
                 west=None, south=None, east=None, north=None):
        if bounds is not None and bounds.get('southwest') and bounds.get('northeast'):
            self.south, self.west = map(float, bounds['southwest'])
            self.north, self.east = map(float, bounds['northeast'])
        elif bbox is not None and all(bbox):
            self.west, self.south, self.east, self.north = map(float, bbox)
        elif lat is not None and lng is not None:
            self.south = float(lat) - self.DEGREES_TOLERANCE
            self.north = float(lat) + self.DEGREES_TOLERANCE
            self.west = float(lng) - self.DEGREES_TOLERANCE
            self.east = float(lng) + self.DEGREES_TOLERANCE
        elif all([west, south, east, north]):
            self.west, self.south, self.east, self.north = map(
                float, [west, south, east, north])
        else:
            raise ValueError("Could not create BBox/Bounds from given arguments")

    @property
    def lat(self):
        return mean([self.south, self.north])

    @property
    def lng(self):
        return mean([self.west, self.east])

    @property
    def latlng(self):
        if isinstance(self.lat, float) and isinstance(self.lng, float):
            return [self.lat, self.lng]
        return []

    @property
    def latitude(self):
        return self.lat

    @property
    def longitude(self):
        return self.lng

    @property
    def xy(self):
        if isinstance(self.lat, float) and isinstance(self.lng, float):
            return [self.lng, self.lat]
        return []

    @property
    def as_dict(self):
        return {
            'northeast': [self.north, self.east],
            'southwest': [self.south, self.west]
        }


if __name__ == '__main__':
    l = Location([0.0, 0.0])
    print(l.lng)
