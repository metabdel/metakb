"""Module for the CIViC harvester."""
from .harvester import Harvester
from civicpy import civic


class CivicHarvester(Harvester):
    """A harvester for the CIViC resource."""

    def harvest_iter(self):
        """Harvest and yield associations from CIViC as dict."""
        evidence = civic.get_all_evidence()
        for e in evidence:
            response_dict = {
                'id': e.id
            }
            yield response_dict
