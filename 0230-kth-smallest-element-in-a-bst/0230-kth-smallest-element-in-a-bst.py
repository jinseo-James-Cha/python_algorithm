# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # need to check all nodes? even tho it is BST?
        # left is smaller, right is greater ?

        #If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
        # the smallest -> leftmost
        # and then parent
        # and then right child...
        # inorder ?
        res = []
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        inorder(root)
        return res[k-1]



        # bruth force -> get all vals and sort and k-1
        vals = []
        def dfs(node):
            if not node:
                return
            
            vals.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        vals.sort()
        return vals[k-1]