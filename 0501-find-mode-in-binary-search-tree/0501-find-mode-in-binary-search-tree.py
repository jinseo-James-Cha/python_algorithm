# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # BST
        # left <= parent <= right
        # Could you do that without using any extra space? 
        # (Assume that the implicit stack space incurred due to recursion does not count).
        def dfs(node: TreeNode):
            if not node:
                return
            
            hashmap[node.val] += 1
            dfs(node.left)
            dfs(node.right)

        hashmap = defaultdict(int)
        dfs(root)
        
        max_count = 0
        res = []
        for num, cnt in hashmap.items():
            if cnt > max_count:
                max_count = cnt
                res = [num]
            elif max_count == cnt:
                res.append(num)
        
        return res

