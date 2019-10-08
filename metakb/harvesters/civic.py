"""Module for the CIViC harvester."""
from .harvester import Harvester
from civicpy import civic


class CivicHarvester(Harvester):
    """A harvester for the CIViC resource."""

    def __init__(self):
        """Initialize instance."""
        self.evidence = None

    def harvest_iter(self):
        """Harvest and yield associations from CIViC as dict."""
        self._get_evidence_records()
        for e in self.evidence:
            response_dict = {
                'id': e.id
            }
            yield response_dict

    def _get_evidence_records(self):
        self.evidence = civic.get_all_evidence()
