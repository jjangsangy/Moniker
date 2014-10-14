# -*- coding: utf-8 -*-
import re
import json
import os
import sys

from os.path import basename
from argparse import ArgumentParser

from .__version__ import __version__, __build__

from .moniker import tree_walk

def main():
    '''Main Entry point'''
    version = ' '.join([__version__, __build__])
    parser = ArgumentParser(
        prog='moniker',
        description='Simple batch file renaming tool.',
    )
    parser.add_argument(
        '-V', '--version', action='version',
        version="%s v%s" % (basename(sys.argv[0]), version))

    # Not Yet Implemented
    parser.add_argument(
        '-t', '--test', action='store_true',
        help='Run test in-place without renaming',
    )

    # Not Yet Implemented
    parser.add_argument(
        '-f', '--force', action='store_true',
        help='Do it by force, no checks.',
    )

    # Not Yet Implemented
    parser.add_argument(
        '-r', '--recursive', action='store_true',
        help='Recursive renaming',
    )
    parser.add_argument(
        'directory',
        help='target directory'
    )
    parser.add_argument(
        'pattern',
        type=str,
        help='glob pattern to match'
    )
    parser.add_argument(
        'replace',
        help='glob pattern to match'
    )

    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        raise IOError

    filetree = tree_walk(args.directory, args.pattern, args.replace)
    print(json.dumps(filetree, indent=4, sort_keys=True))

if __name__ == '__main__':
    sys.exit(main())
