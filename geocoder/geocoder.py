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

    Attributes
    ~~~~~~~~~~
    - address
    - location
    - city
    - country
    - postal
    - quality
    - status
    - ok (boolean)
    - x, lng, longitude (float)
    - y, lat, latitude (float)
    - latlng, xy (tuple)
    - bbox {southwest, northeast}
    - southwest {lat, lng}
    - northeast {lat, lng}
    - south, west, north, east (float)
    """
    def __init__(self, provider):
        self.provider = provider
        self.name = provider.name

        # Connecting to HTTP provider
        self._connect()
        self._add_data()

    def __repr__(self):
        name = '<[{0}] Geocoder {1} [{2}]>'
        return name.format(self.status, self.name, self.address)

    def _connect(self):
        """ Requests the Geocoder's URL with the Address as the query """
        self.url = ''
        self.status = 404

        try:
            r = requests.get(
                self.provider.url,
                params=self.provider.params,
                timeout=5.0,
                headers=self.provider.headers
            )
            self.url = r.url
            self.status = r.status_code
        except KeyboardInterrupt:
            sys.exit()
        except:
            self.status = 'ERROR - URL Connection'

        if self.status == 200:
            self.provider.load(r.json())

    def _add_data(self):
        # Get Attributes
        self.status = self.provider.status()
        self.quality = self.provider.quality()
        self.location = self.provider.location
        self.x = self.provider.lng()
        self.y = self.provider.lat()
        self.ok = self.provider.ok()
        self.address = self.provider.address()
        self.postal = self.provider.postal()
        self.quality = self.provider.quality()

        # Extra Fields
        self.country = self.provider.country()
        self.city = self.provider.city()

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

        # Build JSON
        self.json = self._build_json()

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

        if self.city:
            json['city'] = self.city

        if self.population:
            json['population'] = self.population

        return json

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
