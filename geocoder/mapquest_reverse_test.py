import requests


headers = {
    'referer':'http://www.mapquestapi.com/geocoding/',
    'host': 'www.mapquestapi.com',
    }

params = {
    'key': 'Kmjtd|luua2qu7n9,7a=o5-lzbgq',
    'callback':'renderReverse',
    'location': '40.053116,-76.313603',
    }

url = 'http://www.mapquestapi.com/geocoding/v1/reverse'

r = requests.get(url, params=params, headers=headers)
print r.content


r = requests.get('http://www.mapquestapi.com/media/js/config_key.js')
print r.content