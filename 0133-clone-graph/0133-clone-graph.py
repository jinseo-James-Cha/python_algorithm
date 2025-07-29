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
        def dfs(node: Node, visited = {}) -> Node:
            if node in visited:
                return visited[node]

            cloned_node = Node(node.val)
            visited[node] = cloned_node

            for neighbor in node.neighbors:
                cloned_neighbor = dfs(neighbor, visited)
                cloned_node.neighbors.append(cloned_neighbor)
            return cloned_node

        if not node:
            return None
        return dfs(node)