#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base
from geocoder.yandex import Yandex
from geocoder.location import Location


class YandexReverse(Yandex, Base):
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

    def __init__(self, location, **kwargs):
        self.url = 'https://geocode-maps.yandex.ru/1.x/'
        location = location
        x, y = Location(location).xy
        self.location = u'{}, {}'.format(x, y)
        self.params = {
            'geocode': self.location,
            'lang': kwargs.get('lang', 'en-US'),
            'kind': kwargs.get('kind', ''),
            'format': 'json',
            'results': 1,
        }
        self._initialize(**kwargs)

    @property
    def ok(self):
        return bool(self.address)


if __name__ == '__main__':
    g = YandexReverse({'lat': 41.005407, 'lng': 28.978349})
    g.debug()
