#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import

from geocoder.distance import Distance
from geocoder.location import Location

from geocoder.arcgis import ArcgisQuery
from geocoder.baidu import BaiduQuery
from geocoder.bing import BingQuery, BingQueryDetail
from geocoder.canadapost import CanadapostQuery
from geocoder.freegeoip import FreeGeoIPQuery
from geocoder.gaode import GaodeQuery
from geocoder.geocodefarm import GeocodeFarmQuery
from geocoder.geolytica import GeolyticaQuery
from geocoder.gisgraphy import GisgraphyQuery
from geocoder.here import HereQuery
from geocoder.ipinfo import IpinfoQuery
from geocoder.komoot import KomootQuery
from geocoder.locationiq import LocationIQQuery
from geocoder.mapbox import MapboxQuery
from geocoder.mapquest import MapquestQuery
from geocoder.mapzen import MapzenQuery
from geocoder.maxmind import MaxmindQuery
from geocoder.opencage import OpenCageQuery
from geocoder.osm import OsmQuery, OsmQueryDetail
from geocoder.ottawa import OttawaQuery
from geocoder.tamu import TamuQuery
from geocoder.tomtom import TomtomQuery
from geocoder.tgos import TgosQuery
from geocoder.uscensus import USCensusQuery
from geocoder.yahoo import YahooQuery
from geocoder.yandex import YandexQuery
from geocoder.w3w import W3WQuery

from geocoder.arcgis_reverse import ArcgisReverse
from geocoder.baidu_reverse import BaiduReverse
from geocoder.bing_reverse import BingReverse
from geocoder.gaode_reverse import GaodeReverse
from geocoder.geocodefarm_reverse import GeocodeFarmReverse
from geocoder.gisgraphy_reverse import GisgraphyReverse
from geocoder.here_reverse import HereReverse
from geocoder.locationiq_reverse import LocationIQReverse
from geocoder.komoot_reverse import KomootReverse
from geocoder.mapbox_reverse import MapboxReverse
from geocoder.mapquest_reverse import MapquestReverse
from geocoder.mapzen_reverse import MapzenReverse
from geocoder.opencage_reverse import OpenCageReverse
from geocoder.osm_reverse import OsmReverse
from geocoder.uscensus_reverse import USCensusReverse
from geocoder.w3w_reverse import W3WReverse
from geocoder.yandex_reverse import YandexReverse

from geocoder.mapquest_batch import MapquestBatch
from geocoder.bing_batch_forward import BingBatchForward
from geocoder.bing_batch_reverse import BingBatchReverse
from geocoder.uscensus_batch import USCensusBatch

# Geonames Services
from geocoder.geonames import GeonamesQuery
from geocoder.geonames_details import GeonamesDetails
from geocoder.geonames_children import GeonamesChildren
from geocoder.geonames_hierarchy import GeonamesHierarchy

# Google Services
from geocoder.google import GoogleQuery
from geocoder.google_timezone import TimezoneQuery
from geocoder.google_reverse import GoogleReverse
from geocoder.google_elevation import ElevationQuery
from geocoder.google_places import PlacesQuery

