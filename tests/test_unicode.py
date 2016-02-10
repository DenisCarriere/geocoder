# -*- encoding: utf-8 -*-

import geocoder


def test_unicode():
    g = geocoder.google('東京', key='')
    assert g


def test_repr_unicode():
    g = geocoder.osm('Tokyo, Japan')
    assert g


def test_bing_unicode():
    g = geocoder.bing('1 rue bergere, paris')
    assert g

if __name__ == '__main__':
    test_repr_unicode()
    test_unicode()
