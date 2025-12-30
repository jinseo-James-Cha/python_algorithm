# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # LCA
        # between p and q as the lowest 
        # who is the common ancestor for the both p and q.
        def dfs(root):
            nonlocal lca
            if not root:
                return False
            
            # if p or q reaches curr_node .. return its.
            left = dfs(root.left)
            right = dfs(root.right)
            myself = root == p or root == q

            if left + myself + right >= 2:
                lca = root
            
            return left or myself or right
            

            # how to stop when we meet one of p or q
            # and keep moving lower ?
            # p and q will be root left or right.. how to check them?
            # 4 ways... and if 2 >= return root
        lca = None
        dfs(root)
        return lca

            