options = {
    'osm': {
        'geocode': OsmQuery,
        'details': OsmQueryDetail,
        'reverse': OsmReverse,
    },
    'tgos': {
        'geocode': TgosQuery
    },
    'here': {
        'geocode': HereQuery,
        'reverse': HereReverse,
    },
    'baidu': {
        'geocode': BaiduQuery,
        'reverse': BaiduReverse
    },
    'gaode': {
        'geocode': GaodeQuery,
        'reverse': GaodeReverse
    },
    'yahoo': {'geocode': YahooQuery},
    'tomtom': {'geocode': TomtomQuery},
    'arcgis': {
        'geocode': ArcgisQuery,
        'reverse': ArcgisReverse
    },
    'ottawa': {'geocode': OttawaQuery},
    'mapbox': {
        'geocode': MapboxQuery,
        'reverse': MapboxReverse,
    },
    'maxmind': {'geocode': MaxmindQuery},
    'ipinfo': {'geocode': IpinfoQuery},
    'geonames': {
        'geocode': GeonamesQuery,
        'details': GeonamesDetails,
        'timezone': GeonamesDetails,
        'children': GeonamesChildren,
        'hierarchy': GeonamesHierarchy
    },
    'freegeoip': {'geocode': FreeGeoIPQuery},
    'w3w': {
        'geocode': W3WQuery,
        'reverse': W3WReverse,
    },
    'yandex': {
        'geocode': YandexQuery,
        'reverse': YandexReverse
    },
    'mapquest': {
        'geocode': MapquestQuery,
        'reverse': MapquestReverse,
        'batch': MapquestBatch
    },
    'geolytica': {'geocode': GeolyticaQuery},
    'canadapost': {'geocode': CanadapostQuery},
    'opencage': {
        'geocode': OpenCageQuery,
        'reverse': OpenCageReverse,
    },
    'bing': {
        'geocode': BingQuery,
        'details': BingQueryDetail,
        'reverse': BingReverse,
        'batch': BingBatchForward,
        'batch_reverse': BingBatchReverse
    },
    'google': {
        'geocode': GoogleQuery,
        'reverse': GoogleReverse,
        'timezone': TimezoneQuery,
        'elevation': ElevationQuery,
        'places': PlacesQuery,
    },
    'mapzen': {
        'geocode': MapzenQuery,
        'reverse': MapzenReverse,
    },
    'komoot': {
        'geocode': KomootQuery,
        'reverse': KomootReverse,
    },
    'tamu': {
        'geocode': TamuQuery
    },
    'geocodefarm': {
        'geocode': GeocodeFarmQuery,
        'reverse': GeocodeFarmReverse,
    },
    'uscensus': {
        'geocode': USCensusQuery,
        'reverse': USCensusReverse,
        'batch': USCensusBatch
    },
    'locationiq': {
        'geocode': LocationIQQuery,
        'reverse': LocationIQReverse,
    },
    'gisgraphy': {
        'geocode': GisgraphyQuery,
        'reverse': GisgraphyReverse,
    },
}


def get(location, **kwargs):
    """Get Geocode

    :param ``location``: Your search location you want geocoded.
    :param ``provider``: The geocoding engine you want to use.

    :param ``method``: Define the method (geocode, method).
    """
    provider = kwargs.get('provider', 'bing').lower().strip()
    method = kwargs.get('method', 'geocode').lower().strip()
    if isinstance(location, (list, dict)) and method == 'geocode':
        raise ValueError("Location should be a string")

    if provider not in options:
        raise ValueError("Invalid provider")

    else:
        if method not in options[provider]:
            raise ValueError("Invalid method")
    return options[provider][method](location, **kwargs)


def distance(*args, **kwargs):
    """Distance tool measures the distance between two or multiple points.

    :param ``location``: (min 2x locations) Your search location you want geocoded.
    :param ``units``: (default=kilometers) Unit of measurement.
        > kilometers
        > miles
        > feet
        > meters
    """
    return Distance(*args, **kwargs)


def location(location, **kwargs):
    """Parser for different location formats
    """
    return Location(location, **kwargs)


def google(location, **kwargs):
    """Google Provider

    :param ``location``: Your search location you want geocoded.
    :param ``method``: (default=geocode) Use the following:
        > geocode
        > places
        > reverse
        > batch
        > timezone
        > elevation
    """
    return get(location, provider='google', **kwargs)


def mapbox(location, **kwargs):
    """Mapbox Provider

    :param ``location``: Your search location you want geocoded.
    :param ``proximity``: Search nearby [lat, lng]
    :param ``method``: (default=geocode) Use the following:
        > geocode
        > reverse
        > batch
    """
    return get(location, provider='mapbox', **kwargs)


