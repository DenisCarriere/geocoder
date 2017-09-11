# coding: utf8

import geocoder

location = 'Ottawa'


def test_ottawa():
    g = geocoder.ottawa(location)
    assert g.ok


def test_multi_results():
    g = geocoder.ottawa(location, maxRows=3)
    assert len(g) == 3
