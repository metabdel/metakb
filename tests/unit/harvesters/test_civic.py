"""Test the CIViC harvester."""
import pytest
from metakb.harvesters.civic import CivicHarvester


@pytest.fixture(autouse=True)
def get_fixture(monkeypatch):
    """Prevent live CIViC queries with monkeypatch."""
    def mock_response(self):
        resp = [
            'eid1',
            'eid2',
            'eid3'
        ]
        return resp

    monkeypatch.setattr(CivicHarvester, "_get_evidence_records", mock_response)


@pytest.mark.skip(reason="Testing mock first")
def test_harvest_iter():
    """Test that harvest iterable works as expected."""
    assert False


def test_mock():
    """Test that the get fixture patch works correctly."""
    ch = CivicHarvester()
    assert len(ch._get_evidence_records()) == 3
