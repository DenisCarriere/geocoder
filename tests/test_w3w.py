#!/usr/bin/python
# coding: utf8
import geocoder

location = 'index.home.raft'
ottawa = (45.4215296, -75.6971930)


def test_w3w():
    g = geocoder.w3w(location)
    assert g.ok
    osm_count, fields_count = g.debug()[0]
    assert osm_count == 0
    assert fields_count >= 7


def test_w3w_reverse():
    g = geocoder.w3w(ottawa, method='reverse')
    assert g.ok
