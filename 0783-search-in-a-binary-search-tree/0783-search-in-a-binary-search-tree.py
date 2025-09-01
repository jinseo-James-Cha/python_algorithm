# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return []
        
        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        
        return self.searchBST(root.right, val)





        # BST!!
        # val == me -> [me, left, right]

        while root and root.val != val:
            root = root.left if val < root.val else root.right
        return root
    
    # v2:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None or val == root.val:
            return root
            
        return self.searchBST(root.left, val) if val < root.val \
            else self.searchBST(root.right, val)