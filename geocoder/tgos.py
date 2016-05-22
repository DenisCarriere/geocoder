#!/usr/bin/python
# coding: utf8

import re
from geocoder.base import Base


class Tgos(Base):
    '''
    TGOS Geocoding Service

    TGOS Map is official map service of Taiwan.

    API Reference
    -------------
    http://api.tgos.nat.gov.tw/TGOS_MAP_API/Web/Default.aspx
    '''
    provider = 'tgos'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self._define_language(kwargs)
        self.url = 'http://gis.tgos.nat.gov.tw/TGLocator/TGLocator.ashx'
        self.params = {
            'format': 'json',
            'input': location,
            'center': kwargs.get('method', 'center'),
            'srs': 'EPSG:4326',
            'ignoreGeometry': False,
            'pnum': 5
        }
        self._initialize(**kwargs)

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
    def quality(self):
        return self.type

    @property
    def lat(self):
        return self.parse['geometry'].get('y')

    @property
    def lng(self):
        return self.parse['geometry'].get('x')

    @property
    def address(self):
        return self.parse.get('FULL_ADDR')

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
        return self.parse.get('ALLEY')

    @property
    def lane(self):
        return self.parse.get('LANE')

    @property
    def neighborhood(self):
        return self.parse.get('NEIGHBORHOOD')

    @property
    def number(self):
        return self.parse.get('NUMBER')

    @property
    def road(self):
        return self.parse.get('ROAD')

    @property
    def section(self):
        section = self.parse.get('SECTION')
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
        return self.parse.get('sub_alley')

    @property
    def tong(self):
        return self.parse.get('TONG')

    @property
    def village(self):
        return self.parse.get('VILLAGE')

    @property
    def county(self):
        return self.parse.get('county')

    @property
    def name(self):
        return self.parse.get('name')

    @property
    def town(self):
        return self.parse.get('town')

    @property
    def type(self):
        return self.parse.get('type')


if __name__ == '__main__':
    g = Tgos('台北市內湖區內湖路一段735號', language='en')
    g.debug()
