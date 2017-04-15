#!/usr/bin/python
# coding: utf8

import geocoder


def test_entry_points():
    geocoder.ip
    geocoder.osm
    geocoder.w3w
    geocoder.bing
    geocoder.here
    geocoder.tgos
    geocoder.baidu
    geocoder.yahoo
    geocoder.mapbox
    geocoder.google
    geocoder.yandex
    geocoder.tomtom
    geocoder.arcgis
    geocoder.ipinfo
    geocoder.mapzen
    geocoder.geonames
    geocoder.mapquest
    geocoder.timezone
    geocoder.maxmind
    geocoder.elevation
    geocoder.freegeoip
    geocoder.geolytica
    geocoder.timezone
    geocoder.opencage
    geocoder.places
    geocoder.canadapost
    geocoder.tamu
    geocoder.geocodefarm
    geocoder.uscensus


def test_location():
    g = geocoder.location('45.4215296, -75.6971931')
    assert g.ok
    g = geocoder.location({'lat': 45.4215296, 'lng': -75.6971931})
    assert g.ok
    g = geocoder.location([45.4215296, -75.6971931])
    assert g.ok
