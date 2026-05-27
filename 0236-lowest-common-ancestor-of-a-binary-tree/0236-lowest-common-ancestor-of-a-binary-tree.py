# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

        # DFS
        def dfs(node):
            nonlocal lcs
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            curr = node == p or node == q
            if left + right + curr >= 2:
                lcs = node
            return left or right or curr

        lcs = None
        dfs(root)
        return lcs