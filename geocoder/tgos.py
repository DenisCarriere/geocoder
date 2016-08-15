#!/usr/bin/python
# coding: utf8

import re
import math
import requests
from geocoder.base import Base
from geocoder.keys import tgos_key


class Tgos(Base):
    '''
    TGOS Geocoding Service

    TGOS Map is official map service of Taiwan.
    '''
    PLATFORM_URL = 'http://map.tgos.nat.gov.tw/TGOSCLOUD/Web/Map/TGOSViewer_Map.aspx'

    provider = 'tgos'
    method = 'geocode'
    section_chars = u'.一二三四五六七八九'

    # state variables
    pagekey = False
    cookies = {}

    def __init__(self, location, **kwargs):
        self._define_language(kwargs)

        if Tgos.pagekey == False:
            self._get_state()

        self.url = 'http://map.tgos.nat.gov.tw/TGOSCloud/Generic/Project/GHTGOSViewer_Map.ashx'
        self.headers = {
            'Origin': 'http://map.tgos.nat.gov.tw',
            'Referer': Tgos.PLATFORM_URL,
            'X-Requested-With': 'XMLHttpRequest'
        }
        self.params = {
            'pagekey': Tgos.pagekey
        }
        Tgos.data = {
            'method': 'querymoiaddr',
            'address': location,
            'sid': self.cookies['ASP.NET_SessionId'],
            'useoddeven': False
        }

        self._initialize(**kwargs)

    @staticmethod
    def _get_state():
        r = requests.post(Tgos.PLATFORM_URL)
        if r.status_code == 200:
            m = re.search('window\.sircMessage\.sircPAGEKEY\s?=\s?\'([\w\+%]+)\';', r.text)
            if m != None:
                Tgos.pagekey = m.group(1)
                for c in r.cookies:
                    Tgos.cookies[c.name] = c.value

    @staticmethod
    def rate_limited_get(url, **kwargs):
        kwargs['cookies'] = Tgos.cookies
        kwargs['data'] = Tgos.data
        return requests.post(url, **kwargs)

    def _catch_errors(self):
        status = self.parse['status']
        if not status == 'OK':
            error = self.parse['error_message']
            if status == 'REQUEST_DENIED':
                self.error = self.parse['error_message']
                self.status_code = 401
            else:
                self.error = 'Unknown'
                self.status_code = 500

    def _define_language(self, kwargs):
        # Custom language output
        language = kwargs.get('language', 'taiwan').lower()
        if language in ['english', 'en', 'eng']:
            self.language = 'en'
        elif language in ['chinese', 'zh']:
            self.language = 'zh-tw'
        else:
            self.language = 'zh-tw'

    def _exceptions(self):
        # Build intial Tree with results
        result = self.parse['results']
        if result:
            self._build_tree(result[0])

    @property
    def ok(self):
        t = len(self.parse['AddressList'])
        return (t > 0)

    @property
    def lat(self):
        if self.ok:
            # TWD97 -> WGS84
            ty = self.parse['AddressList'][0]['Y']
            y  = ty * 0.00000899823754
            return y
        return False

    @property
    def lng(self):
        if self.ok:
            # TWD97 -> WGS84
            tx = self.parse['AddressList'][0]['X']
            x = 121 + (tx - 250000) * 0.000008983152841195214 / math.cos(math.radians(self.lat))
            return x
        return False

    @property
    def address(self):
        if self.ok:
            return self.parse['AddressList'][0]['FULL_ADDR']
        return ''

    @property
    def country(self):
        return {'en': u'Taiwan', 'zh-tw': u'中華民國'}[self.language]

    @property
    def city(self):
        if self.ok:
            return self.parse['AddressList'][0]['COUNTY']

    @property
    def housenumber(self):
        if self.ok:
            m = re.match(r'(\d+).+', self.parse['AddressList'][0]['NUMBER'])
            if m is not None:
                return int(m.group(1))
        return False

    @property
    def street(self):
        if self.ok:
            s = self.parse['AddressList'][0]['SECTION']
            if s != '':
                s = Tgos.section_chars[int(s)]
                return u'{road}{section}{segment}'.format(
                    road = self.parse['AddressList'][0]['ROAD'],
                    section = s,
                    segment = {u'zh-tw': u'段', u'en': u'Segment'}[self.language]
                )
            return self.parse['AddressList'][0]['ROAD']

if __name__ == '__main__':
    g = Tgos('台北市內湖區內湖路一段735號', language='en')
    g.debug()
