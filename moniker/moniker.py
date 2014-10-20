import os
import re

from os.path import relpath, abspath

from .structs import Tree, Pattern, FileSchema

__all__ = ['tree_walk']

def add(t, key):
    t[key.base] = {
        'oldname': key.name,
        'size': key.size,
        'moniker': key.moniker,
        'depth': key.depth,
    }

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
    root  = Tree()
    find  = Pattern(*replace)
    esc   = re.escape(find.lookup)
    pat   = re.compile(r'(\w*|\w*\.|\w*-)({p})(\w*|\w*\.|\w*-)'.format(
                    p=esc))
    c_match = lambda f: (match for match in f if pat.search(match))

    for path, dirpath, filelist in os.walk(top):
        if not any(c_match(filelist)):
            continue
        base = relpath(path, start=top)
        levels = base.split(os.sep)
        depth = len(levels) - levels.count('.')
        if depth >= maxdepth+1:
            continue
        for node in filelist:
            if not pat.search(node):
                continue
            moniker  = re.sub(pat.search(node).group(2), find.replace, node)
            size     = os.path.getsize(abspath(os.path.join(path, node)))
            filenode = FileSchema(node, moniker, base, size, depth)
            add(root, filenode)
    return root
