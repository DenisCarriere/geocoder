#!/usr/bin/python
# coding: utf8
import geocoder

location = 'Ottawa, Ontario'
city = 'Ottawa'
ottawa = (45.4215296, -75.6971930)


def test_osm():
    g = geocoder.osm(location)
    assert g.ok
    osm_count, fields_count = g.debug()[0]
    assert osm_count >= 3
    assert fields_count >= 21


def test_osm_reverse():
    g = geocoder.osm(ottawa, method='reverse')
    assert g.ok


def test_multi_results():
    g = geocoder.osm(location, maxRows='5')
    assert len(g) == 5

def test_detailed_query():
    g = geocoder.osm("",postalcode="45326", street="Ellernstraße", method="details")
    assert g.postal == "45326"
    assert "ellern" in g.street.lower()
    assert g.ok

