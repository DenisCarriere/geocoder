#!/usr/bin/python
# coding: utf8

import geocoder

location = 'Ottawa, Ontario'
ottawa = (45.4215296, -75.6971930)


def test_here():
    g = geocoder.here(location)
    assert g.ok
    osm_count, fields_count = g.debug()[0]
    assert osm_count == 4
    assert fields_count == 13


def test_here_reverse():
    g = geocoder.here(ottawa, method='reverse')
    assert g.ok
