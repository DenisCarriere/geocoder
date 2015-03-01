# Write to CSV

## Single Address

```python
import geocoder
import csv

g = geocoder.bing('Avenida da Republica, Lisboa')

with open('test.csv', 'wb') as f:
    writer = csv.DictWriter(f, fieldnames=g.fieldnames)
    writer.writeheader()
    writer.writerow(g.json)
```
**Note**: The `fieldnames` is new in 1.1.3, `attributes` in the earlier versions.

## Multiple Address

The CSV file used for **locations.csv**.

Using `delimiter` for parsing a CSV might include `<\t> <;> <|> <,>`


| location    | extra      |
|-------------|-----------|
| Canada      | best      |
| Australia   | amazing   |
| Venezuela   | awesome   |

```python
import geocoder
import csv

rows = []
fieldnames = ['location', 'extra', 'lat', 'lng', 'state', 'country']

with open('locations.csv') as f:
    reader = csv.DictReader(f, delimiter=';')
    for line in reader:
        g = geocoder.google(line['location'])

        # Add the CSV line data into the Geocoder JSON result
        result = g.json
        result.update(line)

        # Store Geocoder results in a list to save it later
        rows.append(result)

with open('locations_new.csv', 'wb') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(rows)
```