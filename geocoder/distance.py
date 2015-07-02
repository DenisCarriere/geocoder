#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from math import radians, cos, sin, asin, sqrt
from geocoder.location import Location

AVG_EARTH_RADIUS = 6371  # in km


def Distance(*args, **kwargs):
    total = 0.0
    last = None

    if len(args) == 1 and isinstance(args, (list, tuple)):
        args = args[0]

    if len(args) <= 1:
        raise ValueError("Distance needs at least two locations")

    for location in args:
        if last:
            distance = haversine(Location(last), Location(location), **kwargs)
            if distance:
                total += distance
        last = location

    return total


def haversine(point1, point2, **kwargs):
    """ Calculate the great-circle distance bewteen two points on the Earth surface.

    :input: two 2-tuples, containing the latitude and longitude of each point
    in decimal degrees.

    Example: haversine((45.7597, 4.8422), (48.8567, 2.3508))

    :output: Returns the distance bewteen the two points.
    The default unit is kilometers. Miles can be returned
    if the ``miles`` parameter is set to True.

    """

    lookup_units = {
        'miles': 'miles',
        'mile': 'miles',
        'mi': 'miles',
        'ml': 'miles',
        'kilometers': 'kilometers',
        'kilometres': 'kilometers',
        'kilometer': 'kilometers',
        'kilometre': 'kilometers',
        'km': 'kilometers',
        'meters': 'meters',
        'metres': 'meters',
        'meter': 'meters',
        'metre': 'meters',
        'm': 'meters',
        'feet': 'feet',
        'f': 'feet',
        'ft': 'feet',
    }

    if point1.ok and point2.ok:
        # convert all latitudes/longitudes from decimal degrees to radians
        lat1, lng1, lat2, lng2 = list(map(radians, point1.latlng + point2.latlng))

        # calculate haversine
        lat = lat2 - lat1
        lng = lng2 - lng1
        d = sin(lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(lng / 2) ** 2
        h = 2 * AVG_EARTH_RADIUS * asin(sqrt(d))

        # Measurements
        units = kwargs.get('units', 'kilometers').lower()
        units_calculation = {
            'miles': h * 0.621371,
            'feet': h * 0.621371 * 5280,
            'meters': h * 1000,
            'kilometers': h,
        }

        if units in lookup_units:
            return units_calculation[lookup_units[units]]
        else:
            raise ValueError("Unknown units of measurement")

    else:
        print('[WARNING] Error calculating the following two locations.\n'
              'Points: {0} to {1}'.format(point1.location, point2.location))

if __name__ == '__main__':
    d = Distance('Ottawa, ON', 'Toronto, ON', 'Montreal, QC')
    print(d)
