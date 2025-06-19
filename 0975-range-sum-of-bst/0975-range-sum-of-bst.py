# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # BST
        # left child is less than parent
        # right child is greater than parent.
        # left -> low < val < high
        # right -> parent < val < high
        # I think we can use recursive..
        s = 0
        def addSum(node, low, high):
            nonlocal s
            
            if not node:
                return 0
            
            if low <= node.val <= high:
                s += node.val
            
            addSum(node.left, low, high)
            addSum(node.right, low, high) 
        addSum(root, low, high)
        return s


        


        