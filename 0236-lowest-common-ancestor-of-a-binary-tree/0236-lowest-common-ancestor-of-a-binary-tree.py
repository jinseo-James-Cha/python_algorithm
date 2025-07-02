# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # DFS recursive
        def dfs(node: TreeNode, p: TreeNode, q: TreeNode) -> bool:
            nonlocal lca
            if not node:
                return False

            nodeIsPOrQ = node == p or node == q
            leftPOrQ = dfs(node.left, p, q)
            rightPorQ = dfs(node.right, p, q)

            if nodeIsPOrQ + leftPOrQ + rightPorQ == 2:
                lca = node
            
            return (nodeIsPOrQ or leftPOrQ or rightPorQ)

        lca = None
        dfs(root, p, q)
        return lca