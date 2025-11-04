# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        isFromLeft = True
        queue = deque([root])
        res = []
        while queue:
            size = len(queue)
            temp = []
            for _ in range(size):
                curr_node = queue.popleft()
                temp.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            if isFromLeft:
                res.append(temp)
                isFromLeft = False
            else:
                temp.reverse()
                res.append(temp)
                isFromLeft = True
        return res