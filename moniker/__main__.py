# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import json
import os
import sys

from os.path import basename
from argparse import ArgumentParser

from .__version__ import __version__, __build__
from .moniker import tree_walk

try:
    from pygments import highlight
    from pygments.lexers.web import JsonLexer
    from pygments.formatters import Terminal256Formatter
except:
    # No color for you
    pass

def main():
    '''Main Entry point'''
    version = ' '.join([__version__, __build__])
    parser = ArgumentParser(
        prog='moniker',
        description='Simple batch file renaming tool.',
    )
    parser.add_argument(
        '-v', '--version', action='version',
        version="%s v%s" % (basename(sys.argv[0]), version)
    )
    # Not Yet Implemented
    parser.add_argument(
        '--depth',
        type=int,
        metavar='depth',
        help='Recursive renaming',
    )

    parser.add_argument(
        '--replace',
        nargs=2,
        default=('', ''),
        metavar='replace',
        help='glob pattern to match'
    )
    parser.add_argument(
        'directory',
        default='.',
        help='target directory root',
    )

    # Parse/Validate User Input
    args = parser.parse_args()
    if not os.path.isdir(args.directory):
        raise IOError

    # Abstract File Tree
    filetree = tree_walk(args.directory, args.replace)
    jsontree = json.dumps(
        filetree, indent=2, sort_keys=True, separators=(', ', ': ')
    )

    # Pipe vs Redirection
    if sys.stdout.isatty():
        try:
            jsontree = highlight(jsontree, JsonLexer(), Terminal256Formatter(style='autumn'))
        except:
            pass

    print(jsontree)

if __name__ == '__main__':
    sys.exit(main())
