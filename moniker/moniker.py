import os
import re

from os.path import relpath

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
    esc   = re.escape(find.lookup)
    pat   = re.compile(r'(\w*|\w*\.|\w*-)({p})(\w*|\w*\.|\w*-)'.format(
                    p=esc))

    for path, _, filelist in os.walk(top):
        if not any(i for i in filelist if pat.search(i)):
            continue

        base = relpath(path, start=top)
        print(base)
        node = [
            base, [
            {
                files: re.sub(
                    pat.search(files).group(2), find.replace, files
            )}
                for files in filelist if pat.search(files)
        ]]
        # Add Node
        add(root, node)

    return root
