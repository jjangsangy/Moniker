"""
Custom data structures.
"""

from collections import defaultdict, namedtuple


Tree = lambda: defaultdict(Tree)
Pattern = namedtuple('Pattern', ['lookup', 'replace'])
