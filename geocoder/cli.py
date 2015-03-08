#!/usr/bin/python
# coding: utf8

import click
import json
import geocoder
import sys
import os


providers = ['google', 'bing', 'osm', 'here', 'w3w', 'opencage', 'yandex',
             'arcgis', 'tomtom', 'mapquest', 'maxmind', 'baidu', 'canadapost',
             'freegeoip', 'geolytica', 'ottawa', 'geonames', 'yahoo']
methods = ['geocode', 'reverse', 'elevation', 'timezone']
outputs = ['json', 'osm', 'geojson', 'wkt']


@click.command()
@click.argument('location', nargs=-1)
@click.option('--provider', '-p', default='bing', type=click.Choice(providers))
@click.option('--method', '-m', default='geocode', type=click.Choice(methods))
@click.option('--output', '-o', default='json', type=click.Choice(outputs))
@click.option('--url', '-u', default='')
def cli(location, provider, method, output, url):
    "Geocode an arbitrary number of strings from Command Line."

    # Read multiple files & user input location
    locations = []
    for item in location:
        if os.path.exists(item):
            with open(item, 'rb') as f:
                locations += f.read().splitlines()
        else:
            locations.append(item)

    # Geocode results from user input
    for location in locations:
        g = geocoder.get(location.strip(), provider=provider, method=method, url=url)
        try:
            click.echo(json.dumps(g.__getattribute__(output)))
        except IOError:
            # When invalid command is entered a broken pipe error occurs
            sys.exit()

if __name__ == '__main__':
    cli()
