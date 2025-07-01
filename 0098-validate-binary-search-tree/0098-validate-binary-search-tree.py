# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # DFS recursive
        # left.val < node.val < right.val
        def validBST(node: TreeNode, minimum: int, maximum: int) -> bool:
            if not node:
                return True
            
            if node.val <= minimum:
                return False
            if node.val >= maximum:
                return False
            
            return validBST(node.left, minimum, node.val) and validBST(node.right, node.val, maximum)
        
        return validBST(root, -inf, inf)
        