from __future__ import absolute_import

from geocoder.geonames_children import GeonamesChildren


class GeonamesHierarchy(GeonamesChildren):
    """ Hierarchy:
        http://api.geonames.org/hierarchyJSON?formatted=true&geonameId=6094817
    """

    provider = 'geonames'
    method = 'hierarchy'

    def __init__(self, geonameid, **kwargs):
        url = 'http://api.geonames.org/hierarchyJSON'
        super(GeonamesHierarchy, self).__init__(geonameid, url=url, **kwargs)
