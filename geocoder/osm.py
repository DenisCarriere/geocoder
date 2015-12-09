#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base


class Osm(Base):
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

    def __init__(self, location, **kwargs):
        self.url = self._get_osm_url(kwargs.get('url', ''))
        self.location = location
        self.params = {
            'q': location,
            'format': 'jsonv2',
            'addressdetails': 1,
            'limit': kwargs.get('limit', 1),
        }
        self._initialize(**kwargs)

    def _get_osm_url(self, url):
        if url.lower() == 'localhost':
            return 'http://localhost/nominatim/search'
        elif url:
            return url
        else:
            return 'https://nominatim.openstreetmap.org/search'

    def _exceptions(self):
        if self.content:
            self._build_tree(self.content[0])

    def __iter__(self):
        for item in self.content:
            yield item

    # ============================ #
    # Geometry - Points & Polygons #
    # ============================ #

    @property
    def lat(self):
        lat = self.parse.get('lat')
        if lat:
            return float(lat)

    @property
    def lng(self):
        lng = self.parse.get('lon')
        if lng:
            return float(lng)

    @property
    def bbox(self):
        if self.parse['boundingbox']:
            south = float(self.parse['boundingbox'][0])
            west = float(self.parse['boundingbox'][2])
            north = float(self.parse['boundingbox'][1])
            east = float(self.parse['boundingbox'][3])
            return self._get_bbox(south, west, north, east)

    # ========================== #
    # Tags for individual houses #
    # ========================== #

    @property
    def address(self):
        return self.parse.get('display_name')

    @property
    def housenumber(self):
        return self.parse['address'].get('house_number')

    @property
    def street(self):
        return self.parse['address'].get('road')

    @property
    def postal(self):
        return self.parse['address'].get('postcode')

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
        return self.parse['address'].get('neighbourhood')

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
        return self.parse['address'].get('suburb')

    @property
    def quarter(self):
        """place=quarter

        A named part of a bigger settlement where this part is smaller than
        a suburb and bigger than a neighbourhood. This does not have to be
        an administrative entity.

        The term quarter is sometimes used synonymously for neighbourhood.
        """
        return self.parse['address'].get('quarter')

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
        return self.parse['address'].get('hamlet')

    @property
    def farm(self):
        """place=farm

        A farm that has its own name. If the farm is not a part of bigger
        settlement use place=isolated_dwelling. See also landuse=farmyard
        """
        return self.parse['address'].get('hamlet')

    @property
    def locality(self):
        """place=isolated_dwelling

        For an unpopulated named place.
        """
        return self.parse['address'].get('locality')

    @property
    def isolated_dwelling(self):
        """place=isolated_dwelling

        Smallest kind of human settlement. No more than 2 households.
        """
        return self.parse['address'].get('hamlet')

    @property
    def hamlet(self):
        """place=hamlet

        A smaller rural community typically with less than 100-200 inhabitants,
        few infrastructure.
        """
        return self.parse['address'].get('hamlet')

    @property
    def village(self):
        """place=village

        A smaller distinct settlement, smaller than a town with few facilities
        available with people traveling to nearby towns to access these.
        Populations of villages vary widely in different territories but will
        nearly always be less than 10,000 people, often a lot less.

        See place=neighbourhood on how to tag divisions within a larger village
        """
        return self.parse['address'].get('village')

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
        return self.parse['address'].get('town')

    @property
    def island(self):
        """place=island

        Identifies the coastline of an island (> 1 km2), also consider
        place=islet for very small islandsIdentifies the coastline of an
        island (> 1 km2), also consider place=islet for very small islands
        """
        return self.parse['address'].get('island')

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
        return self.parse['address'].get('city')

    # ================================ #
    # Administratively declared places #
    # ================================ #

    @property
    def municipality(self):
        """admin_level=8"""
        return self.parse['address'].get('municipality')

    @property
    def county(self):
        """admin_level=6"""
        return self.parse['address'].get('county')

    @property
    def district(self):
        """admin_level=5/6"""
        return self.parse['address'].get('city_district')

    @property
    def state(self):
        """admin_level=4"""
        return self.parse['address'].get('state')

    @property
    def region(self):
        """admin_level=3"""
        return self.parse['address'].get('state')

    @property
    def country(self):
        """admin_level=2"""
        return self.parse['address'].get('country')

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
        return self.parse.get('population')

    @property
    def license(self):
        return self.parse.get('license')

    @property
    def type(self):
        return self.parse.get('type')

    @property
    def importance(self):
        return self.parse.get('importance')

    @property
    def icon(self):
        return self.parse.get('icon')

    @property
    def osm_type(self):
        return self.parse.get('osm_type')

    @property
    def osm_id(self):
        return self.parse.get('osm_id')

    @property
    def place_id(self):
        return self.parse.get('place_id')

    @property
    def place_rank(self):
        return self.parse.get('place_rank')


if __name__ == '__main__':
    g = Osm("Ottawa, ON")
    g.debug()
