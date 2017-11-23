#!/usr/bin/python
# coding: utf8
import geocoder

location = '8.8.8.8'


def test_maxmind():
    g = geocoder.maxmind(location)
    assert g.ok
    osm_count, fields_count = g.debug()[0]
    assert osm_count >= 1
    assert fields_count >= 13
