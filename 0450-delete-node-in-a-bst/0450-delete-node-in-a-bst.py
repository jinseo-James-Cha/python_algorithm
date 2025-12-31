# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # search for a node to remove
        if root.val == key:
            return self.helper(root)
        
        dummy = root
        while root:
            if root.val > key:
                if root.left and root.left.val == key:
                    root.left = self.helper(root.left)
                    break
                else:
                    root = root.left
            else:
                if root.right and root.right.val == key:
                    root.right = self.helper(root.right)
                    break
                else:
                    root = root.right
        return dummy
    
    def helper(self, root):
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        rightChild = root.right
        lastRight = self.flr(root.left)
        lastRight.right = rightChild
        return root.left

    def flr(self, root):
        if root.right is None:
            return root
        return self.flr(root.right)