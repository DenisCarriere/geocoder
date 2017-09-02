#!/usr/bin/python
# coding: utf8

import geocoder

location = 'Ottawa, Ontario'
ottawa = (45.4215296, -75.6971930)


def test_geocodefarm():
    g = geocoder.geocodefarm(location)
    assert g.ok


def test_geocodefarm_reverse():
    g = geocoder.geocodefarm(ottawa, method='reverse')
    assert g.ok
