"""
Custom data structures.
"""

from collections import defaultdict, namedtuple, OrderedDict

Tree = lambda: defaultdict(Tree)
Pattern = namedtuple('Pattern', ['lookup', 'replace'])

class FileSchema(object):

    def __init__(self, name, moniker, base, size):
        self.name = name
        self.moniker = moniker
        self.base = base
        self.size = size
