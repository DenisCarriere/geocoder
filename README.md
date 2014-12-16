# [Geocoder](https://github.com/DenisCarriere/geocoder) [![version](https://badge.fury.io/py/geocoder.png)](http://badge.fury.io/py/geocoder) [![build](https://travis-ci.org/DenisCarriere/geocoder.png?branch=master)](https://travis-ci.org/DenisCarriere/geocoder)

### A complete Python Geocoding module made easy.

Every task is made easy with tons of ``help`` & ``debug`` commands!

```python
>>> import geocoder # pip install geocoder
>>> g = geocoder.google('<address>')
>>> g.lat, g.lng
45.413140 -75.656703
...
```

![Providers](https://pbs.twimg.com/media/Bqi8kThCUAAboo0.png)

## QuickStart

A place to get you started on how to use this module and set up your work station.

**Install from PyPi** (Tested build)
```bash
$ pip install geocoder
```

**Install from GitHub** (Latest build)
```bash
$ git clone https://github.com/DenisCarriere/geocoder.git
$ cd geocoder
$ python setup.py install
```

**Using iPython with Geocoder**
```bash
$ pip install ipython
$ ipython
```

Using the **TAB** key after entering '.' you will see all the available **providers**.

```python
>>> import geocoder
>>> g = geocoder.
geocoder.api             geocoder.geolytica       geocoder.mapquest
geocoder.arcgis          geocoder.geonames        geocoder.nokia
geocoder.base            geocoder.get             geocoder.osm
geocoder.bing            geocoder.google          geocoder.timezone
geocoder.canadapost      geocoder.ip              geocoder.yahoo
geocoder.cli             geocoder.keys            geocoder.tomtom
geocoder.elevation       geocoder.location 
...       
```

Using the **TAB** key again, you can see all the available **attributes**.

```python
>>> g = geocoder.google('Ottawa')
>>> g.
g.accuracy            g.latlng              g.south
g.address             g.lng                 g.southeast
g.api                 g.locality            g.southwest
g.attributes          g.location            g.state
g.bbox                g.neighborhood        g.status
g.content             g.north               g.status_code
g.country             g.northeast           g.status_description
g.county              g.northwest           g.street_number
g.debug               g.ok                  g.sublocality
g.east                g.params              g.subpremise
g.error               g.parse               g.url
g.geometry            g.postal              g.west
g.headers             g.provider            g.wkt
g.help                g.quality             g.x
g.json                g.route               g.y
g.lat                 g.short_name
...    
```

## Command Line Interface

The command line tool allows you to geocode one or many strings, either
passed as an argument, passed via STDIN, or contained in a referenced file.

```bash
$ geocode "Ottawa"
{
  "accuracy": "Rooftop",
  "quality": "PopulatedPlace",
  "lng": -75.68800354003906,
  "status": "OK",
  "locality": "Ottawa",
  "country": "Canada",
  "provider": "bing",
  "state": "ON",
  "location": "Ottawa",
  "address": "Ottawa, ON",
  "lat": 45.389198303222656
}
```

Now, suppose you have a file with two lines, which you want to geocode.

```bash
$ geocode `textfile.txt`
{"status": "OK", "locality": "Ottawa", ...}
{"status": "OK", "locality": "Boston", ...}
```

The output is, by default, sent to stdout, so it can be conveniently parsed
by json parsing tools like `jq`.

```bash
$ geocode `textfile.txt` | jq [.lat,.lng,.country] -c
[45.389198303222656,-75.68800354003906,"Canada"]
[42.35866165161133,-71.0567398071289,"United States"]
```

Parsing a batch geocode to CSV can also be done with `jq`. Build your headers first then run the `geocode` application.

```bash
$ echo 'lat,lng,locality' > test.csv
$ geocode cities.txt | jq [.lat,.lng,.locality] -c | jq -r '@csv' >> test.csv
```

Make the output look **--pretty**!

```bash
$ geocode "Ottawa, Ontario" --pretty
{
    "status": "OK", 
    "city": "Ottawa", 
    "country": "Canada", 
    "provider": "bing", 
    "location": "Ottawa Ontario", 
    "state": "ON", 
    "bbox": {
        "northeast": [
            45.77197265625, 
            -74.90253448486328
        ], 
        "southwest": [
            45.07920837402344, 
            -76.4996109008789
        ]
    }, 
    "address": "Ottawa, ON", 
    "lat": 45.389198303222656, 
    "lng": -75.68800354003906, 
    "quality": "PopulatedPlace", 
    "accuracy": "Rooftop"
}
```

Change the type of output between JSON/GeoJSON

```bash
$ geocode "Ottawa, Ontario" --geojson --pretty
{
    "geometry": {
        "type": "Point", 
        "coordinates": [
            -75.68800354003906, 
            45.389198303222656
        ]
    }, 
    "type": "Feature", 
    "properties": {
        "status": "OK", 
        "city": "Ottawa", 
        "country": "Canada", 
        "provider": "bing", 
        "location": "Ottawa Ontario", 
        "state": "ON", 
        "address": "Ottawa, ON", 
        "quality": "PopulatedPlace", 
        "accuracy": "Rooftop"
    }, 
    "bbox": [
        -76.4996109008789, 
        45.07920837402344, 
        -74.90253448486328, 
        45.77197265625
    ]
}
```


For more development requests for the CLI, please provide your input in the [Github Issues Page](https://github.com/DenisCarriere/geocoder/issues).


## Reverse Geocoding

The term geocoding generally refers to translating a human-readable address into
a location on a map. The process of doing the opposite, translating a location
on the map into a human-readable address, is known as reverse geocoding.
Using Geocoder you can retrieve Reverse's geocoded data from Google Geocoding API.

### Python Example

At the moment the two providers that have the functionality of Reverse geocoding are **Google** & **Bing**. Simply include the `method=reverse` parameter.

```python
>>> import geocoder
>>> g = geocoder.bing(['lat','lng'], method='reverse')
>>> g.address
'453 Booth Street, Ottawa'
...
```

## Using Proxies

Using proxies will hide the IP address of the client computer when calling a request using the Python Geocoder.

```python
>>> import geocoder
>>> proxies = {'http':'http://108.165.33.12:3128'}
>>> g = geocoder.google('New York City', proxies=proxies)
...
```

## GeoJSON

Use the `geometry` attribute to retrieve the format in a GeoJSON format.

```python
>>> g = geocoder.google('Ottawa, ON')
>>> g.geometry
{'coordinates': [-75.69719309999999, 45.4215296], 'type': 'Point'}
...
```

### Visit the [Wiki](https://github.com/DenisCarriere/geocoder/wiki/)

Please look at the following pages on the wiki for more information about a certain topic.

### Providers
Here is a list of providers that are available for use with **FREE** or limited restrictions.

- [FreeGeoIP](https://github.com/DenisCarriere/geocoder/wiki/FreeGeoIP) **New**

- [OpenCage](https://github.com/DenisCarriere/geocoder/wiki/OpenCage) **New**

- [OSM](https://github.com/DenisCarriere/geocoder/wiki/OSM)

- [Bing](https://github.com/DenisCarriere/geocoder/wiki/Bing)

- [Nokia](https://github.com/DenisCarriere/geocoder/wiki/Nokia)

- [Yahoo](https://github.com/DenisCarriere/geocoder/wiki/Yahoo)

- [Google](https://github.com/DenisCarriere/geocoder/wiki/Google)

- [ArcGIS](https://github.com/DenisCarriere/geocoder/wiki/ArcGIS)

- [TomTom](https://github.com/DenisCarriere/geocoder/wiki/TomTom)

- [Geonames](https://github.com/DenisCarriere/geocoder/wiki/Geonames)

- [MapQuest](https://github.com/DenisCarriere/geocoder/wiki/MapQuest)

- [Geocoder.ca](https://github.com/DenisCarriere/geocoder/wiki/Geocoder.ca)

### Extras

The fun extra stuff I added to enjoy some cool features the web has to offer.

- [Reverse Geocoding](https://github.com/DenisCarriere/geocoder/wiki/Reverse)

- [IP Address](https://github.com/DenisCarriere/geocoder/wiki/IP Address)

- [Elevation (Meters)](https://github.com/DenisCarriere/geocoder/wiki/Elevation)

- [Time Zone](https://github.com/DenisCarriere/geocoder/wiki/TimeZone)

- [CanadaPost](https://github.com/DenisCarriere/geocoder/wiki/CanadaPost)


### Topic not available?

If you cannot find a topic you are looking for, please feel free to ask me @[DenisCarriere](https://github.com/DenisCarriere) or post them on the [Github Issues Page](https://github.com/DenisCarriere/geocoder/issues).

## Support

This project is free & open source, it would help greatly for you guys reading this to contribute, here are some of the ways that you can help make this Python Geocoder better.

### Feedback

Please feel free to give any feedback on this module. If you find any bugs or any enhancements to recommend please send some of your comments/suggestions to the [Github Issues Page](https://github.com/DenisCarriere/geocoder/issues).

### Twitter

Speak up on Twitter [@DenisCarriere](https://twitter.com/DenisCarriere) and tell me how you use this Python Geocoder. New updates will be pushed to Twitter Hashtags [#geocoder](https://twitter.com/search?q=%23geocoder).

### Thanks to

A big thanks to all the people that help contribute: 

* @[flebel](https://github.com/flebel)
* @[patrickyan](https://github.com/patrickyan)
* @[themiurgo](https://github.com/themiurgo)
* @[esy](https://github.com/lambda-conspiracy)
