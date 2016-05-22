#!/usr/bin/python
# coding: utf8

import geocoder


address = '453 Booth Street, Ottawa'
location = 'Ottawa, Ontario'
words = 'embedded.fizzled.trial'
city = 'Ottawa'
ip = '74.125.226.99'
china = '中国'
taiwan = '台北市內湖區內湖路一段735號'
repeat = 3
ottawa = (45.4215296, -75.6971930)
toronto = (43.653226, -79.3831843)
istanbul = {'lat': 41.005407, 'lng': 28.978349}
us_address = '595 Market St'
us_city = 'San Francisco'
us_state = 'CA'
us_zipcode = '94105'


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
    geocoder.elevation
    geocoder.canadapost
    geocoder.tamu
    geocoder.geocodefarm


def test_location():
    g = geocoder.location('45.4215296, -75.6971931')
    assert g.ok
    g = geocoder.location({'lat': 45.4215296, 'lng': -75.6971931})
    assert g.ok
    g = geocoder.location([45.4215296, -75.6971931])
    assert g.ok


def test_ipinfo():
    g = geocoder.ipinfo(ip)
    assert g.ok

"""
# FREEGEOIP REMOVED
# =================
# Server not stable for testing

def test_freegeoip():
    g = geocoder.freegeoip(ip)
    assert g.ok
"""


def test_mapbox():
    g = geocoder.mapbox(location)
    assert g.ok


def test_mapbox_reverse():
    g = geocoder.mapbox(ottawa, method='reverse')
    assert g.ok


def test_mapzen():
    g = geocoder.mapzen(location)
    assert g.ok


def test_mapzen_reverse():
    g = geocoder.mapbox(ottawa, method='reverse')
    assert g.ok


def test_yandex():
    g = geocoder.yandex(location)
    assert g.ok


def test_yandex_reverse():
    g = geocoder.yandex(istanbul, method='reverse')
    assert g.ok


def test_w3w():
    g = geocoder.w3w(words)
    assert g.ok


def test_w3w_reverse():
    g = geocoder.w3w(ottawa, method='reverse')
    assert g.ok


def test_maxmind():
    g = geocoder.maxmind(ip)
    assert g.ok


def test_baidu():
    g = geocoder.baidu(china)
    assert g.ok


def test_google():
    g = geocoder.google(location, client=None)
    assert g.ok
    assert str(g.city) == city


def test_google_for_work():
    g = geocoder.google(location)
    assert g.ok
    assert str(g.city) == city


def test_google_reverse():
    g = geocoder.google(ottawa, method='reverse')
    assert g.ok


def test_google_timezone():
    g = geocoder.google(ottawa, method='timezone')
    assert g.ok


def test_google_elevation():
    g = geocoder.google(ottawa, method='elevation')
    assert g.ok

"""
Bing REMOVED
==============
- Currently works
- Connection isn't very good for testing purpose

def test_bing():
    g = geocoder.bing(location)
    assert g.ok
    assert g.city == city


def test_bing_reverse():
    g = geocoder.bing(ottawa, method='reverse')
    assert g.ok
"""


def test_opencage():
    g = geocoder.opencage(location)
    assert g.ok


def test_opencage_reverse():
    g = geocoder.opencage(ottawa, method='reverse')
    assert g.ok


def test_yahoo():
    pass
    # g = geocoder.yahoo(location)
    # assert g.ok
    # assert str(g.city) == city


def test_arcgis():
    g = geocoder.arcgis(location)
    assert g.ok


def test_geolytica():
    g = geocoder.geolytica(address)
    assert g.ok


"""
Issues with API key

def test_canadapost():
    g = geocoder.canadapost(address)
    assert g.ok
"""

"""
Permission Error, no valid API key

def test_here():
    g = geocoder.here(location)
    assert g.ok
    assert g.city == city


def test_here_reverse():
    g = geocoder.here(ottawa, method='reverse')
    assert g.ok
"""


def test_osm():
    g = geocoder.osm(location)
    assert g.ok
    assert str(g.city) == city


def test_tomtom():
    g = geocoder.tomtom(location)
    assert g.ok
    assert str(g.city) == city


def test_mapquest():
    g = geocoder.mapquest(location)
    assert g.ok
    assert str(g.city) == city


def test_mapquest_reverse():
    g = geocoder.mapquest(ottawa, method='reverse')
    assert g.ok


def test_geonames():
    g = geocoder.geonames(city)
    assert g.ok


def test_tamu():
    g = geocoder.tamu(
        us_address,
        city=us_city,
        state=us_state,
        zipcode=us_zipcode)
    assert g.ok


def test_geocodefarm():
    g = geocoder.geocodefarm(location)
    assert g.ok
    assert str(g.city) == city


def test_geocodefarm_reverse():
    g = geocoder.geocodefarm(ottawa, method='reverse')
    assert g.ok


def test_tgos():
    g = geocoder.tgos(taiwan)
    assert g.ok
    g = geocoder.tgos(taiwan, language='en')
    assert g.ok


if __name__ == '__main__':
    test_entry_points()
