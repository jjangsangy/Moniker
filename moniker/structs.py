"""
Custom data structures.
"""

import collections

Tree    = lambda: collections.defaultdict(Tree)
Pattern = collections.namedtuple('Pattern', ['lookup', 'replace'])
