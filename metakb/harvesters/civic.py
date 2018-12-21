"""Harvest all data from civic.

A harvester simply retrieves data from a source and writes it to a file for downstream processing
"""

from metakb.utils.requests import Client
from metakb.utils.ioutils import JSONEmitter


def fetch(gene_count):
    """Retrieve all gene data N data elements."""
    requests = Client('civic')
    r = requests.get('https://civic.genome.wustl.edu/api/genes?count={}'.format(gene_count))
    for record in r.json()['records']:
        variants = record['variants']
        gene = record['name']
        variants_details = []
        for variant in variants:
            r = requests.get('https://civic.genome.wustl.edu/api/variants/{}'.format(variant['id']))
            variants_details.append(r.json())
        gene_data = {'gene': gene, 'civic': {'variants': variants_details}}
        yield gene_data


def harvest(path='source/civic.json', gene_count=999999, compresslevel=9):
    """Harvest data from civic, write to a file."""
    with JSONEmitter(path, compresslevel=compresslevel) as emitter:
        for gene_data in fetch(gene_count):
            emitter.write(gene_data)
