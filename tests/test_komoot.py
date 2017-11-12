#!/usr/bin/python
# coding: utf8

import geocoder

location = 'Ottawa, Ontario'
ottawa = (45.4215296, -75.6971930)


def test_komoot():
    g = geocoder.komoot(location, timeout=10)
    assert g.ok
    assert len(g) == 1
    osm_count, fields_count = g.debug()[0]
    assert osm_count >= 3
    assert fields_count >= 15


def test_komoot_multi_result():
    g = geocoder.komoot(location, maxRows=3, timeout=10)
    assert g.ok
    assert len(g) == 3


def test_komoot_reverse():
    g = geocoder.komoot(ottawa, method='reverse', timeout=10)
    assert g.ok
