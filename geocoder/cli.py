import argparse
import fileinput
import itertools
import json
import sys
from api import get

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
        args.outfile.write("{}\n".format(json.dumps(g.json)))
