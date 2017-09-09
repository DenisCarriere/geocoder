#!/usr/bin/python
# coding: utf8
import geocoder

location = '8.8.8.8'


def test_maxmind():
    g = geocoder.maxmind(location)
    assert g.ok
