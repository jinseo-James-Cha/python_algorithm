# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Lowest Common Ancester
        # me? -> 1
        # left? -> 1
        # right? -> 1
        # if 2 == this is the answer

        # this is not Binary Search Tree, so I don't care the range.
        def dfs(node, p, q):
            nonlocal res
            if not node:
                return 0
            
            score = 0
            if node == p or node == q:
                score += 1
            
            if dfs(node.left, p, q):
                score += 1
            
            if dfs(node.right, p, q):
                score += 1
            
            if score == 2:
                res = node
            
            return score
        
        res = None
        dfs(root, p, q)
        return res

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

            