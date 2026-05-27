# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # BFS
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()

            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        
        ancesters = set()
        while p:
            ancesters.add(p)
            p = parent[p]
        
        while q not in ancesters:
            q = parent[q]
        return q



        # DFS
        def dfs(node):
            nonlocal lca
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            curr = node == p or node == q
            if left + right + curr >= 2:
                lca = node
            return left or right or curr

        lca = None
        dfs(root)
        return lca