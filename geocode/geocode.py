# -*- coding: utf-8 -*-

import requests
import simplejson as json
import re


class Source(object):
	""" Template for Source """
	allow_proxies = False
	x = 0.0
	y = 0.0
	west = 0.0
	north = 0.0
	south = 0.0
	east = 0.0

	def __repr__(self):
		return "<Source {0}>".format(self.name)

	def load(self, json, last=''):
		# DICTIONARY
		if type(json) == type(dict()):
			for keys, values in json.items():
				# MAXMIND
				if 'geoname_id' in json:
					names = json.get('names')
					self.json[last] = names['en']

				# GOOGLE
				if keys == 'address_components':
					for item in values:
						long_name = item.get('long_name')
						all_types = item.get('types')
						for types in all_types:
							self.json[types] = long_name
				if keys == 'types':
					for item in values:
						name = 'types_{0}'.format(item)
						self.json[name] = True

				# LIST
				elif type(values) == type(list()):
					if len(values) == 1:
						self.load(values[0], keys)
					elif len(values) > 1:
						count = 0
						for value in values:
							name = '{0}-{1}'.format(keys, count)
							self.load(value, name)
							count += 1
				# DICTIONARY
				elif type(values) == type(dict()):
					self.load(values, keys)
				else:
					if last:
						name = last + '-' + keys
					else:
						name = keys
					self.json[name] = values
		# LIST
		elif type(json) == type(list()):
			if json:
				self.load(json[0], last)
		# OTHER Formats
		else:
			self.json[last] = json

	def safe_postal(self, item):
		pattern = re.compile(r'[A-Z]{1}[0-9]{1}[A-Z]{1}[ ]?[0-9]?[A-Z]?[0-9]?')
		if item:
			match = pattern.search(item)

			# Canada Pattern
			if match:
				return match.group()
			else:
				# United States Pattern
				pattern = re.compile(r'[0-9]{4}[0-9]?')
				match = pattern.search(item)
				if match:
					return match.group()	
		return ''

	def safe_format(self, item):
		item = self.json.get(item)
		if item:
			return item.encode('utf8')

	def safe_coord(self, item):
		item = self.json.get(item)
		if item:
			try:
				return float(item)
			except:
				return 0.0
		else:
			return 0.0

	def safe_bbox(self, southwest, northeast):
		# South Latitude, West Longitude, North Latitude, East Longitude
		if southwest:
			if southwest[0]:
				self.south = float(southwest[0]) 
				self.west = float(southwest[1])
				self.north = float(northeast[0])
				self.east = float(northeast[1])
				return [(self.south, self.west), (self.north, self.east)]
			else:
				return [(0.0, 0.0), (0.0, 0.0)]

	def ok(self):
		if self.lat():
			return True
		else:
			return False

	def status(self):
		if self.lng():
			return 'OK'
		else:
			return 'ERROR - No Geometry'

	def bbox(self):
		return [(0.0, 0.0), (0.0, 0.0)]

	def quality(self):
		return ''

	def postal(self):
		return ''

class MaxMind(Source):
	name ='maxmind'
	allow_proxies = False

	def __init__(self, location):
		self.url = 'http://www.maxmind.com/geoip/v2.0/city_isp_org/{ip}'.format(ip=location)
		self.json = dict()
		self.params = dict()
		self.params['demo'] = 1

	def lat(self):
		return self.json.get('location-latitude')

	def lng(self):
		return self.json.get('location-longitude')

	def address(self):
		city = self.json.get('city')
		province = self.json.get('subdivisions')
		country = self.json.get('country')
		if city:
			return '{0}, {1} {2}'.format(city, province, country)
		elif province:
			return '{0}, {1}'.format(province, country)
		elif country:
			return '{0}'.format(country)
		else:
			return ''

	def quality(self):
		return self.json.get('traits-isp')


class Geolytica(Source):
	name = 'geolytica'
	url = 'http://geocoder.ca/'
	allow_proxies = True

	def __init__(self, location):
		self.json = dict()
		self.params = dict()
		self.params['locate'] = location
		self.params['jsonp'] = 1
		self.params['geoit'] = 'xml'
		self.params['callback'] = 'Results'

	def lat(self):
		return self.safe_coord('latt')

	def lng(self):
		return self.safe_coord('longt')

	def address(self):
		street_number = self.json.get('standard-stnumber')
		street_name = self.json.get('standard-staddress')
		city = self.json.get('standard-city')
		province = self.json.get('standard-prov')
		street_full = ''
		area = ''

		if street_number and street_name:
			street_full = '{0} {1}'.format(street_number, street_name.strip().title())	

		if city and province:
			area = '{0} {1}'.format(city, province)

		if street_full and area:
			return '{0}, {1}'.format(street_full, area).encode('utf8')
		elif street_full:
			return street_full.encode('utf8')
		elif area:
			return area.encode('utf8')
		else:
			return ''

	def postal(self):
		return self.json.get('postal')


