# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # return to the same node in the cloned tree
        queue = deque([(original, cloned)])
        while queue:
            original_node, cloned_node = queue.popleft()
            if original_node == target:
                return cloned_node
            
            if original_node.left:
                queue.append((original_node.left, cloned_node.left))
            if original_node.right:
                queue.append((original_node.right, cloned_node.right))

        return None
        

        