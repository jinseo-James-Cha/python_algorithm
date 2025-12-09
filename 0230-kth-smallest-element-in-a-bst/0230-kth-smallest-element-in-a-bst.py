# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # get all vals into heapq and get the kth?
        vals = []

        def dfs(node):
            if not node:
                return
            
            vals.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        vals.sort()
        return vals[k-1]