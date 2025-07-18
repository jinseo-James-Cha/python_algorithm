"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # n-ary tree preorder -> p l r
        # dfs preorder
        def dfs(node: Node):
            if not node:
                return
            
            res.append(node.val)
            for child in node.children:
                dfs(child)
        
        res = []
        dfs(root)
        return res