def yandex(location, **kwargs):
    """Yandex Provider

    :param ``location``: Your search location you want geocoded.
    :param ``maxRows``: (default=1) Max number of results to fetch
    :param ``lang``: Chose the following language:
        > ru-RU — Russian (by default)
        > uk-UA — Ukrainian
        > be-BY — Belarusian
        > en-US — American English
        > en-BR — British English
        > tr-TR — Turkish (only for maps of Turkey)
    :param ``kind``: Type of toponym (only for reverse geocoding):
        > house - house or building
        > street - street
        > metro - subway station
        > district - city district
        > locality - locality (city, town, village, etc.)
    """
    return get(location, provider='yandex', **kwargs)


def w3w(location, **kwargs):
    """what3words Provider

    :param ``location``: Your search location you want geocoded.
    :param ``key``: W3W API key.
    :param ``method``: Chose a method (geocode, method)
    """
    return get(location, provider='w3w', **kwargs)


def baidu(location, **kwargs):
    """Baidu Provider

    :param ``location``: Your search location you want geocoded.
    :param ``key``: Baidu API key.
    :param ``referer``: Baidu API referer website.
    """
    return get(location, provider='baidu', **kwargs)


def gaode(location, **kwargs):
    """Gaode Provider

    :param ``location``: Your search location you want geocoded.
    :param ``key``: Gaode API key.
    :param ``referer``: Gaode API referer website.
    """
    return get(location, provider='gaode', **kwargs)


def komoot(location, **kwargs):
    """Ottawa Provider

    :param ``location``: Your search location you want geocoded.
    """
    return get(location, provider='komoot', **kwargs)


def ottawa(location, **kwargs):
    """Ottawa Provider

    :param ``location``: Your search location you want geocoded.
    :param ``maxRows``: (default=1) Max number of results to fetch
    """
    return get(location, provider='ottawa', **kwargs)


def elevation(location, **kwargs):
    """Elevation - Google Provider

    :param ``location``: Your search location you want to retrieve elevation data.
    """
    return get(location, method='elevation', provider='google', **kwargs)


def places(location, **kwargs):
    """Places - Google Provider

    :param ``location``: Your search location you want geocoded.
    :param ``proximity``: Search within given area (bbox, bounds, or around latlng)
    """
    return get(location, method='places', provider='google', **kwargs)


def timezone(location, **kwargs):
    """Timezone - Google Provider

    :param ``location``: Your search location you want to retrieve timezone data.
    :param ``timestamp``: Define your own specified time to calculate timezone.
    """
    return get(location, method='timezone', provider='google', **kwargs)


def reverse(location, provider="google", **kwargs):
    """Reverse Geocoding

    :param ``location``: Your search location you want to reverse geocode.
    :param ``key``: (optional) use your own API Key from Bing.
    :param ``provider``: (default=google) Use the following:
        > google
        > bing
    """
    return get(location, method='reverse', provider=provider, **kwargs)


def bing(location, **kwargs):
    """Bing Provider

    :param ``location``: Your search location you want geocoded.
    :param ``key``: (optional) use your own API Key from Bing.
    :param ``maxRows``: (default=1) Max number of results to fetch
    :param ``method``: (default=geocode) Use the following:
        > geocode
        > reverse
    """
    return get(location, provider='bing', **kwargs)


def yahoo(location, **kwargs):
    """Yahoo Provider

    :param ``location``: Your search location you want geocoded.
    """
    return get(location, provider='yahoo', **kwargs)


def geolytica(location, **kwargs):
    """Geolytica (Geocoder.ca) Provider

    :param ``location``: Your search location you want geocoded.
    """
    return get(location, provider='geolytica', **kwargs)


def opencage(location, **kwargs):
    """Opencage Provider

    :param ``location``: Your search location you want geocoded.
    :param ``key``: (optional) use your own API Key from OpenCage.
    """
    return get(location, provider='opencage', **kwargs)


