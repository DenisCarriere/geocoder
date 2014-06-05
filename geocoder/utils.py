#!/usr/bin/python
# coding: utf8

import api

def get_provider(location, provider):
    provider = provider.lower()

    if provider == 'google':
        return api.google(location)
    elif provider == 'bing':
        return api.bing(location)
    elif provider == 'osm':
        return api.osm(location)
    elif provider == 'nokia':
        return api.nokia(location)
    elif provider == 'mapquest':
        return api.mapquest(location)
    elif provider == 'arcgis':
        return api.arcgis(location)
    elif provider == 'ip':
        return api.ip(location)
    elif provider == 'reverse':
        return api.reverse(location)
    elif provider == 'tomtom':
        return api.tomtom(location)
    elif provider == 'geonames':
        return api.geonames(location)

if __name__ == "__main__":
    print get_provider("Ottawa", provider='google')