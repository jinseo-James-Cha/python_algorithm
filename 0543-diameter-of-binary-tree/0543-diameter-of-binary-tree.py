# cannot understand this well, solve later again

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # DFS
       
        def dfs(node):
            if not node:
                return -1
            nonlocal diameter

            left_path = dfs(node.left) 
            right_path = dfs(node.right)
            diameter = max(diameter, left_path + right_path + 2)

            return max(left_path, right_path) + 1

        diameter = 0
        dfs(root)
        return diameter