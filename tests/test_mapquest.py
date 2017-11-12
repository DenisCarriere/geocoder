#!/usr/bin/python
# coding: utf8

import geocoder

location = 'Ottawa'
city = 'Ottawa'
ottawa = (45.50, -76.05)


def test_mapquest():
    g = geocoder.mapquest(location, timeout=10)
    assert g.ok
    osm_count, fields_count = g.debug()[0]
    assert osm_count >= 3
    assert fields_count >= 10


def test_mapquest_reverse():
    g = geocoder.mapquest(ottawa, method='reverse', timeout=10)
    assert g.ok


def test_multi_results():
    g = geocoder.mapquest(location, maxRows=3, timeout=10)
    assert len(g) == 3
