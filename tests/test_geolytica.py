#!/usr/bin/python
# coding: utf8

import geocoder

location = '1552 Payette dr., Ottawa'


def test_geolytica():
    g = geocoder.geolytica(location)
    assert g.ok