class Esri(Source):
	name = 'esri'
	url = 'http://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/find'
	allow_proxies = True

	def __init__(self, location, country='CAN'):
		self.json = dict()
		self.params = dict()
		self.params['text'] = location
		self.params['f'] = 'pjson'
		self.params['sourceCountry'] = country

	def lat(self):
		return self.json.get('geometry-y')

	def lng(self):
		return self.json.get('geometry-x')

	def address(self):
		return self.safe_format('locations-name')

	def quality(self):
		return self.json.get('attributes-Addr_Type')

	def postal(self):
		return self.safe_postal(self.address())

	def bbox(self):
		southwest = self.json.get('extent-ymin'), self.json.get('extent-xmin')
		northeast = self.json.get('extent-ymax'), self.json.get('extent-xmax')
		return self.safe_bbox(southwest, northeast)


class Nokia(Source):
	name = 'nokia'
	url = 'http://geocoder.cit.api.here.com/6.2/geocode.json'
	app_id = '6QqTvc3kUWsMjYi7iGRb'
	app_code = 'q7R__C774SunvWJDEiWbcA'

	def __init__(self, location):
		self.json = dict()
		self.params = dict()
		self.params['searchtext'] = location
		self.params['app_id'] = self.app_id
		self.params['app_code'] = self.app_code
		self.params['gen'] = 3

	def lat(self):
		return self.json.get('NavigationPosition-Latitude')

	def lng(self):
		return self.json.get('NavigationPosition-Longitude')

	def address(self):
		return self.safe_format('Address-Label')

	def quality(self):
		return self.json.get('Result-MatchType')

	def postal(self):
		return self.json.get('Address-PostalCode')

	def bbox(self):
		southwest = self.json.get('BottomRight-Latitude'), self.json.get('TopLeft-Longitude')
		northeast = self.json.get('TopLeft-Latitude'), self.json.get('BottomRight-Longitude')
		return self.safe_bbox(southwest, northeast)

class Google(Source):
	name = 'google'
	url = 'http://maps.googleapis.com/maps/api/geocode/json'
	allow_proxies = True

	def __init__(self, location):
		self.json = dict()
		self.params = dict()
		self.params['sensor'] = 'false'
		self.params['address'] = location

	def lat(self):
		return self.json.get('location-lat')

	def lng(self):
		return self.json.get('location-lng')

	def address(self):
		return self.safe_format('results-formatted_address')

	def status(self):
		return self.json.get('status')

	def quality(self):
		return self.json.get('geometry-location_type')

	def postal(self):
		return self.json.get('postal_code')

	def bbox(self):
		southwest = self.json.get('southwest-lat'), self.json.get('southwest-lng')
		northeast = self.json.get('northeast-lat'), self.json.get('northeast-lng')
		return self.safe_bbox(southwest, northeast)


class Mapquest(Source):
	name = 'mapquest'
	url = 'http://www.mapquest.ca/_svc/searchio'

	def __init__(self, location):
		self.json = dict()
		self.params = dict()
		self.params['query0'] = location
		self.params['action'] = 'search'
		#self.params['thumbMaps'] = False

	def lat(self):
		return self.json.get('latLng-lat')

	def lng(self):
		return self.json.get('latLng-lng')

	def address(self):
		return self.safe_format('address-singleLineAddress')

	def quality(self):
		return self.json.get('address-geocodeQualityCode')

	def postal(self):
		return self.json.get('address-postalCode')


class OSM(Source):
	name = 'osm'
	url = 'http://nominatim.openstreetmap.org/search'

	def __init__(self, location):
		self.json = dict()
		self.params = dict()
		self.params['format'] = 'json'
		self.params['q'] = location

	def lat(self):
		return self.safe_coord('lat')
		
	def lng(self):
		return self.safe_coord('lon')

	def address(self):
		return self.safe_format('display_name')

	def quality(self):
		return self.json.get('type')

	def postal(self):
		return self.safe_postal(self.address())

	def bbox(self):
		southwest = self.json.get('boundingbox-0'), self.json.get('boundingbox-2')
		northeast = self.json.get('boundingbox-1'), self.json.get('boundingbox-3')
		return self.safe_bbox(southwest, northeast)

class Bing(Source):
	name = 'bing'
	key = 'AtnSnX1rEHr3yTUGC3EHkD6Qi3NNB-PABa_F9F8zvLxxvt8A7aYdiG3bGM_PorOq'
	url = 'http://dev.virtualearth.net/REST/v1/Locations'

	def __init__(self, location):
		self.params = dict()
		self.json = dict()
		self.params['key'] = self.key
		self.params['q'] = location

	def lat(self):
		return self.json.get('coordinates-0')

	def lng(self):
		return self.json.get('coordinates-1')

	def address(self):
		return self.safe_format('address-formattedAddress')

	def status(self):
		return self.json.get('statusDescription')

	def quality(self):
		if self.json.get('matchCodes'):
			return self.json.get('matchCodes')
		else:
			return self.json.get('matchCodes-0')

	def postal(self):
		return self.json.get('address-postalCode')

	def bbox(self):
		southwest = self.json.get('bbox-0'), self.json.get('bbox-1')
		northeast = self.json.get('bbox-2'), self.json.get('bbox-3')
		return self.safe_bbox(southwest, northeast)

