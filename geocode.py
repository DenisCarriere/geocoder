import click
import geocoder
import unicodecsv
import sys


@click.command()
@click.argument('location', required=False)
@click.option('--provider', default='bing')
@click.option('--input', type=click.File('r'))
@click.option('--output', type=click.File('w'), default='-')
@click.option('--fieldnames')

def cli(location, provider, input, output, fieldnames):
    """
    This is the help function part of the script\n
    geocode --string
    """
    container = []

    # Reading Input files
    if input:
        reader = unicodecsv.DictReader(input)
        first_column = reader.fieldnames[0]

        # Loop inside the reader
        for item in reader:
            location = item[first_column]
            g = geocoder.geocode(location, provider=provider)
            
            # Format Row
            row = dict(g.json.items() + item.items())

            # Print Results & Add
            container.append(row)
            if output.name == '<stdout>':
                click.echo(row)

    # Reading Single Input
    else:
        g = geocoder.geocode(location, provider=provider)
        container.append(g.json)
        
        if output.name == '<stdout>':
            click.echo(g.json)  


    # Saving Results
    if container:
        first = container[0]
        fieldnames = first.keys()
        if not output.name == '<stdout>':
            writer = unicodecsv.DictWriter(output, fieldnames=fieldnames) 
            writer.writeheader()

            for row in container:
                writer.writerow(row)
