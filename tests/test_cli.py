#!/usr/bin/env python
# coding: utf8
"""
Unit tests for cli functionality
"""

import subprocess


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


def test_cli_google():
    assert not subprocess.call(['geocode', location, '--provider', 'google'])


def test_cli_bing():
    assert not subprocess.call(['geocode', location, '--provider', 'bing'])


def test_cli_osm():
    assert not subprocess.call(['geocode', location, '--provider', 'osm'])


def test_cli_tamu():
    assert not subprocess.call([
        'geocode', us_address,
        '--city', us_city, '--state', us_state, '--zipcode', us_zipcode,
        '--provider', 'tamu'
    ])

if __name__ == '__main__':
    test_cli_tamu()
