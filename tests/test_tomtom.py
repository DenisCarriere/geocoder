# coding: utf8

import geocoder

location = 'Ottawa'


def test_tomtom():
    g = geocoder.tomtom(location)
    assert g.ok
    osm_count, fields_count = g.debug()[0]
    assert osm_count >= 2
    assert fields_count >= 12


def test_multi_results():
    g = geocoder.tomtom(location, maxRows=3)
    assert len(g) == 3
