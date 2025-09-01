# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # tail recursion with bfs
        def bfs(q, max_depth):
            if not q:
                return max_depth
            
            current_node, current_depth = q.pop()
            max_depth = max(max_depth, current_depth)
            if current_node.left:
                q.append((current_node.left, current_depth + 1))
            if current_node.right:
                q.append((current_node.right, current_depth + 1))
            
            # tail recursion
            return bfs(q, max_depth)
        
        if not root:
            return 0
        
        return bfs([(root, 1)], 0)


        # recursion
        if root is None:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))







        def dfs(node: TreeNode):
            if not node:
                return 0
            
            return 1 + max(dfs(node.left), dfs(node.right))
        return dfs(root)
        