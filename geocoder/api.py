#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import

from geocoder.osm import Osm
from geocoder.w3w import W3W
from geocoder.bing import Bing
from geocoder.here import Here
from geocoder.tamu import Tamu
from geocoder.tgos import Tgos
from geocoder.yahoo import Yahoo
from geocoder.baidu import Baidu
from geocoder.tomtom import Tomtom
from geocoder.arcgis import Arcgis
from geocoder.ottawa import Ottawa
from geocoder.yandex import Yandex
from geocoder.mapbox import Mapbox
from geocoder.mapzen import Mapzen
from geocoder.ipinfo import Ipinfo
from geocoder.komoot import Komoot
from geocoder.maxmind import Maxmind
from geocoder.location import Location
from geocoder.opencage import OpenCage
from geocoder.geonames import Geonames
from geocoder.mapquest import Mapquest
from geocoder.distance import Distance
from geocoder.geolytica import Geolytica
from geocoder.freegeoip import FreeGeoIP
from geocoder.canadapost import Canadapost
from geocoder.geocodefarm import GeocodeFarm
from geocoder.uscensus import USCensus
from geocoder.w3w_reverse import W3WReverse
from geocoder.osm_reverse import OsmReverse
from geocoder.here_reverse import HereReverse
from geocoder.bing_reverse import BingReverse
from geocoder.arcgis_reverse import ArcgisReverse
from geocoder.mapzen_reverse import MapzenReverse
from geocoder.komoot_reverse import KomootReverse
from geocoder.mapbox_reverse import MapboxReverse
from geocoder.yandex_reverse import YandexReverse
from geocoder.mapquest_reverse import MapquestReverse
from geocoder.opencage_reverse import OpenCageReverse
from geocoder.geocodefarm_reverse import GeocodeFarmReverse
from geocoder.uscensus_reverse import USCensusReverse

# Google Services
from geocoder.google import Google
from geocoder.google_timezone import Timezone
from geocoder.google_reverse import GoogleReverse
from geocoder.google_elevation import Elevation
from geocoder.google_places import Places

