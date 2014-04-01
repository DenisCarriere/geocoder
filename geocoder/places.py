import geocoder
import requests
import sys

g = geocoder.google('Kabul, Afghanistan')
latlng = '{0},{1}'.format(g.y, g.x)

url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
params = dict()
params['location'] = latlng
params['radius'] = 5000
params['keyword']='Mosque'
params['sensor'] = 'false'
params['key'] = 'AIzaSyCz6Gp5fQexBVxhMGoW2l_YlbQk-tFLCVE'


r = requests.get(url, params=params)

for item in r.json():
	print item
	
sys.exit()
results = r.json()['results']
for item in results:
	name = item['name'].encode('utf-8')
	location = item['geometry']['location']
	lat, lng = location['lat'], location['lng']
	spaces = ' ' * (40 - len(name))
	print '{0} {1}({2}, {3})'.format(name, spaces, lat, lng)