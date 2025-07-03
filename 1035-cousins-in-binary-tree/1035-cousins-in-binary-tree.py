# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # true if x and y are cousins
        # cousins -> if they have the same depth with different parent
        # the same depth, different parent
        
        # BFS
        queue = deque([root])
        x_depth = y_depth = cur_depth = 0
        x_parent = y_parent = 0
        while queue:
            n = len(queue)
            cur_depth += 1
            for _ in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    if node.left.val == x:
                        x_depth = cur_depth
                        x_parent = node.val
                    elif node.left.val == y:
                        y_depth = cur_depth
                        y_parent = node.val
                if node.right:
                    queue.append(node.right)
                    if node.right.val == x:
                        x_depth = cur_depth
                        x_parent = node.val
                    elif node.right.val == y:
                        y_depth = cur_depth
                        y_parent = node.val

        return x_depth == y_depth and x_parent != y_parent