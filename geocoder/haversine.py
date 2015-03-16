#!/usr/bin/python
# coding: utf8
from math import radians, cos, sin, asin, sqrt
from .location import Location

AVG_EARTH_RADIUS = 6371  # in km


def haversine(point1, point2, miles=False):
    """ Calculate the great-circle distance bewteen two points on the Earth surface.

    :input: two 2-tuples, containing the latitude and longitude of each point
    in decimal degrees.

    Example: haversine((45.7597, 4.8422), (48.8567, 2.3508))

    :output: Returns the distance bewteen the two points.
    The default unit is kilometers. Miles can be returned
    if the ``miles`` parameter is set to True.

    """
    # unpack latitude/longitude
    point1 = Location(point1)
    point2 = Location(point2)

    if bool(point1.ok and point2.ok):
        # convert all latitudes/longitudes from decimal degrees to radians
        lat1, lng1, lat2, lng2 = list(map(radians, point1.latlng + point2.latlng))

        # calculate haversine
        lat = lat2 - lat1
        lng = lng2 - lng1
        d = sin(lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(lng / 2) ** 2
        h = 2 * AVG_EARTH_RADIUS * asin(sqrt(d))
        if miles:
            return h * 0.621371  # in miles
        else:
            return h  # in kilometers
