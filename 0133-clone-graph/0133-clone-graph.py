"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # DFS
        # hash map
        def dfs(node: Node, clone_map = {}) -> Node:
            # if already cloned, return the one
            if node in clone_map:
                return clone_map[node]

            cloned_node = Node(node.val)
            clone_map[node] = cloned_node

            for neighbor in node.neighbors:
                cloned_neighbor = dfs(neighbor, clone_map)
                cloned_node.neighbors.append(cloned_neighbor)
            return cloned_node

        if not node:
            return None
        return dfs(node)