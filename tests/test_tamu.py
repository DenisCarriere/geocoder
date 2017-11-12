#!/usr/bin/python
# coding: utf8

import geocoder

location = '595 Market Street'


def test_tamu():
    g = geocoder.tamu(
        location,
        city='San Francisco',
        state='CA',
        zipcode='94105')
    assert g.ok
    osm_count, fields_count = g.debug()[0]
    assert osm_count >= 5
    assert fields_count >= 28
