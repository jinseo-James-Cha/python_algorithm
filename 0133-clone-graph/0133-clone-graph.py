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
        def dfs(curr_node):
            if curr_node in visited:
                return visited[curr_node]
            
            copied_node = Node(curr_node.val)
            visited[curr_node] = copied_node
            
            for neighbor in curr_node.neighbors:
                copied_neighbor = dfs(neighbor)
                copied_node.neighbors.append(copied_neighbor)
            
            return copied_node
        
        
        if not node:
            return None
        
        visited = {}
        return dfs(node)