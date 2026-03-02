# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # bfs  
        res = 0
        queue = deque([(root, 0)])
        while queue:
            curr, curr_total = queue.popleft()
            
            # leaf
            if not curr.left and not curr.right:
                res += (curr_total * 10) + curr.val
            
            if curr.left:
                queue.append((curr.left, curr_total*10 + curr.val))

            if curr.right:
                queue.append((curr.right, curr_total*10 + curr.val))
        return res