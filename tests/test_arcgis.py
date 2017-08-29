#!/usr/bin/python
# coding: utf8
import logging
import geocoder

location = 'Ottawa, Ontario'
ottawa = (45.4215296, -75.6971930)


def test_arcgis():
    g = geocoder.arcgis(location)
    assert g.ok


def test_arcgis_reverse():
    g = geocoder.arcgis(ottawa, method='reverse')
    assert g.ok


def test_multi_results():
    g = geocoder.arcgis(location, maxRows='5')
    assert len(g) == 5

    expected_results = [
        'Ottawa, Ontario',
        'Ottawa, Ontario',
        'Ontario, Oklahoma'
    ]
    assert [result.address for result in g][:3] == expected_results


def main():
    logging.basicConfig(level=logging.INFO)
    test_multi_results()


if __name__ == '__main__':
    main()
