#!/usr/bin/python
# coding: utf8

import re
import requests
import logging

from geocoder.base import OneResult, MultipleResultsQuery
from geocoder.keys import tgos_key


class TgosResult(OneResult):

    def __init__(self, json_content, language):
        super(TgosResult, self).__init__(json_content)
        self.language = language

    @property
    def quality(self):
        return self.type

    @property
    def lat(self):
        return self.raw('geometry', {}).get('y')

    @property
    def lng(self):
        return self.raw('geometry', {}).get('x')

    @property
    def address(self):
        return self.raw.get('FULL_ADDR')

    @property
    def housenumber(self):
        number = self.number
        if number:
            match = re.match(r'\d+', number)
            if match:
                return int(match.group())
        return number

    @property
    def street(self):
        if bool(self.road and self.section):
            return u'{road}{section}{segment}'.format(
                road=self.road,
                section=self.section,
                segment={'zh-tw': u'段', 'en': 'Segement'}[self.language])
        return self.road

    @property
    def state(self):
        return self.county

    @property
    def city(self):
        return self.town

    @property
    def country(self):
        return {'en': u'Taiwan', 'zh-tw': u'中華民國'}[self.language]

    # TGOS specific attributes
    # ========================
    @property
    def alley(self):
        return self.raw.get('ALLEY')

    @property
    def lane(self):
        return self.raw.get('LANE')

    @property
    def neighborhood(self):
        return self.raw.get('NEIGHBORHOOD')

    @property
    def number(self):
        return self.raw.get('NUMBER')

    @property
    def road(self):
        return self.raw.get('ROAD')

    @property
    def section(self):
        section = self.raw.get('SECTION')
        if section:
            if self.language == 'zh-tw':
                return {
                    0: u'零',
                    1: u'一',
                    2: u'二',
                    3: u'三',
                    4: u'四',
                    5: u'五',
                    6: u'六',
                    7: u'七',
                    8: u'八',
                    9: u'九'
                }[int(section)]
            return int(section)

    @property
    def sub_alley(self):
        return self.raw.get('sub_alley')

    @property
    def tong(self):
        return self.raw.get('TONG')

    @property
    def village(self):
        return self.raw.get('VILLAGE')

    @property
    def county(self):
        return self.raw.get('county')

    @property
    def name(self):
        return self.raw.get('name')

    @property
    def town(self):
        return self.raw.get('town')

    @property
    def type(self):
        return self.raw.get('type')


class TgosQuery(MultipleResultsQuery):
    '''
    TGOS Geocoding Service

    TGOS Map is official map service of Taiwan.

    API Reference
    -------------
    http://api.tgos.nat.gov.tw/TGOS_MAP_API/Web/Default.aspx
    '''
    provider = 'tgos'
    method = 'geocode'

    _URL = 'http://gis.tgos.nat.gov.tw/TGLocator/TGLocator.ashx'
    _RESULT_CLASS = TgosResult
    _KEY = tgos_key

    @classmethod
    def _get_api_key(cls, key=None):
        # Retrieves API Key from method argument first, then from Environment variables
        key = key or cls._KEY

        if not key:
            key = cls._get_tgos_key()

        # raise exception if not valid key found
        if not key and cls._KEY_MANDATORY:
            raise ValueError('Provide API Key')

        return key

    @classmethod
    def _get_tgos_key(cls):
        url = 'http://api.tgos.nat.gov.tw/TGOS_API/tgos'
        r = requests.get(url, headers={'Referer': url})

        # TGOS Hash pattern used for TGOS API key
        pattern = re.compile(r'TGOS.tgHash="([a-zA-Z\d/\-_+=]*)"')
        match = pattern.search(r.text)
        if match:
            return match.group(1)
        else:
            raise ValueError('Cannot find TGOS.tgHash')

    def _build_params(self, location, provider_key, **kwargs):
        return {
            'format': 'json',
            'input': location,
            'center': kwargs.get('method', 'center'),
            'srs': 'EPSG:4326',
            'ignoreGeometry': False,
            'keystr': provider_key,
            'pnum': kwargs.get('maxRows', 5)
        }

    def _before_initialize(self, location, **kwargs):
        # Custom language output
        language = kwargs.get('language', 'taiwan').lower()
        if language in ['english', 'en', 'eng']:
            self.language = 'en'
        elif language in ['chinese', 'zh']:
            self.language = 'zh-tw'
        else:
            self.language = 'zh-tw'

    def _catch_errors(self, json_response):
        status = json_response['status']
        if status != 'OK':
            if status == 'REQUEST_DENIED':
                self.error = json_response['error_message']
                self.status_code = 401
            else:
                self.error = 'Unknown'
                self.status_code = 500

        return self.error

    def _adapt_results(self, json_response):
        return json_response['results']

    def _parse_results(self, json_response):
        # overriding method to pass language to every result
        for json_dict in self._adapt_results(json_response):
            self.add(self.one_result(json_dict, self.language))

        # set default result to use for delegation
        self.current_result = len(self) > 0 and self[0]


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = TgosQuery('台北市內湖區內湖路一段735號', language='en')
    g.debug()
