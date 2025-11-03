# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # sum root to leaf
        # parent * 10 -> child..
        
        def dfs(node, totalSum):
            if not node:
                return 0
                
            if not node.left and not node.right:
                return totalSum*10 + node.val

            totalSum = totalSum*10 + node.val
            return dfs(node.left, totalSum) + dfs(node.right, totalSum)
                
        return dfs(root, 0)