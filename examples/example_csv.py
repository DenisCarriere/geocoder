import geocoder
import unicodecsv
import logging


# CSV Writer
csvfile = open('csvfiles/address_out.csv', 'wb')
fieldnames = ['source', 'address', 'lat', 'lng', 'postal']
writer = unicodecsv.DictWriter(csvfile, fieldnames=fieldnames, encoding='utf-8')
writer.writeheader()

# CSV Reader
with open('csvfiles/address.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f, encoding='iso-8859-1')
    for line in reader:
        address = line['Address']

        # Geocoding
        g = geocoder.google(address)
        if g.ok:
            row = {}
            row['source'] = address
            row['address'] = g.address
            row['lat'] = g.lat
            row['lng'] = g.lng
            row['postal'] = g.postal
            writer.writerow(row)
            logging.info('Geocoding SUCCESS: ' + address)
        else:
            logging.warning('Geocoding ERROR: ' + address)

