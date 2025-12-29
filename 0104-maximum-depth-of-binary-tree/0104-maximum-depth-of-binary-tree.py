# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # bfs
        if not root:
            return 0
        
        queue = [(root, 1)]
        max_depth = 1
        while queue:
            curr_node, curr_depth = queue.pop()
            max_depth = max(max_depth, curr_depth)
            if curr_node.left:
                queue.append((curr_node.left, curr_depth + 1))
            if curr_node.right:
                queue.append((curr_node.right, curr_depth + 1))
        return max_depth


        # dfs
        if not root:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1