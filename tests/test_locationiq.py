# coding: utf8

import geocoder

location = 'Ottawa, Ontario'
city = 'Ottawa'
country = 'Canada'
ottawa = (45.421106, -75.690308)


def test_locationiq():
    """ Expected result :
        https://locationiq.org/v1/search.php?q=Ottawa,Ontario&format=json&key=YOUR-API-KEY
    """
    g = geocoder.locationiq(location)
    assert g.ok
    assert g[0].lat == ottawa[0]
    assert g[0].lng == ottawa[1]


def test_locationiq_single_result():
    g = geocoder.locationiq(location, maxRows=1)
    assert g.ok
    assert len(g) == 1


def test_locationiq_multi_result():
    g = geocoder.locationiq(location, maxRows=5)
    assert g.ok
    assert len(g) > 1


def test_locationiq_reverse():
    """ Expected result :
        https://locationiq.org/v1/search?q=45.421106,-75.690308&format=json&key=YOUR-API-KEY
    """
    g = geocoder.locationiq(ottawa, method='reverse')
    assert g.ok
    assert g.city == city
    assert g.country == country
