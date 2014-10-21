# -*- coding: utf-8 -*-

import os
import re

from os.path import relpath, abspath, getsize
from collections import OrderedDict

from .structs import Tree, Pattern

__all__ = ['tree_walk']

def tree_walk(top, replace=('', ''), maxdepth=0):
    """
    Walk file system heiarchy for the base directory generating files matching
    unix glob pattern.

    :param top:     The top of the filesystem heiarchy and starting node.
    :type top:      String
    :param replace: Files to be matched and replaced.
    :type replace:  Tuple

    :returns type: <type defaultdict>
    :returns: Tree

    """
    root = Tree()
    find = Pattern(*replace)
    pat = re.compile(
        r'(\w*|\w*\.|\w*-)({phrase})(\w*|\w*\.|\w*-)'.format(
            phrase=re.escape(find.lookup))
    )
    c_match = lambda f: (match for match in f if pat.search(match))

    # Tree Level
    for path, dirpath, filelist in os.walk(top):

        if not any(c_match(filelist)):
            continue

        nodes  = []
        base   = relpath(path, start=top)
        levels = base.split(os.sep)
        depth  = len(levels) - levels.count('.')

        if depth > maxdepth:
            continue

        # Node Level
        for name in filelist:
            match = pat.search(name)
            if not match:
                continue
            node = OrderedDict({
                   'name': name,
                'moniker': re.sub(match.group(2), find.replace, name),
                   'size': getsize(abspath(os.path.join(path, name))),
                  'depth': depth,
            })
            nodes.append(node)
        root[base] = nodes
    return root
