#!/usr/bin/python
# coding: utf8

import geocoder
import pytest
import unittest

address = '453 Booth Street, Ottawa'
location = 'Ottawa, ON, Canada'
ip = '74.125.226.99'
repeat = 3
ottawa = (45.4215296, -75.6971930)
toronto = (43.653226, -79.3831843)

g = geocoder.canadapost(address)
print g

def test_entry_points():
    geocoder.ip
    geocoder.get
    geocoder.osm
    geocoder.bing
    geocoder.nokia
    geocoder.google
    geocoder.arcgis
    geocoder.tomtom
    geocoder.reverse
    geocoder.geonames
    geocoder.mapquest
    geocoder.canadapost
    geocoder.population

def test_canadapost():
    g = geocoder.google(address)
    assert g.ok

def test_google():
    g = geocoder.google(location)
    assert g.ok

def test_bing():
    g = geocoder.bing(location)
    assert g.ok

def test_nokia():
    g = geocoder.nokia(location)
    assert g.ok

def test_osm():
    g = geocoder.osm(location)
    assert g.ok

def test_tomtom():
    g = geocoder.tomtom(location)
    assert g.ok

def test_mapquest():
    g = geocoder.mapquest(location)
    assert g.ok

def test_geonames():
    g = geocoder.geonames(location)
    assert g.ok

def test_reverse():
    g = geocoder.reverse(ottawa)
    assert g.ok

def test_ip():
    g = geocoder.ip(ip)
    assert g.ok

def test_get():
    g = geocoder.get(location)
    assert g.ok

"""
Not Currently working
ArcGIS server are down

def test_arcgis():
    g = geocoder.arcgis(location)
    assert g.ok
"""