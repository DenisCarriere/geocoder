# coding: utf8

import geocoder

location = 'Ottawa'
coordinates = {'lat': 41.005407, 'lng': 28.978349}


def test_yandex():
    g = geocoder.yandex(location)
    assert g.ok


def test_yandex_reverse():
    g = geocoder.yandex(coordinates, method='reverse')
    assert g.ok


def test_multi_results():
    g = geocoder.yandex(location, maxRows=3)
    assert len(g) == 3
