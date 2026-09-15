"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    # BFS
    def __init__(self):
        self.original_clone = {} # hashmap with mapping
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.traverse(node)
        return self.original_clone.get(node) # according node in clone graph 

    def traverse(self, node):
        if node is None:
            return
        if node in self.original_clone:
            return
        # preposition
        elif node not in self.original_clone:
            self.original_clone[node] = Node(node.val) # new a node to copy
        clone_node = self.original_clone[node]

        for neighbor in node.neighbors:
            self.traverse(neighbor)
            # also add neighbors
            clone_neighbor = self.original_clone[neighbor]
            clone_node.neighbors.append(clone_neighbor)
        