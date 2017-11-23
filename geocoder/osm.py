#!/usr/bin/python
# coding: utf8
from __future__ import absolute_import

import logging
import json

from geocoder.base import OneResult, MultipleResultsQuery


class OsmResult(OneResult):

    def __init__(self, json_content):
        # create safe shortcuts
        self._address = json_content.get('address', {})

        # proceed with super.__init__
        super(OsmResult, self).__init__(json_content)

    # ============================ #
    # Geometry - Points & Polygons #
    # ============================ #

    @property
    def lat(self):
        lat = self.raw.get('lat')
        if lat:
            return float(lat)

    @property
    def lng(self):
        lng = self.raw.get('lon')
        if lng:
            return float(lng)

    @property
    def bbox(self):
        _boundingbox = self.raw.get('boundingbox')
        if _boundingbox:
            south = float(_boundingbox[0])
            west = float(_boundingbox[2])
            north = float(_boundingbox[1])
            east = float(_boundingbox[3])
            return self._get_bbox(south, west, north, east)

    # ========================== #
    # Tags for individual houses #
    # ========================== #

    @property
    def address(self):
        return self.raw.get('display_name')

    @property
    def housenumber(self):
        return self._address.get('house_number')

    @property
    def street(self):
        return self._address.get('road')

    @property
    def postal(self):
        return self._address.get('postcode')

    # ============================ #
    # Populated settlements, urban #
    # ============================ #

    @property
    def neighborhood(self):
        """place=neighborhood

        A named part of a place=village, a place=town or a place=city. Smaller
        than place=suburb and place=quarter.

        The tag can be used for any kind of landuse or mix of landuse (such as
        residential, commercial, industrial etc). Usage of this term depends
        greatly on local history, culture, politics, economy and organization
        of settlements. More specific rules are intentionally avoided.

        Note: the British English spelling is used rather than the
              American English spelling of neighborhood.
        """
        return self._address.get('neighbourhood')

    @property
    def suburb(self):
        """place=suburb

        A distinct section of an urban settlement (city, town, etc.) with its
        own name and identity. e.g.

        - annexed towns or villages which were formerly independent,
        - independent (or dependent) municipalities within a city or next to a
          much bigger town
        - historical districts of settlements
        - industrial districts or recreation areas within a settlements with
          specific names.
        """
        return self._address.get('suburb')

    @property
    def quarter(self):
        """place=quarter

        A named part of a bigger settlement where this part is smaller than
        a suburb and bigger than a neighbourhood. This does not have to be
        an administrative entity.

        The term quarter is sometimes used synonymously for neighbourhood.
        """
        return self._address.get('quarter')

    # ====================================== #
    # Populated settlements, urban and rural #
    # ====================================== #

    @property
    def allotments(self):
        """place=allotments

        Dacha or cottage settlement, which is located outside other
        inhabited locality. This value is used mainly in Russia and other
        countries of the former Soviet Union, where a lot of such unofficial
        settlements exist
        """
        return self._address.get('hamlet')

    @property
    def farm(self):
        """place=farm

        A farm that has its own name. If the farm is not a part of bigger
        settlement use place=isolated_dwelling. See also landuse=farmyard
        """
        return self._address.get('hamlet')

    @property
    def locality(self):
        """place=isolated_dwelling

        For an unpopulated named place.
        """
        return self._address.get('locality')

    @property
    def isolated_dwelling(self):
        """place=isolated_dwelling

        Smallest kind of human settlement. No more than 2 households.
        """
        return self._address.get('hamlet')

    @property
    def hamlet(self):
        """place=hamlet

        A smaller rural community typically with less than 100-200 inhabitants,
        few infrastructure.
        """
        return self._address.get('hamlet')

    @property
    def village(self):
        """place=village

        A smaller distinct settlement, smaller than a town with few facilities
        available with people traveling to nearby towns to access these.
        Populations of villages vary widely in different territories but will
        nearly always be less than 10,000 people, often a lot less.

        See place=neighbourhood on how to tag divisions within a larger village
        """
        return self._address.get('village')

    @property
    def town(self):
        """place=town

        A second tier urban settlement of local importance, often with a
        population of 10,000 people and good range of local facilities
        including schools, medical facilities etc and traditionally a market.
        In areas of low population, towns may have significantly
        lower populations.

        See place=neighbourhood and possibly also place=suburb on how to tag
        divisions within a town.
        """
        return self._address.get('town')

    @property
    def island(self):
        """place=island

        Identifies the coastline of an island (> 1 km2), also consider
        place=islet for very small islandsIdentifies the coastline of an
        island (> 1 km2), also consider place=islet for very small islands
        """
        return self._address.get('island')

    @property
    def city(self):
        """place=city

        The largest urban settlements in the territory, normally including the
        national, state and provincial capitals. These are defined by charter
        or other governmental designation in some territories and are a matter
        of judgement in others. Should normally have a population of at
        least 100,000 people and be larger than nearby towns.

        See place=suburb and place=neighbourhood on how to tag divisions
        within a city. The outskirts of urban settlements may or may not match
        the administratively declared boundary of the city.
        """
        return self._address.get('city')

    # ================================ #
    # Administratively declared places #
    # ================================ #

    @property
    def municipality(self):
        """admin_level=8"""
        return self._address.get('municipality')

    @property
    def county(self):
        """admin_level=6"""
        return self._address.get('county')

    @property
    def district(self):
        """admin_level=5/6"""
        return self._address.get('city_district')

    @property
    def state(self):
        """admin_level=4"""
        return self._address.get('state')

    @property
    def region(self):
        """admin_level=3"""
        return self._address.get('state')

    @property
    def country(self):
        """admin_level=2"""
        return self._address.get('country')

    @property
    def country_code(self):
        """admin_level=2"""
        return self._address.get('country_code')

    # ======================== #
    # Quality Control & Others #
    # ======================== #

    @property
    def accuracy(self):
        return self.importance

    @property
    def quality(self):
        return self.type

    @property
    def population(self):
        return self.raw.get('population')

    @property
    def license(self):
        return self.raw.get('license')

    @property
    def type(self):
        return self.raw.get('type')

    @property
    def importance(self):
        return self.raw.get('importance')

    @property
    def icon(self):
        return self.raw.get('icon')

    @property
    def osm_type(self):
        return self.raw.get('osm_type')

    @property
    def osm_id(self):
        return self.raw.get('osm_id')

    @property
    def place_id(self):
        return self.raw.get('place_id')

    @property
    def place_rank(self):
        return self.raw.get('place_rank')


