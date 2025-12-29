# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node, is_right_direction, depth):
            nonlocal longest_zigzag
            if not node:
                return
            
            longest_zigzag = max(longest_zigzag, depth)
            
            if is_right_direction:
                dfs(node.right, True, 1)
                dfs(node.left, False, depth + 1)
            else:
                dfs(node.right, True, depth + 1)
                dfs(node.left, False, 1)

            
        longest_zigzag = 0
        dfs(root, False, 0)
        return longest_zigzag