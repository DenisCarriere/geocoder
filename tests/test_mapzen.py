# coding: utf8

import geocoder

location = 'Ottawa'


def test_mapzen():
    g = geocoder.mapzen(location)
    assert g.ok


def test_mapzen_reverse():
    g = geocoder.mapzen("45.4049053 -75.7077965", method='reverse')
    assert g.ok


def test_multi_results():
    g = geocoder.mapzen(location, maxRows=3)
    assert len(g) == 3
