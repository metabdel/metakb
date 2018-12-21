"""This module tests ioutils."""

import os
import uuid
import metakb.utils.ioutils as ioutils
import pytest


def test_ensure_directory():
    """Should create a directory."""
    dirname = str(uuid.uuid1())
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test', dirname)
    ioutils.ensure_directory(path)
    directory_created = os.path.isdir(path)
    if directory_created:
        os.rmdir(path)
    assert directory_created, 'Should have created new directory {}'.format(path)


def test_ensure_directoryraises_error():
    """Should raise an error if passed a file."""
    path = os.path.realpath(__file__)
    with pytest.raises(Exception):
        ioutils.ensure_directory(path)
        assert False, 'Should have raised an exception'


def test_gzip_emitter():
    """Should create a gz json file with gz."""
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test', 'anything.json')
    with ioutils.JSONEmitter(path) as emitter:
        emitter.write({'foo': 'bar'})
    assert os.path.isfile(path + '.gz'), 'Should create .gz'
    os.remove(path + '.gz')


def test_gzip_emitter_suffix():
    """Should create a gz json file with gz already appended."""
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test', 'anything.json.gz')
    with ioutils.JSONEmitter(path) as emitter:
        emitter.write({'foo': 'bar'})
    assert not os.path.isfile(path + '.gz'), 'Should not create .gz.gz'
    os.remove(path)


def test_plain_emitter():
    """Should create a json file."""
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test', 'anything.json')
    with ioutils.JSONEmitter(path, compresslevel=0) as emitter:
        emitter.write({'foo': 'bar'})
    assert os.path.isfile(path), 'Should create .json'
    os.remove(path)


def test_reader():
    """Should return appropriate reader."""
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fixtures', 'test.txt')
    assert str(ioutils.reader(path).__class__.__name__) == 'TextIOWrapper'
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fixtures', 'test.csv')
    assert str(ioutils.reader(path).__class__.__name__) == 'DictReader'
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fixtures', 'test.tsv')
    assert str(ioutils.reader(path).__class__.__name__) == 'DictReader'
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fixtures', 'test.txt.gz')
    assert str(ioutils.reader(path).__class__.__name__) == 'TextIOWrapper'
