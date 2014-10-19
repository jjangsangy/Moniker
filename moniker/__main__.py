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
except: # No color for you
    pass

def command():
    """
    Argument parsing from the user.
    Passeds a fully parsed command line arguments.

    :TODO:
        Considering parsing at multiple stages or create a tiered system
        with multiple passes.

    """
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
        help='Tiers of file heiarcy explored',
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
    return parser


def main():
    """
    Main Entry point for Moniker
    """

    # CommandLine Args
    parse = command()

    # Parse/Validate User Input
    args = parse.parse_args()
    if not os.path.isdir(args.directory):
        raise IOError

    # Abstract File Tree
    filetree = tree_walk(args.directory, args.replace)
    jsontree = json.dumps(
        filetree, indent=2, sort_keys=True, separators=(', ', ': ')
    )

    # Pipe vs Redirection
    if sys.stdout.isatty():
        try: jsontree = highlight(
                jsontree,
                JsonLexer(),
                Terminal256Formatter(style='autumn'))
        except:
            pass
    print(jsontree)

if __name__ == '__main__':
    sys.exit(main())
