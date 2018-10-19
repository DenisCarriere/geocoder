#!/usr/bin/python
# coding: utf8

import geocoder

location = '1552 Payette dr., Ottawa'


def test_geocodexyz():
    g = geocoder.geocodexyz(location)
    assert g.ok
    osm_count, fields_count = g.debug()[0]
    assert osm_count >= 5
    assert fields_count >= 11
    assert isinstance(g.confidence, float)
    assert isinstance(g.remaining_credits, int)
