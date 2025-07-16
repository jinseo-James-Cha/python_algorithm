# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return
            uniques.add(node.val)
            dfs(node.left)
            dfs(node.right)
            
        uniques = set()
        dfs(root)
        m, ans = root.val, float(inf)
        for u in uniques:
            if m < u < ans:
                ans = u
        
        return ans if ans < float(inf) else -1


