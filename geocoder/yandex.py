#!/usr/bin/python
# coding: utf8
from __future__ import absolute_import

import logging

from geocoder.base import OneResult, MultipleResultsQuery


class YandexResult(OneResult):

    def __init__(self, json_content):
        self._meta_data = json_content['metaDataProperty']['GeocoderMetaData']
        super(YandexResult, self).__init__(json_content)

    @property
    def lat(self):
        pos = self.raw.get('Point', {}).get('pos')
        if pos:
            return pos.split(' ')[1]

    @property
    def lng(self):
        pos = self.raw.get('Point', {}).get('pos')
        if pos:
            return pos.split(' ')[0]

    @property
    def bbox(self):
        envelope = self._meta_data.get('boundedBy', {}).get('Envelope', {})
        if envelope:
            east, north = envelope.get('upperCorner', '').split(' ')
            west, south = envelope.get('lowerCorner', '').split(' ')
            try:
                return self._get_bbox(float(south),
                                      float(west),
                                      float(north),
                                      float(east))
            except:
                pass

    @property
    def description(self):
        return self.raw.get('description')

    @property
    def address(self):
        return self._meta_data.get('text')

    @property
    def quality(self):
        return self._meta_data.get('kind')

    @property
    def accuracy(self):
        return self._meta_data.get('precision')

    @property
    def _country(self):
        return self._meta_data.get('AddressDetails', {}).get('Country', {})

    @property
    def country(self):
        return self._country.get('CountryName')

    @property
    def country_code(self):
        return self._country.get('CountryNameCode')

    @property
    def _administrativeArea(self):
        return self._country.get('AdministrativeArea', {})

    @property
    def state(self):
        return self._administrativeArea.get('AdministrativeAreaName')

    @property
    def _subAdministrativeArea(self):
        return self._administrativeArea.get('SubAdministrativeArea', {})

    @property
    def county(self):
        return self._subAdministrativeArea.get('SubAdministrativeAreaName')

    @property
    def _locality(self):
        return self._subAdministrativeArea.get('Locality', {})

    @property
    def city(self):
        return self._locality.get('LocalityName')

    @property
    def _thoroughfare(self):
        return self._locality.get('Thoroughfare', {})

    @property
    def street(self):
        return self._thoroughfare.get('ThoroughfareName')

    @property
    def _premise(self):
        return self._thoroughfare.get('Premise', {})

    @property
    def housenumber(self):
        return self._premise.get('PremiseNumber')


class YandexQuery(MultipleResultsQuery):
    """
    Yandex
    ======
    Yandex (Russian: Яндекс) is a Russian Internet company
    which operates the largest search engine in Russia with
    about 60% market share in that country.

    The Yandex home page has been rated as the most popular website in Russia.

    Params
    ------
    :param location: Your search location you want geocoded.
    :param lang: Chose the following language:
        > ru-RU — Russian (by default)
        > uk-UA — Ukrainian
        > be-BY — Belarusian
        > en-US — American English
        > en-BR — British English
        > tr-TR — Turkish (only for maps of Turkey)
    :param kind: Type of toponym (only for reverse geocoding):
        > house - house or building
        > street - street
        > metro - subway station
        > district - city district
        > locality - locality (city, town, village, etc.)

    References
    ----------
    API Reference: http://api.yandex.com/maps/doc/geocoder/desc/concepts/input_params.xml
    """
    provider = 'yandex'
    method = 'geocode'

    _URL = 'https://geocode-maps.yandex.ru/1.x/'
    _RESULT_CLASS = YandexResult
    _KEY_MANDATORY = False

    def _build_params(self, location, provider_key, **kwargs):
        return {
            'geocode': location,
            'lang': kwargs.get('lang', 'en-US'),
            'kind': kwargs.get('kind', ''),
            'format': 'json',
            'results': kwargs.get('maxRows', 1),
        }

    def _adapt_results(self, json_response):
        return [item['GeoObject'] for item
                in json_response['response']['GeoObjectCollection']['featureMember']]


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = YandexQuery('1552 Payette dr., Ottawa', maxRows=3)
    g.debug()
