"""Useful io utilities."""

import json
import gzip
import os
import csv
import io


def ensure_directory(*args):
    """Create a directory."""
    path = os.path.join(*args)
    if os.path.isfile(path):
        raise Exception(
            "Output directory %s is a regular file", path)

    if not os.path.exists(path):
        os.makedirs(path)


def reader(path, **kwargs):
    """Wrap gzip if necessary."""
    if path.endswith(".gz"):
        return io.TextIOWrapper(
            io.BufferedReader(gzip.GzipFile(path))
        )
    elif path.endswith(".csv"):
        return csv.DictReader(open(path, "r"), **kwargs)
    elif path.endswith(".tsv"):
        return csv.DictReader(open(path, "r"), delimiter="\t", **kwargs)
    else:
        return open(path, "r")


class JSONEmitter():
    """Writes objects to disk as json, defaults to gz."""

    def __init__(self, path, compresslevel=9):
        """Ensure path exists and set compresslevel=0 to skip compression."""
        self.path = path
        self.compresslevel = compresslevel
        ensure_directory(os.path.dirname(path))
        if compresslevel == 0:
            self.fh = open(path, mode='wt')
        else:
            if 'gz' not in path:
                self.path = path + '.gz'
            # write with 0 mtime (ensures identical file each run)
            # in turn ensures md5 hash identical
            self.fh = gzip.GzipFile(
                filename='',
                compresslevel=self.compresslevel,
                fileobj=open(self.path, mode='wb'),
                mtime=0
            )

    def write(self, obj):
        """Write object as json + newline."""
        if self.compresslevel > 0:
            self.fh.write(json.dumps(obj).encode())
            self.fh.write('\n'.encode())
        else:
            self.fh.write(json.dumps(obj))
            self.fh.write('\n')

    def close(self):
        """Close the file."""
        self.fh.close()

    # support 'with...'
    def __enter__(self):
        """Set things up."""
        return self

    def __exit__(self, type, value, traceback):
        """Tear things down."""
        self.close()
