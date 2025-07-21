"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def dfs(node: Node):
            if not node:
                return

            if node.children:
                for child in node.children:
                    dfs(child)
            res.append(node.val)
            
        res = []
        dfs(root)
        return res