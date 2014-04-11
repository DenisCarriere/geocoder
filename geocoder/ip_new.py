import requests

params = dict()
ip  = '68.69.18.130'
params['showDetails'] = 'true'
params['showARIN'] = 'true'
#url = 'http://whois.arin.net/rest/nets;q={0}'.format(ip)
url = 'http://whois.arin.net/rest/ip/{0}'.format(ip)

headers = dict()
headers['Accept'] = 'application/json'

r = requests.get(url, params=params, headers=headers)

print r.json()