options = {
    'osm': {
        'geocode': Osm,
        'reverse': OsmReverse,
    },
    'tgos': {
        'geocode': Tgos
    },
    'here': {
        'geocode': Here,
        'reverse': HereReverse,
    },
    'baidu': {'geocode': Baidu},
    'yahoo': {'geocode': Yahoo},
    'tomtom': {'geocode': Tomtom},
    'arcgis': {
        'geocode': Arcgis,
        'reverse': ArcgisReverse
    },
    'ottawa': {'geocode': Ottawa},
    'mapbox': {
        'geocode': Mapbox,
        'reverse': MapboxReverse,
    },
    'maxmind': {'geocode': Maxmind},
    'ipinfo': {'geocode': Ipinfo},
    'geonames': {'geocode': Geonames},
    'freegeoip': {'geocode': FreeGeoIP},
    'w3w': {
        'geocode': W3W,
        'reverse': W3WReverse,
    },
    'yandex': {
        'geocode': Yandex,
        'reverse': YandexReverse
    },
    'mapquest': {
        'geocode': Mapquest,
        'reverse': MapquestReverse,
    },
    'geolytica': {'geocode': Geolytica},
    'canadapost': {'geocode': Canadapost},
    'opencage': {
        'geocode': OpenCage,
        'reverse': OpenCageReverse,
    },
    'bing': {
        'geocode': Bing,
        'reverse': BingReverse,
    },
    'google': {
        'geocode': Google,
        'reverse': GoogleReverse,
        'timezone': Timezone,
        'elevation': Elevation,
        'places': Places,
    },
    'mapzen': {
        'geocode': Mapzen,
        'reverse': MapzenReverse,
    },
    'komoot': {
        'geocode': Komoot,
        'reverse': KomootReverse,
    },
    'tamu': {
        'geocode': Tamu
    },
    'geocodefarm': {
        'geocode': GeocodeFarm,
        'reverse': GeocodeFarmReverse,
    },
    'uscensus': {
        'geocode': USCensus,
        'reverse': USCensusReverse,
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

    :param location: (min 2x locations) Your search location you want geocoded.
    :param units: (default=kilometers) Unit of measurement.
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

    :param location: Your search location you want geocoded.
    :param method: (default=geocode) Use the following:
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

    :param location: Your search location you want geocoded.
    :param proximity: Search nearby [lat, lng]
    :param method: (default=geocode) Use the following:
        > geocode
        > reverse
        > batch
    """
    return get(location, provider='mapbox', **kwargs)


def yandex(location, **kwargs):
    """Yandex Provider

    :param location: Your search location you want geocoded.
    :param lang: Chose the following language:
        > ru-RU — Russian (by default)
        > uk-UA — Ukrainian
        > be-BY — Belarusian
        > en-US — American English
        > en-BR — British English
        > tr-TR — Turkish (only for maps of Turkey)
    :param kind: Type of toponym (only for reverse geocoding):
        > house - house or building
        > street - street
        > metro - subway station
        > district - city district
        > locality - locality (city, town, village, etc.)
    """
    return get(location, provider='yandex', **kwargs)


def w3w(location, **kwargs):
    """what3words Provider

    :param location: Your search location you want geocoded.
    :param key: W3W API key.
    :param method: Chose a method (geocode, method)
    """
    return get(location, provider='w3w', **kwargs)


def baidu(location, **kwargs):
    """Baidu Provider

    :param location: Your search location you want geocoded.
    :param key: Baidu API key.
    :param referer: Baidu API referer website.
    """
    return get(location, provider='baidu', **kwargs)


def komoot(location, **kwargs):
    """Ottawa Provider

    :param location: Your search location you want geocoded.
    """
    return get(location, provider='komoot', **kwargs)


def ottawa(location, **kwargs):
    """Ottawa Provider

    :param location: Your search location you want geocoded.
    """
    return get(location, provider='ottawa', **kwargs)


def elevation(location, **kwargs):
    """Elevation - Google Provider

    :param location: Your search location you want to retrieve elevation data.
    """
    return get(location, method='elevation', provider='google', **kwargs)


def places(location, **kwargs):
    """Places - Google Provider

    :param location: Your search location you want geocoded.
    """
    return get(location, method='places', provider='google', **kwargs)


def timezone(location, **kwargs):
    """Timezone - Google Provider

    :param location: Your search location you want to retrieve timezone data.
    :param timestamp: Define your own specified time to calculate timezone.
    """
    return get(location, method='timezone', provider='google', **kwargs)


def reverse(location, provider="google", **kwargs):
    """Reverse Geocoding

    :param location: Your search location you want to reverse geocode.
    :param key: (optional) use your own API Key from Bing.
    :param provider: (default=google) Use the following:
        > google
        > bing
    """
    return get(location, method='reverse', provider=provider, **kwargs)


def bing(location, **kwargs):
    """Bing Provider

    :param location: Your search location you want geocoded.
    :param key: (optional) use your own API Key from Bing.
    :param method: (default=geocode) Use the following:
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

    :param location: Your search location you want geocoded.
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

    :param location: Your search location you want geocoded.
    :param app_code: (optional) use your own Application Code from HERE.
    :param app_id: (optional) use your own Application ID from HERE.
    :param method: (default=geocode) Use the following:
        > geocode
        > reverse
    """
    return get(location, provider='here', **kwargs)


def nokia(location, **kwargs):
    """HERE Provider

    :param location: Your search location you want geocoded.
    :param app_code: (optional) use your own Application Code from HERE.
    :param app_id: (optional) use your own Application ID from HERE.
    :param method: (default=geocode) Use the following:
        > geocode
        > reverse
    """
    return get(location, provider='here', **kwargs)


def tomtom(location, **kwargs):
    """TomTom Provider

    :param location: Your search location you want geocoded.
    :param key: (optional) use your own API Key from TomTom.
    """
    return get(location, provider='tomtom', **kwargs)


def mapquest(location, **kwargs):
    """MapQuest Provider

    :param location: Your search location you want geocoded.
    :param key: (optional) use your own API Key from MapQuest.
    :param method: (default=geocode) Use the following:
        > geocode
        > reverse
    """
    return get(location, provider='mapquest', **kwargs)


def osm(location, **kwargs):
    """OSM Provider

    :param location: Your search location you want geocoded.
    :param url: Custom OSM Server URL location
               (ex: http://nominatim.openstreetmap.org/search)
    """
    return get(location, provider='osm', **kwargs)


def maxmind(location='me', **kwargs):
    """MaxMind Provider

    :param location: Your search IP Address you want geocoded.
    :param location: (optional) if left blank will return your
                                current IP address's location.
    """
    return get(location, provider='maxmind', **kwargs)


def ipinfo(location='', **kwargs):
    """IP Info.io Provider

    :param location: Your search IP Address you want geocoded.
    :param location: (optional) if left blank will return your
                                current IP address's location.
    """
    return get(location, provider='ipinfo', **kwargs)


def freegeoip(location, **kwargs):
    """FreeGeoIP Provider

    :param location: Your search IP Address you want geocoded.
    :param location: (optional) if left blank will return your
                                current IP address's location.
    """
    return get(location, provider='freegeoip', **kwargs)


def ip(location, **kwargs):
    """IP Address lookup

    :param location: Your search IP Address you want geocoded.
    :param location: (optional) if left blank will return your
                                current IP address's location.
    """
    return get(location, provider='ipinfo', **kwargs)


def canadapost(location, **kwargs):
    """CanadaPost Provider

    :param ``location``: Your search location you want geocoded.
    :param ``key``: (optional) API Key from CanadaPost Address Complete.
    :param ``language``: (default=en) Output language preference.
    :param ``country``: (default=ca) Geofenced query by country.
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
    :param ``username``: (required) needs to be passed with each request.
    """
    return get(location, provider='geonames', **kwargs)


def mapzen(location, **kwargs):
    """Mapzen Provider

    :param ``location``: Your search location you want geocoded.
    """
    return get(location, provider='mapzen', **kwargs)


def tamu(location, **kwargs):
    """TAMU Provider

    Params
    ------
    :param location: The street address of the location you want geocoded.
    :param city: The city of the location to geocode.
    :param state: The state of the location to geocode.
    :param zipcode: The zipcode of the location to geocode.
    :param key: The API key (use API key "demo" for testing).

    API Reference
    -------------
    https://geoservices.tamu.edu/Services/Geocode/WebService
    """
    return get(location, provider='tamu', **kwargs)


def geocodefarm(location, **kwargs):
    """GeocodeFarm Provider

    Params
    ------
    :param location: The string to search for. Usually a street address.
    :param key: (optional) API Key. Only Required for Paid Users.
    :param lang: (optional) 2 digit language code to return results in. Currently only "en"(English) or "de"(German) supported.
    :param country: (optional) The country to return results in. Used for biasing purposes and may not fully filter results to this specific country.

    API Reference
    -------------
    https://geocode.farm/geocoding/free-api-documentation/
    """
    return get(location, provider='geocodefarm', **kwargs)


def tgos(location, **kwargs):
    """TGOS Provider

    :param location: Your search location you want geocoded.
    :param language: (default=taiwan) Use the following:
        > taiwan
        > english
        > chinese
    :param method: (default=geocode) Use the following:
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
    :param location: Your search location you want geocoded.
    :param benchmark: (default=4) Use the following:
        > Public_AR_Current or 4
        > Public_AR_ACSYYYY or 8
        > Public_AR_Census2010 or 9
    :param vintage: (default=4) Use the following:
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
    :param method: (default=geocode) Use the following:
        > geocode
        > reverse

    API Reference
    -------------
    https://geocoding.geo.census.gov/geocoder/Geocoding_Services_API.pdf
    """
    return get(location, provider='uscensus', **kwargs)
