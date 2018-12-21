"""This module tests civic harvester."""

import os
import contextlib

from metakb.harvesters.civic import harvest


def test_creates_file():
    """Should create a file."""
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test', 'civic.json')
    with contextlib.suppress(FileNotFoundError):
        os.remove(path)
    harvest(path=path, gene_count=2, compresslevel=0)
    num_lines = sum(1 for line in open(path))
    assert num_lines == 2, 'Should have created a file with two lines'
    os.remove(path)
