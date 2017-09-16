#!/usr/bin/python
# coding: utf8

import geocoder

location = 'Ottawa, Ontario'
city = 'Ottawa'
ottawa = (45.4215296, -75.6971930)


def test_mapbox():
    g = geocoder.mapbox(location)
    assert g.ok
    osm_count, fields_count = g.debug()[0]
    assert osm_count == 2
    assert fields_count == 11


def test_mapbox_reverse():
    g = geocoder.mapbox(ottawa, method='reverse')
    assert g.ok


def test_multi_results():
    g = geocoder.mapbox(location)
    assert len(g) == 5
