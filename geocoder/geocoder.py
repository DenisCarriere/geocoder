# -*- coding: utf-8 -*-

import requests
import sys


class Geocoder(object):
    """
    geocoder object
    ~~~~~~~~~~~~~~~
    >>> g = geocoder.google('1600 Amphitheatre Pkwy, Mountain View, CA')
    >>> g.latlng
    (37.784173, -122.401557)
    >>> g.country
    'United States'
    """
    def __init__(self, provider, proxies, timeout):
        self.provider = provider
        self.proxies = proxies
        self.timeout = timeout
        self.name = provider.name

        # Connecting to HTTP provider
        self._get_proxies()
        self._get_timeout()
        self._connect()
        self._add_data()

    def __repr__(self):
        return '<[{0}] Geocoder {1} [{2}]>'.format(self.status, self.name, self.address)

    def _get_proxies(self):
        if self.proxies:
            if isinstance(self.proxies, str):
                if 'http://' not in self.proxies:
                    name = 'http://{0}'.format(self.proxies)
                self.proxies = {'http': name}
        else:
            self.proxies = {}

    def _get_timeout(self):
        if isinstance(self.timeout, int):
            self.timeout = float(self.timeout)

    def _connect(self):
        """ Requests the Geocoder's URL with the Address as the query """
        self.url = ''
        self.status = 404
        try:
            r = requests.get(
                self.provider.url,
                params=self.provider.params,
                headers=self.provider.headers,
                timeout=self.timeout,
                proxies=self.proxies
            )
            self.url = r.url
            self.status = r.status_code
        except KeyboardInterrupt:
            sys.exit()
        except:
            self.status = 'ERROR - URL Connection'

        if self.status == 200:
            self.provider.load(r.json())
            self.status = self.provider.status()

    def _add_data(self):
        # Get Attributes
        self.quality = self.provider.quality()
        self.location = self.provider.location
        self.x = self.provider.lng()
        self.y = self.provider.lat()
        self.ok = self.provider.ok()
        self.address = self.provider.address()
        self.postal = self.provider.postal()
        self.quality = self.provider.quality()

        # Administrative Fields
        self.city = self.provider.city()
        self.state = self.provider.state()
        self.province = self.state
        self.country = self.provider.country()

        # More ways to spell X.Y
        x, y = self.x, self.y
        self.lng, self.longitude = x, x
        self.lat, self.latitude = y, y
        self.latlng = self.lat, self.lng
        self.xy = x, y

        # Bounding Box - SouthWest, NorthEast - [y1, x1, y2, x2]
        self.bbox = self.provider.bbox()
        self.south = self.provider.south
        self.west = self.provider.west
        self.southwest = self.provider.southwest
        self.southeast = self.provider.southeast
        self.north = self.provider.north
        self.east = self.provider.east
        self.northeast = self.provider.northeast
        self.northwest = self.provider.northwest

        # Population Field (integer)
        self.population = self.provider.population()
        self.pop = self.population

        # IP Address
        self.ip = self.provider.ip()

        # Build JSON
        self.json = self._build_json()
        self.geojson = self._build_geojson()

    def _build_json(self):
        json = dict()
        json['provider'] = self.name
        json['location'] = self.location
        json['ok'] = self.ok
        json['status'] = self.status

        if self.postal:
            json['postal'] = self.postal

        if self.address:
            json['address'] = self.address

        if self.ok:
            json['quality'] = self.quality
            json['lng'] = self.x
            json['lat'] = self.y

        if self.bbox:
            json['bbox'] = self.bbox

        if self.country:
            json['country'] = self.country

        if self.state:
            json['state'] = self.state

        if self.city:
            json['city'] = self.city

        if self.population:
            json['population'] = self.population

        if self.ip:
            json['ip'] = self.ip

        return json

    def _build_geojson(self):
        geojson = dict()
        geojson['type'] = 'Feature'
        geojson['geometry'] = {'type':'Point', 'coordinates': [self.lng, self.lat]}
        geojson['properties'] = self.json
        return geojson


    def debug(self):
        print '============'
        print 'Debug Geocoder'
        print '-------------'
        print 'Provider:', self.name
        print 'Address: ', self.address
        print 'Location:', self.location
        print 'Lat & Lng:', self.latlng
        print 'Bbox:', self.bbox
        print 'OK:', self.ok
        print 'Status:', self.status
        print 'Quality:', self.quality
        print 'Postal:', self.postal
        print 'Country:', self.country
        print 'City:', self.city
        print 'Url:', self.url
        print 'Proxies:', self.proxies
        print '============'
        print 'JSON Objects'
        print '------------'
        for item in self.provider.json.items():
            print item

if __name__ == '__main__':
    from geonames import Geonames
    from reverse import Reverse
    location = 'Springfield, Virginia'
    lat = 45.5375801
    lng = -75.2465979

    g = Geocoder(Reverse((lat, lng)))
    print g
