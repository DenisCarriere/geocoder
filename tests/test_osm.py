#!/usr/bin/python
# coding: utf8
import logging
import geocoder

location = 'Ottawa, Ontario'
city = 'Ottawa'
ottawa = (45.4215296, -75.6971930)


def test_osm():
    g = geocoder.osm(location)
    assert g.ok


def test_osm_reverse():
    g = geocoder.osm(ottawa, method='reverse')
    assert g.ok


def test_multi_results():
    g = geocoder.osm(location, maxRows='5')
    assert len(g) == 5

    expected_results = [
        'Ottawa, Ontario, Canada', 
        'Ontario, Ottawa County, Oklahoma, United States of America', 
        'Ottawa Fire Station 51, 900, Montréal Road, Viscount Alexander Park, Rideau-Rockcliffe, Ottawa, Ontario, K1L 0S8, Canada']
    assert [result.address for result in g][:3] == expected_results


def main():
    logging.basicConfig(level=logging.INFO)
    test_multi_results()

if __name__ == '__main__':
    main()