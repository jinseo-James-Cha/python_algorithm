# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. left child node should be less than parent node
# 2. right child node should be greater than parent node
# 3. keep cheching all

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, minimum, maximum):
            if not node:
                return True
            
            if not (node.val > minimum and node.val < maximum):
            # if node.val <= minimum or node.val >= maximum:
                return False
        
            return valid(node.left, minimum, node.val) and valid(node.right, node.val, maximum)

        return valid(root, float("-inf"), float("inf"))

        