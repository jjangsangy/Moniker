"""
Custom data structures.
"""

import collections

__all__ = 'Tree', 'Pattern'

Tree    = lambda: collections.defaultdict(Tree)
Pattern = collections.namedtuple('Pattern', ['lookup', 'replace'])
