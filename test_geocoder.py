import geocoder
import pytest
import unittest


location = 'Canada'
ip = '74.125.226.99'
repeat = 3
ottawa = (45.4215296, -75.6971930)
toronto = (43.653226, -79.3831843)

def test_entry_points():
    geocoder.ip
    geocoder.osm
    geocoder.bing
    geocoder.nokia
    geocoder.google
    geocoder.tomtom
    geocoder.reverse
    geocoder.geonames
    geocoder.distance
    geocoder.mapquest

def test_google():
    for i in xrange(repeat):
        g = geocoder.google(location)
        if g.ok:
            return True
    return False

def test_bing():
    for i in xrange(3):
        g = geocoder.bing(location)
        if g.ok:
            return True
    return False

def test_osm():
    for i in xrange(3):
        g = geocoder.osm(location)
        if g.ok:
            return True
    return False

def test_tomtom():
    for i in xrange(3):
        g = geocoder.tomtom(location)
        if g.ok:
            return True
    return False

def test_arcgis():
    for i in xrange(3):
        g = geocoder.arcgis(location)
        if g.ok:
            return True
    return False

def test_mapquest():
    for i in xrange(3):
        g = geocoder.mapquest(location)
        if g.ok:
            return True
    return False

def test_geonames():
    for i in xrange(3):
        g = geocoder.geonames(location)
        if g.ok:
            return True
    return False

def test_distance():
    d = geocoder.distance(ottawa, toronto)
    return d.ok

def test_reverse():
    g = geocoder.reverse(ottawa)
    return g.ok
