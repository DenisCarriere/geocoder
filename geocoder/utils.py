#!/usr/bin/python
# coding: utf8

import api
from keys import *
from geocoder import Geocoder
from ip import Ip
from osm import Osm
from bing import Bing
from nokia import Nokia
from arcgis import Arcgis
from tomtom import Tomtom
from google import Google
from reverse import Reverse
from geonames import Geonames
from mapquest import Mapquest
from timezone import Timezone
from elevation import Elevation
from geolytica import Geolytica

def get_provider(location, provider, short_name):
    provider = provider.lower()

    if provider == 'google':
        return Google(location)
    elif provider == 'bing':
        return Bing(location, key=bing_key)
    elif provider == 'osm':
        return Osm(location)
    elif provider == 'nokia':
        return Nokia(location, app_id=app_id, app_code=app_code)
    elif provider == 'mapquest':
        return Mapquest(location)
    elif provider == 'arcgis':
        return Arcgis(location)
    elif provider == 'ip':
        return Ip(location)
    elif provider == 'reverse':
        return Reverse(location)
    elif provider == 'tomtom':
        return Tomtom(location, key=tomtom_key)
    elif provider == 'geonames':
        return Geonames(location, username=username)
    elif provider == 'geolytica':
        return Geolytica(location)
    elif provider == 'elevation':
        return Elevation(location)
    elif provider == 'timezone':
        return Timezone(location)


if __name__ == "__main__":
    print get_provider("Ottawa", provider='google')