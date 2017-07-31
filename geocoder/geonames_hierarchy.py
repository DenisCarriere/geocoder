from __future__ import absolute_import

from geocoder.geonames_children import GeonamesChildren


class GeonamesHierarchy(GeonamesChildren):
    """ Hierarchy:
        http://api.geonames.org/hierarchyJSON?formatted=true&geonameId=6094817
    """

    provider = 'geonames'
    method = 'hierarchy'

    _URL = 'http://api.geonames.org/hierarchyJSON'


if __name__ == '__main__':
    print("Searching Ottawa's hierarchy...")
    c = GeonamesHierarchy(6094817)
    c.debug()
