# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # bfs
        if not root:
            return 0
        
        queue = deque([(root, 1)])
        max_depth = 0
        while queue:
            curr_node, depth = queue.popleft()
            max_depth = max(max_depth, depth)
            if curr_node.left:
                queue.append((curr_node.left, depth+1))
            if curr_node.right:
                queue.append((curr_node.right, depth+1))
        
        return max_depth

        # dfs, recursive
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # top down recursive
        def top_down(node, depth):
            if not node:
                return depth
            return max(top_down(node.left, depth+1), top_down(node.right, depth+1))
        
        return top_down(root, 0)








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
        