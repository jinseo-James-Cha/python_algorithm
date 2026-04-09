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
        """
        connected undirected graph
        deep copy


        node.val is unique -> can be key?
        [key] = new Node()

        
        """
        def dfs(curr_node):
            if curr_node in visited:
                return visited[curr_node]
            
            copy_node = Node(curr_node.val)
            visited[curr_node] = copy_node
            for neighbor in curr_node.neighbors:
                copy_node.neighbors.append(dfs(neighbor))

            return copy_node

        if not node:
            return None 
            
        visited = {}
        return dfs(node)
