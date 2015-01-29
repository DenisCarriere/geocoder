import argparse
import fileinput
import itertools
import json
import sys
from .api import get

def peek(iterable):
    iterator = iter(iterable)
    item = next(iterator)
    new_iterator = itertools.chain([item], iterator)
    return item, new_iterator

def cli():
    parser = argparse.ArgumentParser(description="Geocode an arbitrary number of strings from Command Line.")
    parser.add_argument('input', type=str, nargs="*", help="Filename(s) or strings to be geocoded")
    parser.add_argument('-p', '--provider', help="provider (choose from: bing,"+\
	"geonames, google, mapquest, nokia, osm, tomtom, geolytica, arcgis, yahoo)", default='bing')
    parser.add_argument('-o', '--outfile', help="Output file (default stdout)", default=sys.stdout)
    parser.add_argument('--geojson', help="GeoJSON output format (default json)", action="store_true")
    parser.add_argument('--json', help="JSON output format (default json)", action="store_true")
    parser.add_argument('--osm', help="OSM output format (default json)", action="store_true")
    parser.add_argument('--pretty', help="Prettify JSON output", action="store_true")
    args = parser.parse_args()

    try:
        sys.argv = [sys.argv[1]] + args.input
        input = fileinput.input()
        _, input = peek(input)
    except IOError:
        input = args.input

    for item in input:
        item = item.strip()
        g = get(item, provider=args.provider)
        
        if args.geojson:
            output = g.geojson
        elif args.osm:
            output = g.osm
        else:
            output = g.json

        if args.pretty:
            params = {'indent': 4}
        else:
            params = {}
        
        args.outfile.write("{}\n".format(json.dumps(output, **params)))