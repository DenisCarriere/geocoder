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
    parser = argparse.ArgumentParser(description="Geocode an arbitrary number"
                                     " of strings from Command Line.")
    parser.add_argument('input',
                        type=str,
                        nargs="*",
                        help="Filename(s) or strings to be geocoded")
    parser.add_argument('-p', '--provider',
                        help="provider (choose from: bing,"
                        "geonames, google, mapquest, nokia, osm, tomtom, "
                        "geolytica, arcgis, yahoo, ottawa)",
                        default='bing')
    parser.add_argument('-m', '--method',
                        type=str,
                        help="Output type (choose from: geocode, reverse)",
                        default='geocode')
    parser.add_argument('-o', '--outfile',
                        help="Output file (default stdout)",
                        default=sys.stdout)
    parser.add_argument('-t', '--type',
                        type=str,
                        help="Output type (choose from: json, osm, geojson)",
                        default='json')
    parser.add_argument('--pretty',
                        help="Prettify JSON output",
                        action="store_true")
    args = parser.parse_args()

    # User input data
    if args.input:
        try:
            sys.argv = [sys.argv[1]] + args.input
            input = fileinput.input()
            _, input = peek(input)
        except IOError:
            input = args.input
    else:
        print('[ERROR] Please include a location or a <File Path>.\n'
              '$ geocode "Ottawa ON\n"'
              '$ geocode "textfile.txt"')
        sys.exit()

    for item in input:
        item = item.strip()
        g = get(item, provider=args.provider, method=args.method)

        # User input output
        args.type = args.type.lower()
        type_lookup = {
            'json': g.json,
            'geojson': g.geojson,
            'osm': g.osm,
        }
        if args.type in type_lookup:
            output = type_lookup.get(args.type.lower(), '')
        else:
            print('[ERROR] Please provide a valid type.\n'
                  'Ex: geojson, osm,  json\n'
                  '$ geocode "Ottawa ON" --type geojson')
            sys.exit()

        # User define Pretty output
        if args.pretty:
            params = {'indent': 4}
        else:
            params = {}

        args.outfile.write("{}\n".format(json.dumps(output, **params)))