class OsmQuery(MultipleResultsQuery):
    """
    Nominatim
    =========
    Nominatim (from the Latin, 'by name') is a tool to search OSM data by name
    and address and to generate synthetic addresses of OSM points (reverse geocoding).

    API Reference
    -------------
    http://wiki.openstreetmap.org/wiki/Nominatim
    """
    provider = 'osm'
    method = 'geocode'

    _URL = 'https://nominatim.openstreetmap.org/search'
    _RESULT_CLASS = OsmResult
    _KEY_MANDATORY = False

    def _build_params(self, location, provider_key, **kwargs):
        # backward compatitibility for 'limit' (now maxRows)
        if 'limit' in kwargs:
            logging.warning(
                "argument 'limit' in OSM is deprecated and should be replaced with maxRows")
            kwargs['maxRows'] = kwargs['limit']
        # build params
        return {
            'q': location,
            'format': 'jsonv2',
            'addressdetails': 1,
            'limit': kwargs.get('maxRows', 1),
        }

    def _before_initialize(self, location, **kwargs):
        """ Check if specific URL has not been provided, otherwise, use cls._URL"""
        url = kwargs.get('url', '')
        if url.lower() == 'localhost':
            self.url = 'http://localhost/nominatim/search'
        elif url:
            self.url = url
        # else:  do not change self.url, which is cls._URL


class OsmQueryDetail(MultipleResultsQuery):
    """
    Nominatim
    =========
    Nominatim (from the Latin, 'by name') is a tool to search OSM data by name
    and address and to generate synthetic addresses of OSM points (reverse geocoding).

    API Reference
    -------------
    http://wiki.openstreetmap.org/wiki/Nominatim
    """
    provider = 'osm'
    method = 'details'

    _URL = 'https://nominatim.openstreetmap.org/search'
    _RESULT_CLASS = OsmResult
    _KEY_MANDATORY = False

    def _build_params(self, location, provider_key, **kwargs):
        # backward compatitibility for 'limit' (now maxRows)
        if 'limit' in kwargs:
            logging.warning(
                "argument 'limit' in OSM is deprecated and should be replaced with maxRows")
            kwargs['maxRows'] = kwargs['limit']
        # build params
        query = {
            'format': 'jsonv2',
            'addressdetails': 1,
            'limit': kwargs.get('maxRows', 1),
        }
        query.update(kwargs)
        return query

    def _before_initialize(self, location, **kwargs):
        """ Check if specific URL has not been provided, otherwise, use cls._URL"""
        url = kwargs.get('url', '')
        if url.lower() == 'localhost':
            self.url = 'http://localhost/nominatim/search'
        elif url:
            self.url = url
        # else:  do not change self.url, which is cls._URL


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = OsmQuery('Ottawa, Ontario')
    g.debug()
    g = OsmQuery('Ottawa, Ontario', maxRows=5)
    print(json.dumps(g.geojson, indent=4))
