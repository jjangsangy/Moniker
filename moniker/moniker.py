import os
import re

from os.path import basename, relpath

from .structs import Tree, Pattern

__all__ = ['tree_walk']

def add(t, key):
    t[key[0]] = [i for i in key[1]]


def tree_walk(top, replace=('', '')):
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
    root  = Tree()
    find  = Pattern(*replace)

    pat = re.compile(re.escape(find.lookup))
    for path, _, filelist in os.walk(top):

        # TODO: Replace binning engine
        if not any(
            [files for files in filelist if files.endswith(find.lookup)]
        ):
            continue

        # TODO: Replace Matching engine
        base = relpath(path, start=top)
        node = [
            base, [
            {
                files: pat.sub(find.replace, files)
            }
                for files in filelist if files.endswith(find.lookup)
        ]]

        # Add Node
        add(root, node)

    return root
