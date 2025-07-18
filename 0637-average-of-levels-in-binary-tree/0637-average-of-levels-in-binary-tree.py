# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # bfs
        res = []
        queue = deque([root])
        while queue:
            sum_of_level = 0
            size_of_level = len(queue)
            for _ in range(size_of_level):
                node = queue.popleft()
                sum_of_level += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(sum_of_level / size_of_level)
        return res
            
