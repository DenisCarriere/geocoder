#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import

import logging

from geocoder.yandex import YandexResult, YandexQuery
from geocoder.location import Location


class YandexReverseResult(YandexResult):

    @property
    def ok(self):
        return bool(self.address)


class YandexReverse(YandexQuery):
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
    API Reference: http://api.yandex.com/maps/doc/geocoder/
                   desc/concepts/input_params.xml
    """
    provider = 'yandex'
    method = 'reverse'

    _RESULT_CLASS = YandexReverseResult

    def _build_params(self, location, provider_key, **kwargs):
        x, y = Location(location).xy
        self.location = u'{}, {}'.format(x, y)
        return {
            'geocode': self.location,
            'lang': kwargs.get('lang', 'en-US'),
            'kind': kwargs.get('kind', ''),
            'format': 'json',
            'results': kwargs.get('maxRows', 1),
        }


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = YandexReverse({'lat': 41.005407, 'lng': 28.978349})
    g.debug()
