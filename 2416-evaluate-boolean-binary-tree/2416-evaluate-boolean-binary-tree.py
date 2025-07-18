# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode):
            if node.val == 0:
                return False
            elif node.val == 1:
                return True
            elif node.val == 2:
                return dfs(node.left) or dfs(node.right)
            else: # node.val == 3:
                return dfs(node.left) and dfs(node.right)
        return dfs(root)