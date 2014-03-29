import geocoder
import pytest
import unittest


location = 'Canada'
ip = '74.125.226.99'
repeat = 3
ottawa = (45.4215296, -75.6971930)
toronto = (43.653226, -79.3831843)
bing_key = 'AtnSnX1rEHr3yTUGC3EHkD6Qi3NNB-PABa_F9F8zvLxxvt8A7aYdiG3bGM_PorOq'
tomtom_key = '95kjrqtpzv39ujcxfyr57wz3'
app_id = '6QqTvc3kUWsMjYi7iGRb'
app_code = 'q7R__C774SunvWJDEiWbcA'
username = 'addxy'

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
    for i in xrange(repeat):
        g = geocoder.bing(location, key=bing_key)
        if g.ok:
            return True
    return False

def test_nokia():
    for i in xrange(repeat):
        g = geocoder.nokia(location, app_code=app_code, app_id=app_id)
        if g.ok:
            return True
    return False

def test_osm():
    for i in xrange(repeat):
        g = geocoder.osm(location)
        if g.ok:
            return True
    return False

def test_tomtom():
    for i in xrange(repeat):
        g = geocoder.tomtom(location, key=tomtom_key)
        if g.ok:
            return True
    return False

def test_arcgis():
    for i in xrange(repeat):
        g = geocoder.arcgis(location)
        if g.ok:
            return True
    return False

def test_mapquest():
    for i in xrange(repeat):
        g = geocoder.mapquest(location)
        if g.ok:
            return True
    return False

def test_geonames():
    for i in xrange(repeat):
        g = geocoder.geonames(location, username=username)
        if g.ok:
            return True
    return False

def test_distance():
    for i in xrange(repeat):
        d = geocoder.distance(ottawa, toronto)
        if d.ok:
            return True
    return False

def test_reverse():
    for i in xrange(repeat):
        g = geocoder.reverse(ottawa)
        if g.ok:
            return True
    return False

def test_ip():
    for i in xrange(repeat):
        g = geocoder.ip(ip)
        if g.ok:
            return True
    return False