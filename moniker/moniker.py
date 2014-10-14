from __future__ import print_function, unicode_literals

import fnmatch
import os

from collections import defaultdict

__all__ = ['tree_walk']

# Recursive Tree Definition
Tree = lambda: defaultdict(Tree)

def add(t, key, replace):
    t = t[key[0]]
    t[key[-1]] = replace


def tree_walk(top, pattern, replace):
    """
    Walk file system heiarchy for the base directory generating files matching
    unix glob pattern.
    """
    root  = Tree()
    for path, dirname, filelist in os.walk(top):
        if not any(fnmatch.fnmatch(match, pattern) for match in filelist):
            continue

        for files in fnmatch.filter(filelist, pattern):
            base = os.path.relpath(path, start=top)
            node = [base, files]
            add(root, node, replace)
    return root
