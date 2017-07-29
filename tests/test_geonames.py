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
    assert g.country_code == 'CA'
    assert g.state == 'Ontario'
    assert g.state_code == '08'
    assert g.description == 'capital of a political entity'
    assert g.class_description == 'city, village,...'
    assert g.feature_class == 'P'
    assert g.code == 'PPLC'
    assert g.geonames_id == 6094817


def test_children():
    """ Expected result :
        http://api.geonames.org/childrenJSON?formatted=true&geonameId=6094817&username=demo
    """
    g = geocoder.geonames(6094817, method='children')
    assert g.ok
    assert len(g.parse['geonames']) == 2
    expected_names = set(("Birch Manor", "Templeton-Est"))
    results = set([res['toponymName'] for res in g.parse['geonames']])
    assert expected_names == results
