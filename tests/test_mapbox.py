#!/usr/bin/python
# coding: utf8

import geocoder

location = 'Ottawa, Ontario'
city = 'Ottawa'
ottawa = (45.4215296, -75.6971930)


def test_mapbox():
    g = geocoder.mapbox(location)
    assert g.ok


def test_mapbox_reverse():
    g = geocoder.mapbox(ottawa, method='reverse')
    assert g.ok


def test_multi_results():
    g = geocoder.mapbox(location)
    assert len(g) == 5

    expected_results = [
        'Ottawa, Ontario, Canada',
        'Ontario Court of Justice, 15 Victoria, Ottawa, Ontario K2G 3H2, Canada',
        'Ontario Secondary School Teachers Federation Dis trict 25, 9 Corvus Crt, Ottawa, Ontario K2E 7Z4, Canada',
        'Ontario Secondary School Teachers Federation District 25, 67 Jamie Ave, Ottawa, Ontario K2E 7Y6, Canada',
        'Ontario Carlton District School Board, 60 Tiverton Dr, Ottawa, Ontario K2E 6L8, Canada',
    ]
    assert [result.address for result in g] == expected_results

def main():
    test_multi_results()

if __name__ == '__main__':
    main()