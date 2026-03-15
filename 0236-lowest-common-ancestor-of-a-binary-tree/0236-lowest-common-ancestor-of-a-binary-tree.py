# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # bfs
        parents = {root: None}
        pq = deque([root])
        while pq:
            node = pq.popleft()
            if node.left:
                parents[node.left] = node
                pq.append(node.left)
            if node.right:
                parents[node.right] = node
                pq.append(node.right)
        
        p_ancestors = set()
        while p:
            p_ancestors.add(p)
            p = parents[p]

        while q not in p_ancestors:
            q = parents[q]
        
        return q

        # dfs post order traversal
        # score
        def dfs(node):
            nonlocal lca
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            myself = 1 if node == p or node == q else 0
            if left + right + myself >= 2:
                lca = node
            
            return left or right or myself
        
        lca = None
        dfs(root)
        return lca
