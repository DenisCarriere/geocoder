# coding: utf8

import geocoder

address = 'The Happy Goat, Ottawa'
location = 'Ottawa, Ontario'
city = 'Ottawa'
ottawa = (45.4215296, -75.6971930)

def test_geonames():
    """ Expected result :
        http://api.geonames.org/searchJSON?q=Ottawa%2C+Ontario&fuzzy=0.8&username=demo&maxRows=1
    """
    g = geocoder.geonames(location)
    assert g.ok
    assert g.country == 'Canada'
    assert g.state == 'Ontario'
    assert g.description == 'capital of a political entity'
    assert g.code == 'PPLC'
    assert g.geonames_id == 6094817
