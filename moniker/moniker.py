# -*- coding: utf-8 -*-

import os
import re
import stat

from os.path import relpath

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
    pat  = re.compile(
        r'(\w*|\w*\.|\w*-)({phrase})(\w*|\w*\.|\w*-)'.format(
            phrase=re.escape(find.lookup))
    )

    # Tree Level
    for path, dirpath, filelist in os.walk(top):

        matches = []
        base    = relpath(path, start=top)
        levels  = base.split(os.sep)
        depth   = len(levels) - levels.count('.')

        if depth > maxdepth:
            break
        if not any(pat.search(i) for i in filelist):
            continue

        # Node Level
        for name in filelist:

            # Filter
            match = pat.search(name)
            if not match:
                continue

            # Construct Data Structure
            filepath = os.path.join(path, name)
            info     = os.stat(filepath)
            node     = {
                'depth': depth,
                'name': {
                    'oldname': name,
                    'moniker': re.sub(match.group(2), find.replace, name),
                },
                'stats': {
                    'size'  : info.st_size,
                    '_uid'  : info.st_uid,
                    '_gid'  : info.st_gid,
                    'mode'  : stat.S_IFMT(info.st_mode),
                    'write' : os.access(filepath, os.W_OK),
                }
            }

            matches.append(node)

        root[base] = matches

    return root
