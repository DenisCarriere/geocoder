#!../../bin/python
# coding: utf8

import pyproj
import re
import requests

from bs4 import BeautifulSoup
from geocoder.base import Base


class Tgos(Base):
    '''
    TGOS Geocoding Service

    TGOS Map is official map service of Taiwan. It use EPSG:3826 coordinate system.
    Beause of different coordinate system, this project need "pyproj" to transform the coordinate.
    It's HTTP request need session state, so "beautifulsoup4" is needed to extract "pagekey" field.

    API Reference
    -------------
    http://api.tgos.nat.gov.tw/TGOS_MAP_API/Web/Default.aspx
    '''
    provider = 'tgos'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'http://map.tgos.nat.gov.tw/TGOSCloud/Generic/Project/GHTGOSViewer_Map.ashx'
        self.params = {
            'method': kwargs.get('method', 'queryaddr'),
            'useoddeven': kwargs.get('useoddeven', False),
            'address': location,
            'sid': kwargs.get('sid', 'Unknown')
        }
        self._initialize(**kwargs)

    def _get_tgos_entry(self):
        if not hasattr(self, 'tgos_entry'):
            if 'AddressList' in self.parse and len(self.parse['AddressList']) > 0:
                entry = self.parse['AddressList'][0]
                epsg3826 = pyproj.Proj(init='EPSG:3826')
                coord = epsg3826(entry['X'], entry['Y'], inverse=True)
                entry['lat'] = coord[1]
                entry['lng'] = coord[0]
                self.tgos_entry = entry
            else:
                return None

        return self.tgos_entry

    @property
    def lat(self):
        entry = self._get_tgos_entry()
        if entry is not None:
            return entry['lat']
        return 0

    @property
    def lng(self):
        entry = self._get_tgos_entry()
        if entry is not None:
            return entry['lng']
        return 0

    @property
    def address(self):
        entry = self._get_tgos_entry()
        if entry is not None:
            return entry['FULL_ADDR']
        return ''

    @property
    def housenumber(self):
        entry = self._get_tgos_entry()
        if entry is not None:
            m = re.match(u'(\d+)號', entry['NUMBER'])
            if m is not None:
                num = int(m.group(1))
                return num
        return 0

    @property
    def street(self):
        entry = self._get_tgos_entry()
        if entry is not None:
            numch = u'零一二三四五六七八九'
            if entry['SECTION'] != '':
                street = u'%s%s段' % (entry['ROAD'], numch[int(entry['SECTION'])])
            else:
                street = entry['ROAD']
            return street
        return ''

    @property
    def city(self):
        entry = self._get_tgos_entry()
        if entry is not None:
            return entry['COUNTY']
        return 0

    @property
    def country(self):
        return u'中華民國'

    @staticmethod
    def rate_limited_get(url, **kwargs):
        pagekey = 'Unknown'
        cookies = {'ASP.NET_SessionId': 'Unknown'}

        # Get a session
        # *   range: <script id='sircMessage1'>...</script>
        # * pattern: window.sircMessage.sircPAGEKEY = '...';
        r = requests.post('http://map.tgos.nat.gov.tw/TGOSCLOUD/Web/Map/TGOSViewer_Map.aspx')
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            node = soup.find('script', {'id': 'sircMessage1'})
            script = node.get_text().strip()
            m = re.search('window\.sircMessage\.sircPAGEKEY\s?=\s?\'([\w\+%]+)\';', script)
            if m is not None:
                pagekey = m.group(1)
                for c in r.cookies:
                    cookies[c.name] = c.value

        # Main request
        url = url + '?pagekey=' + pagekey
        headers = {
            'Origin': 'http://map.tgos.nat.gov.tw',
            'Referer': 'http://map.tgos.nat.gov.tw/TGOSCLOUD/Web/Map/TGOSViewer_Map.aspx',
            'X-Requested-With': 'XMLHttpRequest'
        }
        kwargs['params']['sid'] = cookies['ASP.NET_SessionId']
        return requests.post(url, headers=headers, cookies=cookies, data=kwargs['params'])

if __name__ == '__main__':
    try:
        g = Tgos('台北市內湖區內湖路一段735號')
        print(g.url)
        g.debug()
    except Exception as ex:
        print(ex)
