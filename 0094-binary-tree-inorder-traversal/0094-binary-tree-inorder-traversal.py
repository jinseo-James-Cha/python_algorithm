# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# try #2 stack
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = [] 
#         stack = [] # stack, LIFO

#         while root or stack:
#             while root:
#                 stack.append(root)
#                 root = root.left
            
#             root = stack.pop()
#             res.append(root.val)
#             root = root.right
        
#         return res



# try # 1 recursive
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # YES BT problem.
        # inorder

        res = [] 
        # go left -> root (myself) -> go right
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        
        inorder(root)
        return res
        
            