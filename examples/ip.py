#!/usr/bin/python
# coding: utf8

import geocoder

g = geocoder.ip('199.7.XXX.XX')
#OR
g = geocoder.ip('me')

print g.address
print g.latlng