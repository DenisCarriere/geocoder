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
