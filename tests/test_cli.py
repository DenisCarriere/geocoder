#!/usr/bin/env python
# coding: utf8

import subprocess


location = 'Ottawa, Ontario'


def test_cli_google():
    assert not subprocess.call(['geocode', location, '--provider', 'google'])


def test_cli_osm():
    assert not subprocess.call(['geocode', location, '--provider', 'osm'])
