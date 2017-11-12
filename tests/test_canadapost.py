# coding: utf8

import geocoder
import requests_mock

location = "453 Booth Street, ON"


def test_canadapost():
    url_1 = 'https://ws1.postescanada-canadapost.ca/AddressComplete/Interactive/Find/v2.10/json3ex.ws?Key=fake&LastId=&Country=ca&SearchFor=Everything&SearchTerm=453+Booth+Street%2C+ON&LanguagePreference=en&%24cache=true'
    url_2 = 'https://ws1.postescanada-canadapost.ca/AddressComplete/Interactive/Find/v2.10/json3ex.ws?Key=fake&LastId=CA%7CCP%7CENG%7CON-OTTAWA-BOOTH_ST-453&Country=ca&SearchFor=Everything&SearchTerm=453+Booth+Street%2C+ON&LanguagePreference=en&%24cache=true'
    url_3 = 'https://ws1.postescanada-canadapost.ca/AddressComplete/Interactive/RetrieveFormatted/v2.10/json3ex.ws?Key=fake&Id=CA%7CCP%7CB%7C80225509&Source=&MaxResults=3&cache=true'
    data_file_1 = 'tests/results/canadapost_find_1.json'
    data_file_2 = 'tests/results/canadapost_find_2.json'
    data_file_3 = 'tests/results/canadapost_retrieve.json'
    with requests_mock.Mocker() as mocker, open(data_file_1, 'r') as input_1, open(data_file_2, 'r') as input_2, open(data_file_3, 'r') as input_3:
        mocker.get(url_1, text=input_1.read())
        mocker.get(url_2, text=input_2.read())
        mocker.get(url_3, text=input_3.read())
        g = geocoder.canadapost(location, key='fake', maxRows=3)
        assert g.ok
        osm_count, fields_count = g.debug()[0]
        assert osm_count >= 6
        assert fields_count >= 15
