#!/usr/bin/python
# coding: utf8

import geocoder

g = geocoder.google('Ottawa, ON')

print g.address
print g.latlng
print g.json