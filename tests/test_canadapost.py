# coding: utf8

import geocoder

location = "453 Booth Street, ON"


def test_canadapost():
    g = geocoder.canadapost(location, maxRows=3)
    assert g.ok
