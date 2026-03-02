# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # iterative version
        # save parent[child] = parent
        # save ancestor of all p
        # loop until q not in ancestor
        parent = {root: None}
        stack = [root]
        while p not in parent or q not in parent:
            curr = stack.pop()
            if curr.left:
                parent[curr.left] = curr
                stack.append(curr.left)
            
            if curr.right:
                parent[curr.right] = curr
                stack.append(curr.right)
        
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        
        while q not in ancestors:
            q = parent[q]
        
        return q

        """
        left true
        right true 
        i am the LCA

        """
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


