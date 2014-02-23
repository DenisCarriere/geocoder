# -*- coding: utf-8 -*-

try:
	import requests
except:
	print 'Need to install Requests Module'
	
import sys


class Geocoder(object):
	def __init__(self, provider):
		self.provider = provider
		self.name = provider.name

		# Functions
		self.connect()
		self.add_data()

	def __repr__(self):
		return '<[{status}] Geocoder {name} [{address}]>'.format(status=self.status, name=self.name, address=self.address)

	def connect(self):
		""" Requests the Geocoder's URL with the Address as the query """
		self.url = ''
		self.status = 404

		headers = dict()
		headers['Referer'] = 'http://www.mapquestapi.com/geocoding/'
		headers['Accept-Language'] = 'en-US,en;q=0.8,fr-CA;q=0.6,fr;q=0.4'
		headers['User-Agent'] = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64;'
		
		try:
			r = requests.get(self.provider.url, params=self.provider.params, headers=headers, timeout=5.0)
			self.url = r.url
			self.status = r.status_code
		except KeyboardInterrupt:
			sys.exit()
		except:
			self.status = 'ERROR - URL Connection'

		if self.status == 200:
			self.provider.load(r.json())
			
	def add_data(self):
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
		self.north = self.provider.north
		self.east = self.provider.east
		self.northeast = self.provider.northeast

		# Build JSON
		self.json = self.build_json()

	def build_json(self):
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

		return json

	def debug(self):
		print '============'
		print 'Debug Geocoder'
		print '-------------'
		print 'Provider:', self.name
		print 'Address: ', self.address
		print 'Location:', self.location
		print 'Lat:', self.lat
		print 'Lng:', self.lng
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
	"""
	Providers
	=========
	Google
	Bing
	TomTom
	Mapquest
	Nokia
	Esri
	OSM
	Maxmind
	"""

	from osm import Osm

	location = 'Ottawa Ontario'
	lat = 45.5375801
	lng = -75.2465979
	
	g = Geocoder(Osm(location))
	print g.debug()

