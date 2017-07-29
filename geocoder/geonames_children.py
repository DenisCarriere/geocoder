from __future__ import absolute_import

from geocoder.geonames import Geonames
from geocoder.keys import geonames_username


class GeonamesChidren(Geonames):
    """ Children:
        http://api.geonames.org/childrenJSON?formatted=true&geonameId=6094817
    """

    provider = 'geonames'
    method = 'children'

    def __init__(self, geonameid, **kwargs):
        self.url = 'http://api.geonames.org/childrenJSON'
        self.geonameid = geonameid
        username = kwargs.get('username', geonames_username)
        if not username:
            raise ValueError('Provide username')
        self.params = {
            'geonameId': geonameid,
            'username': username,
        }
        self._initialize(**kwargs)


if __name__ == '__main__':
    g = Geonames('Ottawa, Ontario')
    g.debug()
    c = GeonamesChidren(g.geonames_id)
    c.debug()
