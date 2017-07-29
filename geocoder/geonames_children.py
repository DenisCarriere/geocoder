from __future__ import absolute_import

from geocoder.geonames import Geonames
from geocoder.keys import geonames_username


class GeonamesChildren(Geonames):
    """ Children:
        http://api.geonames.org/childrenJSON?formatted=true&geonameId=6094817
    """

    provider = 'geonames'
    method = 'children'

    def __init__(self, geonameid, url='http://api.geonames.org/childrenJSON', **kwargs):
        self.url = url
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
    print("Searching Ottawa...")
    g = Geonames('Ottawa, Ontario')
    g.debug()
    print("Searching its children...")
    c = GeonamesChildren(g.geonames_id)
    c.debug()
