# -*- coding: utf-8 -*-

from google import Google
from geocoder import Geocoder
from haversine import haversine
from location import Location


class Distance(object):
	name = 'Distance'
	lat1 = 0.0
	lng1 = 0.0
	lat2 = 0.0
	lng2 = 0.0
	ok = False
	km = None
	miles = None

	def __init__(self, location1, location2):
		self.location1 = Location(location1)
		self.location2 = Location(location2)

		# Calculate Distance
		self.calculate_distance()

		# Add address from Geocoder Class
		self.add_address()

	def __repr__(self):
		return '<Distance - {0} to {1} [{2}km]>'.format(self.location1, self.location2, self.km)

	def calculate_distance(self):
		latlng1 = self.location1.latlng
		latlng2 = self.location2.latlng

		if bool(latlng1 and latlng2):
			self.ok = True
			self.km = haversine(latlng1, latlng2)
			self.miles = haversine(latlng1, latlng2, miles=True)
		else:
			print '<ERROR - Input is incorrect>'

	def add_address(self):
		pass
		"""
		if hasattr(self.location1, 'address'):
			self.location1 = self.location1.address
		if hasattr(self.location2, 'address'):
			self.location2 = self.location2.address
		"""


if __name__ == '__main__':
	ottawa = Geocoder(Google('Ottawa'))
	#toronto = Geocoder(Google('Toronto')).latlng

	ottawa = (45.4215296, -75.69719309999999)
	#toronto = (43.653226, -79.3831843)
	toronto = {'lat':43.653226, 'lng':-79.3831843}

	d = Distance(ottawa, toronto)
	print d
