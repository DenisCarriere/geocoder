# coding: utf8

import geocoder

location = 'Ottawa'


def test_tomtom():
    g = geocoder.tomtom(location)
    assert g.ok


def test_multi_results():
    g = geocoder.tomtom(location, maxRows=3)
    assert len(g) == 3
