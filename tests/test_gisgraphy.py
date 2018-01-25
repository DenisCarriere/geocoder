#!/usr/bin/python
# coding: utf-8

import geocoder

location = 'Ottawa, Ontario'
ottawa = (45.4215296, -75.6971930)


def test_gisgraphy():
    g = geocoder.gisgraphy(location, timeout=10)
    assert g.ok
    assert len(g) == 1
    osm_count, fields_count = g.debug()[0]
    assert osm_count >= 3
    assert fields_count >= 9


def test_gisgraphy_multi_result():
    print(geocoder.komoot)
    print(geocoder.gisgraphy)
    
    g = geocoder.gisgraphy(location, maxRows=3, timeout=10)
    assert g.ok
    assert len(g) == 3


def test_gisgraphy_reverse():
    g = geocoder.gisgraphy(ottawa, method='reverse', timeout=10)
    assert g.ok
