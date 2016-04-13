#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base


class Yandex(Base):
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
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'http://geocode-maps.yandex.ru/1.x/'
        self.location = location
        self.params = {
            'geocode': location,
            'lang': kwargs.get('lang', 'en-US'),
            'kind': kwargs.get('kind', ''),
            'format': 'json',
            'results': 1,
        }
        self._initialize(**kwargs)

    def _exceptions(self):
        # Build intial Tree with results
        feature = self.parse['GeoObjectCollection']['featureMember']
        for item in feature:
            self._build_tree(item['GeoObject'])

    @property
    def address(self):
        return self.parse['GeocoderMetaData'].get('text')

    @property
    def lat(self):
        pos = self.parse['Point'].get('pos')
        if pos:
            return pos.split(' ')[1]

    @property
    def lng(self):
        pos = self.parse['Point'].get('pos')
        if pos:
            return pos.split(' ')[0]

    @property
    def bbox(self):
        if self.parse['Envelope']:
            east, north = self.parse['Envelope'].get('upperCorner').split(' ')
            west, south = self.parse['Envelope'].get('lowerCorner').split(' ')
            try:
                return self._get_bbox(float(south),
                                      float(west),
                                      float(north),
                                      float(east))
            except:
                pass

    @property
    def quality(self):
        return self.parse['GeocoderMetaData'].get('kind')

    @property
    def accuracy(self):
        return self.parse['GeocoderMetaData'].get('precision')

    @property
    def housenumber(self):
        return self.parse['Premise'].get('PremiseNumber')

    @property
    def street(self):
        return self.parse['Thoroughfare'].get('ThoroughfareName')

    @property
    def city(self):
        return self.parse['Locality'].get('LocalityName')

    @property
    def county(self):
        return self.parse['SubAdministrativeArea'].get('SubAdministrative'
                                                       'AreaName')

    @property
    def state(self):
        return self.parse['AdministrativeArea'].get('AdministrativeAreaName')

    @property
    def country(self):
        return self.parse['Country'].get('CountryName')

    @property
    def country_code(self):
        return self.parse['Country'].get('CountryNameCode')

    @property
    def SubAdministrativeArea(self):
        return self.parse['SubAdministrativeArea'].get('SubAdministrativeAreaName')

    @property
    def Premise(self):
        return self.parse.get('Premise')

    @property
    def AdministrativeArea(self):
        return self.parse['AdministrativeArea'].get('AdministrativeAreaName')

    @property
    def Locality(self):
        return self.parse['Locality']

    @property
    def Thoroughfare(self):
        return self.parse['Thoroughfare'].get('ThoroughfareName')

    @property
    def description(self):
        return self.parse['description']


if __name__ == '__main__':
    g = Yandex('1552 Payette dr., Ottawa')
    g.debug()
