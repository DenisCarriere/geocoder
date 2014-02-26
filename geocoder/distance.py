# -*- coding: utf-8 -*-

from google import Google
from geocoder import Geocoder
from haversine import haversine

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
		self.location1 = location1
		self.location2 = location2

		# Check the input values of the locations
		self.lat1, self.lng1 = self.check_input(location1)
		self.lat2, self.lng2 = self.check_input(location2)

		# Calculate Distance
		self.calculate_distance()

		# Add address from Geocoder Class
		self.add_address()

	def __repr__(self):
		return '<Distance - {0} to {1} [{2}km]>'.format(self.location1, self.location2, self.km)

	def convert_float(self, number):
		try:
			return float(number)
		except ValueError:
			print '<ERROR - Distance tool - Input not a number>'
			return None

	def check_input(self, location):
		lat, lng = 0.0, 0.0

		# Checking for a String
		if isinstance(location, str):
			lat, lng = Geocoder(Google(location)).latlng

		# Checking for List of Tuple
		if isinstance(location, (list, tuple)):
			lat, lng = self.check_for_list(location)

		# Checking for Dictionary
		elif isinstance(location, dict):
			lat, lng = self.check_for_dict(location)

		# Checking for a Geocoder Class
		elif hasattr(location, 'latlng'):
			lat, lng = location.latlng

		# Return Results
		return lat, lng

	def check_for_list(self, location):
		# Standard LatLng list or tuple with 2 number values
		if len(location) == 2:
			lat = self.convert_float(location[0])
			lng = self.convert_float(location[1])
			if bool(lat and lng):
				return lat, lng

	def check_for_dict(self, location):
		# Standard LatLng list or tuple with 2 number values
		if bool('lat' in location and 'lng' in location):
			lat = self.convert_float(location.get('lat'))
			lng = self.convert_float(location.get('lng'))
			if bool(lat and lng):
				return lat, lng

	def calculate_distance(self):
		if bool(self.lat1 and self.lng1 and self.lat2 and self.lng2):
			self.ok = True

			latlng1 = (self.lat1, self.lng1) 
			latlng2 = (self.lat2, self.lng2)
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
