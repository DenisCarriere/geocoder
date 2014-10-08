import json
import sys

import click

import geocoder

@click.command()
@click.argument('infile', type=click.File('r'), default=sys.stdin)
@click.option('--provider', default='bing', help="Provider (choose from: bing,\
geonames, google, mapquest, nokia, osm, tomtom, geolytica, arcgis, yahoo")
@click.option('--outfile', '-o', type=click.File('w'), default=sys.stdout,
        help="Output File")
def cli(infile, provider, outfile):
    """Geocode multiple strings, line by line, passed via STDIN or contained in a file."""
    # Loop inside the reader
    for item in infile:
        item = item.strip()
        g = geocoder.geocode(item, provider=provider)
        outfile.write("{}\n".format(json.dumps(g.json)))

