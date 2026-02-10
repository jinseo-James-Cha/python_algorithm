# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # bfs
        
        if not root:
            return []
        
        res = []
        queue = deque([root])
        while queue:
            size = len(queue)
            curr_max = float('-inf')
            for _ in range(size):
                curr = queue.popleft()
                curr_max = max(curr.val, curr_max)
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
            res.append(curr_max)
        return res