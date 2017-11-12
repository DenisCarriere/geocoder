#!/usr/bin/python
# coding: utf8

import geocoder

location = '99.240.181.199'


def test_ipinfo():
    g = geocoder.ipinfo(location)
    assert g.ok
    osm_count, fields_count = g.debug()[0]
    assert osm_count >= 4
    assert fields_count >= 12
