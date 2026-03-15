# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # bfs

        # dfs
        # score

        def dfs(node):
            nonlocal lca
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            myself = 1 if node == p or node == q else 0
            if left + right + myself >= 2:
                lca = node
            
            return left or right or myself
        
        lca = None
        dfs(root)
        return lca