def arcgis(location, **kwargs):
    """ArcGIS Provider

    :param ``location``: Your search location you want geocoded.
    """
    return get(location, provider='arcgis', **kwargs)


def here(location, **kwargs):
    """HERE Provider

    :param ``location``: Your search location you want geocoded.
    :param ``app_code``: (optional) use your own Application Code from HERE.
    :param ``app_id``: (optional) use your own Application ID from HERE.
    :param ``maxRows``: (default=1) Max number of results to fetch
    :param ``method``: (default=geocode) Use the following:
        > geocode
        > reverse
    """
    return get(location, provider='here', **kwargs)


def nokia(location, **kwargs):
    """HERE Provider

    :param ``location``: Your search location you want geocoded.
    :param ``app_code``: (optional) use your own Application Code from HERE.
    :param ``app_id``: (optional) use your own Application ID from HERE.
    :param ``method``: (default=geocode) Use the following:
        > geocode
        > reverse
    """
    return get(location, provider='here', **kwargs)


def tomtom(location, **kwargs):
    """TomTom Provider

    :param ``location``: Your search location you want geocoded.
    :param ``key``: (optional) use your own API Key from TomTom.
    :param ``maxRows``: (default=1) Max number of results to fetch
    """
    return get(location, provider='tomtom', **kwargs)


def mapquest(location, **kwargs):
    """MapQuest Provider

    :param ``location``: Your search location you want geocoded.
    :param ``key``: (optional) use your own API Key from MapQuest.
    :param ``maxRows``: (default=1) Max number of results to fetch
    :param ``method``: (default=geocode) Use the following:
        > geocode
        > reverse
    """
    return get(location, provider='mapquest', **kwargs)


def osm(location, **kwargs):
    """OSM Provider

    :param ``location``: Your search location you want geocoded.
    :param ``url``: Custom OSM Server URL location
               (ex: http://nominatim.openstreetmap.org/search)
    """
    return get(location, provider='osm', **kwargs)


def maxmind(location='me', **kwargs):
    """MaxMind Provider

    :param ``location``: Your search IP Address you want geocoded.
    :param ``location``: (optional) if left blank will return your
                                current IP address's location.
    """
    return get(location, provider='maxmind', **kwargs)


def ipinfo(location='', **kwargs):
    """IP Info.io Provider

    :param ``location``: Your search IP Address you want geocoded.
    :param ``location``: (optional) if left blank will return your
                                current IP address's location.
    """
    return get(location, provider='ipinfo', **kwargs)


def freegeoip(location, **kwargs):
    """FreeGeoIP Provider

    :param ``location``: Your search IP Address you want geocoded.
    :param ``location``: (optional) if left blank will return your
                                current IP address's location.
    """
    return get(location, provider='freegeoip', **kwargs)


def ip(location, **kwargs):
    """IP Address lookup

    :param ``location``: Your search IP Address you want geocoded.
    :param ``location``: (optional) if left blank will return your
                                current IP address's location.
    """
    return get(location, provider='ipinfo', **kwargs)


def canadapost(location, **kwargs):
    """CanadaPost Provider

    :param ``location``: Your search location you want geocoded.
    :param ``key``: (optional) API Key from CanadaPost Address Complete.
    :param ``language``: (default=en) Output language preference.
    :param ``country``: (default=ca) Geofenced query by country.
    :param ``maxRows``: (default=1) Max number of results to fetch
    """
    return get(location, provider='canadapost', **kwargs)


def postal(location, **kwargs):
    """CanadaPost Provider

    :param ``location``: Your search location you want geocoded.
    :param ``key``: (optional) use your own API Key from
                               CanadaPost Address Complete.
    """
    return get(location, provider='canadapost', **kwargs)


