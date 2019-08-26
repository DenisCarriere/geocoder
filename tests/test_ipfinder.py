#!/usr/bin/python
# coding: utf8

import geocoder

location = '1.0.0.0'


def test_ipfinder():
    g = geocoder.ipfinder(location)

    assert g.status_code == 200
    assert g.url         == "https://api.ipfinder.io/v1/1.0.0.0?token=free&format=json"
    assert g.status      == "ok"
    assert g.headers.get('user-agent')      == "geocoder Python-client"

