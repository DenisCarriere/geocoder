#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
import click
import json
import geocoder
import os
import fileinput
from geocoder.api import options


providers = sorted(options.keys())
methods = ['geocode', 'reverse', 'elevation', 'timezone', 'places']
outputs = ['json', 'osm', 'geojson', 'wkt']
units = ['kilometers', 'miles', 'feet', 'meters']


@click.command()
@click.argument('location', nargs=-1)
@click.option('--provider', '-p', default='osm', type=click.Choice(providers))
@click.option('--method', '-m', default='geocode', type=click.Choice(methods))
@click.option('--output', '-o', default='json', type=click.Choice(outputs))
@click.option('--units', '-u', default='kilometers', type=click.Choice(units))
@click.option('--timeout', '-t', default=5.0)
@click.option('--distance', is_flag=True)
@click.option('--language', default='')
@click.option('--url', default='')
@click.option('--proxies')
@click.option('--key')
# following are for Tamu provider
@click.option('--city', '-c', default='')
@click.option('--state', '-s', default='')
@click.option('--zipcode', '-z', default='')
def cli(location, **kwargs):
    """Geocode an arbitrary number of strings from Command Line."""

    locations = []

    # Read Standard Input
    # $ cat foo.txt | geocode
    try:
        for line in fileinput.input():
            locations.append(line.strip())
    except:
        pass

    # Read multiple files & user input location
    for item in location:
        if os.path.exists(item):
            with open(item, 'rb') as f:
                locations += f.read().splitlines()
        else:
            locations.append(item)

    # Distance calcuation
    if kwargs['distance']:
        d = geocoder.distance(locations, **kwargs)
        click.echo(d)
        return

    # Geocode results from user input
    for location in locations:
        g = geocoder.get(location.strip(), **kwargs)
        try:
            click.echo(json.dumps(g.__getattribute__(kwargs['output'])))
        except IOError:
            # When invalid command is entered a broken pipe error occurs
            return

if __name__ == '__main__':
    cli()
