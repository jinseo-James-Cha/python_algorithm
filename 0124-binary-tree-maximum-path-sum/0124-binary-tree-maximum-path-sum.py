# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = -float('inf')

        def dfs(node):
            nonlocal maxPath
            if not node:
                return 0
            
            gainFromLeft = max(dfs(node.left), 0)
            gainFromRight = max(dfs(node.right), 0)

            maxPath = max(maxPath, gainFromLeft + gainFromRight + node.val)
            return max(gainFromLeft + node.val, gainFromRight + node.val)

        dfs(root)
        return maxPath