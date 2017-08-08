#!/usr/bin/python
# coding: utf8

import geocoder

location = 'Ottawa'
city = 'Ottawa'
ottawa = (45.50, -76.05)


def test_mapquest():
    g = geocoder.mapquest(location)
    assert g.ok


def test_mapquest_reverse():
    g = geocoder.mapquest(ottawa, method='reverse')
    assert g.ok


def test_multi_results():
    g = geocoder.mapquest(location, maxRows=3)
    assert len(g) == 3
