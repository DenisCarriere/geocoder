#!/usr/bin/python
# coding: utf8

import geocoder

latlng = (45.4215296, -75.6971931)
g = geocoder.elevation(latlng)
#OR
g = geocoder.elevation("Ottawa, ON")

print g.elevation
