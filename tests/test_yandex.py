# coding: utf8
import requests_mock

import geocoder

location = 'Ottawa'
coordinates = {'lat': 41.005407, 'lng': 28.978349}
location_url = (f'https://geocode-maps.yandex.ru/1.x/?apikey=mock&geocode='
                f'{location}')
coordinates_url = (f'https://geocode-maps.yandex.ru/1.x/?apikey=mock&geocode='
                   f'{coordinates["lng"]}, {coordinates["lat"]}')


def test_yandex():
    data_file = 'tests/results/yandex.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(location_url, text=input.read())
        g = geocoder.yandex(location, key='mock')
        assert g.ok


def test_yandex_reverse():
    data_file = 'tests/results/yandex_reverse.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(coordinates_url, text=input.read())
        g = geocoder.yandex(coordinates, method='reverse', key='mock')
        assert g.ok


def test_multi_results():
    data_file = 'tests/results/yandex_batch.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(location_url, text=input.read())
        g = geocoder.yandex(location, maxRows=3, key='mock')
        assert len(g) == 3
