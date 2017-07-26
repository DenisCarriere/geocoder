#!/usr/bin/python
# coding: utf8

import geocoder
import requests

try:
    import mock
except ImportError:
    from unittest import mock

address = 'Booth Street, Ottawa'


def test_session():
    with requests.Session() as session:
        g = geocoder.google(address, session=session)
        assert g.ok


def test_session_called():
    with mock.patch('requests.Session.get'):
        with requests.Session() as session:
            geocoder.google(address, session=session)
        session.get.assert_called_once()
