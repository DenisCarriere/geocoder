import json
import sys
import click
from api import get

@click.command()
@click.argument('input', type=str)
@click.option('--provider', '-p', default='bing', help="provider (choose from: bing,\
geonames, google, mapquest, nokia, osm, tomtom, geolytica, arcgis, yahoo)")
@click.option('--outfile', '-o', type=click.File('w'), default='-',
        help="Output File")
def cli(input, provider, outfile):
    """Geocode one or many string.

    Arguments:

        input      string or filename containing one string per line.

    """
    try:
        input = open(input, "r")
    except:
        input = [input]

    # Loop inside the reader
    for item in input:
        item = item.strip()
        g = get(item, provider=provider)
        outfile.write("{}\n".format(json.dumps(g.json)))

