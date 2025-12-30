# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # bfs -> sum by levels

        # edge case
        if not root.left and not root.right:
            return 1

        maximum_sum = float('-inf')
        maximum_level = 1
        
        queue = deque([root])
        curr_level = 0
        while queue:
            size = len(queue)
            curr_level += 1
            level_sum = 0
            for _ in range(size):
                curr = queue.popleft()
                level_sum += curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            if level_sum > maximum_sum:
                maximum_sum = level_sum
                maximum_level = curr_level
        return maximum_level