class Geocode(object):
	""" Goeocode API
		geocode = Geocode('1552 Payette dr., Ottawa ON')
		x, y = geocode.xy
	"""
	url = ''
	postal = ''
	quality = ''

	def __init__(self, location, source='google', proxy=''):
		self.name = 'Geocode'
		self.proxy = proxy
		self.location = location
		self.raw = {}

		# Functions
		self.source = self.source(source)
		self.connect()
		self.add_formats()

	def __repr__(self):
		address = self.source.address()
		if not address:
			address = self.location
		return '<[{status}] {name} {source} [{address}]>'.format(status=self.status, name=self.name, source=self.source.name, address=address)

	def source(self, source):
		source = source.lower()
		if source in ['google']:
			return Google(self.location) 
		elif source in ['esri', 'arcgis']:
			return Esri(self.location)
		elif source in ['osm']:
			return OSM(self.location)
		elif source in ['bing', 'microsoft']:
			return Bing(self.location)
		elif source in ['nokia']:
			return Nokia(self.location)
		elif source in ['geolytica']:
			return Geolytica(self.location)
		elif source in ['mapquest']:
			return Mapquest(self.location)
		elif source in ['maxmind']:
			return MaxMind(self.location)

	def debug(self, full=True):
		print '============'
		print 'Debug Geocode'
		print '-------------'
		print 'Source:', self.source.name
		print 'Address:', self.source.address()
		print 'Address2:', self.location
		print 'LatLng:', [self.source.lat(), self.source.lng()]
		print 'Bbox:', self.bbox
		print 'South-West:', self.south, self.west
		print 'North-East:', self.north, self.east
		print 'OK:', self.source.ok()
		print 'Status:', self.source.status()
		print 'Quality:', self.source.quality()
		print 'Postal:', self.source.postal()
		print 'Url:', self.url
		print 'Proxies:', self.proxy
		print '============'
		print 'JSON Objects'
		print '------------'
		if full:
			for item in self.source.json.items():
				print item

	def connect(self):
		""" Requests the Geocode's URL with the Address as the query """
		try:
			if not self.source.allow_proxies:
				self.proxy = ''
			#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:9.0.1) Gecko/20100101 Firefox/9.0.1'}
			r = requests.get(self.source.url, params=self.source.params, proxies=self.proxy, timeout=5.0)
			self.url = r.url
			self.status = r.status_code
		except KeyboardInterrupt:
			sys.exit()
		except:
			self.status = 'ERROR - URL Connection'

		if self.status == 200:
			# Geolytica Exceptions (JSON corrupted & Query over limits)
			prefix = 'Results('
			suffix = ');'
			if r.content.startswith(prefix) and r.content.endswith(suffix):
				self.json = json.loads(r.content[len(prefix):-len(suffix)])
			elif '<code>006</code>' in r.content:
				self.status = 'OVER_QUERY_LIMIT'
			else:
				# Loading standard JSON data
				if r.content:
					try:
						self.json = r.json()
					except:
						self.status = 'ERROR - JSON corrupt'
				else:
					self.status = 'ERROR - No content'

			if self.status == 200:
				self.raw = self.json
				self.source.load(self.json)
				self.json = self.source.json
				self.ok = self.source.ok()
				self.status = self.source.status()

				if self.ok:
					self.x = self.source.lng()
					self.y = self.source.lat()

				# Remove List from Raw JSON
				if type(list()) == type(self.raw):
					if self.raw:
						self.raw = self.raw[0]
				if not self.raw:
					self.raw = dict()

	def add_formats(self):
		# Geometry
		self.x, self.y = self.source.x, self.source.y
		x, y = self.x, self.y
		self.lng, self.longitude = x, x
		self.lat, self.latitude = y, y
		self.latlng = [self.lat, self.lng]
		self.xy = [x, y]
		self.bbox = self.source.bbox()

		self.south = self.source.south
		self.west = self.source.west
		self.north = self.source.north
		self.east = self.source.east

		# Address
		try:
			self.address = self.source.address()
		except:
			self.address = self.source.address()

		self.postal = self.source.postal()

		# Quality Control
		self.quality = self.source.quality()

	def row(self):
		row = dict()
		row['x'] = self.x
		row['y'] = self.y
		row['address'] = self.address
		row['status'] = self.status
		row['quality'] = self.quality
		row['postal'] = self.postal
		row['source'] = self.source.name
		row['bbox'] = self.bbox
		return row

def test(location):
	Geocode(location, source='google').debug()
	Geocode(location, source='bing').debug()
	Geocode(location, source='nokia').debug()
	Geocode(location, source='mapquest').debug()
	Geocode(location, source='osm').debug()
	Geocode(location, source='geolytica').debug()
	Geocode(location, source='esri').debug()

if __name__ == '__main__':
	"""
	Providers
	=========
	google
	esri
	bing
	osm
	mapquest
	geolytica
	nokia
	"""

	location = '1552 Payette dr. Ottawa, ON, Canada'
	location = 'Bay Street, New York City, NY'
	location = '10.87.78.208'
	Geocode(location, source='maxmind').debug()
	
	#test(location)

