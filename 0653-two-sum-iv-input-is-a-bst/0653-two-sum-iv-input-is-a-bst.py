# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # BFS
        nums = {}
        queue = deque([root])
        while queue:
            node = queue.popleft()
            
            if node.val in nums:
                return True
            
            nums[k - node.val] = True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return False
        