# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validateBST(node, minimum, maximum):
            if not node:
                return True
            
            if minimum >= node.val:
                return False
            
            if maximum <= node.val:
                return False

            return validateBST(node.left, minimum, node.val) and validateBST(node.right, node.val, maximum)
        
        return validateBST(root, -float('inf'), float('inf'))