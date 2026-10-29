import sys

from .core import parse_config


def main(argv=None):
    path = (argv or sys.argv[1:])[0]
    with open(path) as f:
        print(parse_config(f.read()))
