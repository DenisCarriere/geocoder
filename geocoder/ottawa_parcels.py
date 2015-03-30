import requests

url = 'http://maps.ottawa.ca/arcgis/rest/services/Property_Parcels/MapServer/find'
params = {
    'searchText': '453 Booth',
    'layers': 0,
    'f': 'json',
    'sr': 4326,
}


#returnZ=false&returnM=false&gdbVersion=&f=json
r = requests.get(url, params=params)
content = r.json()
if content:
    results = content['results'][0]
    address_id = results['attributes']['PI Municipal Address ID']
    params = {
        'searchText': address_id,
        'layers': 2,
        'f': 'json',
        'sr': 4326,
    }

    r = requests.get(url, params=params)
    import json
    print(json.dumps(r.json(), indent=4))
