# -*- coding: utf-8 -*-

from haversine import haversine
from location import Location


class Distance(object):
	name = 'Distance'
	ok = False
	km = None
	miles = None
	meters = None
	feet = None

	def __init__(self, location1, location2):
		self.location1 = Location(location1)
		self.location2 = Location(location2)

		# Calculate Distance
		self.calculate_distance()

	def __repr__(self):
		display = '<Distance - {0} to {1} [{2}km]>'
		return display.format(self.location1.name, self.location2.name, self.km)

	def calculate_distance(self):
		latlng1 = self.location1.latlng
		latlng2 = self.location2.latlng

		if bool(latlng1 and latlng2):
			self.ok = True
			self.km = haversine(latlng1, latlng2)
			self.miles = haversine(latlng1, latlng2, miles=True)
			self.meters = int(self.km * 1000)
			self.feet = int(self.miles * 5280)
		else:
			print '<ERROR - Input is incorrect>'


if __name__ == '__main__':
	#ottawa = Geocoder(Google('Ottawa'))
	#toronto = Geocoder(Google('Toronto')).latlng

	ottawa = (45.4215296, -75.69719309999999)
	#toronto = (43.653226, -79.3831843)
	toronto = {'lat':43.653226, 'lng':-79.3831843}

	d = Distance(ottawa, toronto, word=True)
	print d.feet
	print d.miles
	print d.meters
	print d.km