def geonames(location, **kwargs):
    """GeoNames Provider

    :param ``location``: Your search location you want geocoded.
    :param ``geonameid``: The place you want children / hierarchy for.
    :param ``key``: (required) geonames *username*: needs to be passed with each request.
    :param ``maxRows``: (default=1) Max number of results to fetch
    :param ``proximity``: Search within given area (bbox, bounds, or around latlng)
    :param ``method``: (default=geocode) Use the following:
        > geocode
        > details (mainly for administrive data and timezone)
        > timezone (alias for details)
        > children
        > hierarchy
    """
    return get(location, provider='geonames', **kwargs)


def mapzen(location, **kwargs):
    """Mapzen Provider

    :param ``location``: Your search location you want geocoded.
    :param ``maxRows``: (default=1) Max number of results to fetch
    """
    return get(location, provider='mapzen', **kwargs)


def tamu(location, **kwargs):
    """TAMU Provider

    Params
    ------
    :param ``location``: The street address of the location you want geocoded.
    :param ``city``: The city of the location to geocode.
    :param ``state``: The state of the location to geocode.
    :param ``zipcode``: The zipcode of the location to geocode.
    :param ``key``: The API key (use API key "demo" for testing).

    API Reference
    -------------
    https://geoservices.tamu.edu/Services/Geocode/WebService
    """
    return get(location, provider='tamu', **kwargs)


def geocodefarm(location, **kwargs):
    """GeocodeFarm Provider

    Params
    ------
    :param ``location``: The string to search for. Usually a street address.
    :param ``key``: (optional) API Key. Only Required for Paid Users.
    :param ``lang``: (optional) 2 digit language code to return results in. Currently only "en"(English) or "de"(German) supported.
    :param ``country``: (optional) The country to return results in. Used for biasing purposes and may not fully filter results to this specific country.
    :param ``maxRows``: (default=1) Max number of results to fetch

    API Reference
    -------------
    https://geocode.farm/geocoding/free-api-documentation/
    """
    return get(location, provider='geocodefarm', **kwargs)


def tgos(location, **kwargs):
    """TGOS Provider

    :param ``location``: Your search location you want geocoded.
    :param ``language``: (default=taiwan) Use the following:
        > taiwan
        > english
        > chinese
    :param ``method``: (default=geocode) Use the following:
        > geocode

    API Reference
    -------------
    http://api.tgos.nat.gov.tw/TGOS_MAP_API/Web/Default.aspx
    """
    return get(location, provider='tgos', **kwargs)


def uscensus(location, **kwargs):
    """US Census Provider

    Params
    ------
    :param ``location``: Your search location(s) you want geocoded.
    :param ``benchmark``: (default=4) Use the following:
        > Public_AR_Current or 4
        > Public_AR_ACSYYYY or 8
        > Public_AR_Census2010 or 9
    :param ``vintage``: (default=4, not available with batch method) Use the following:
        > Current_Current or 4
        > Census2010_Current or 410
        > ACS2013_Current or 413
        > ACS2014_Current or 414
        > ACS2015_Current or 415
        > Current_ACS2015 or 8
        > Census2010_ACS2015 or 810
        > ACS2013_ACS2015 or 813
        > ACS2014_ACS2015 or 814
        > ACS2015_ACS2015 or 815
        > Census2010_Census2010 or 910
        > Census2000_Census2010 or 900
    :param ``method``: (default=geocode) Use the following:
        > geocode
        > reverse
        > batch

    API Reference
    -------------
    https://geocoding.geo.census.gov/geocoder/Geocoding_Services_API.pdf
    """
    return get(location, provider='uscensus', **kwargs)


def locationiq(location, **kwargs):
    """LocationIQ Provider

    Params
    ------
    :param ``location``: Your search location you want geocoded.
    :param ``method``: (default=geocode) Use the following:
        > geocode
        > reverse

    API Reference
    -------------
    https://locationiq.org/
    """
    return get(location, provider='locationiq', **kwargs)


def gisgraphy(location, **kwargs):
    """Gisgraphy Provider

    :param ``location``: Your search location you want geocoded.
    """
    return get(location, provider='gisgraphy', **kwargs)
