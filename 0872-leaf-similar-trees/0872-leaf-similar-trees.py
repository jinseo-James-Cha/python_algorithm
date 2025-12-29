# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1 = []
        leaves2 = []

        def dfs(root, leaves):
            if not root:
                return
            
            if not root.left and not root.right:
                leaves.append(root.val)
            dfs(root.left, leaves)
            dfs(root.right, leaves)
        
        dfs(root1, leaves1)
        dfs(root2, leaves2)
        return leaves1 == leaves2


        def dfs(root):
            leaves = []
            if not root:
                return []
            
            if not root.left and not root.right:
                leaves.append(root.val)
            
            leaves += dfs(root.left)
            leaves += dfs(root.right)
            return leaves

        root1_vals = dfs(root1)
        root2_vals = dfs(root2)
        
        return root1_vals == root2_vals



    

