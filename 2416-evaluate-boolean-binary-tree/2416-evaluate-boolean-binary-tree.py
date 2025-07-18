# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode):
            if not node:
                return True
            
            l = dfs(node.left)
            r = dfs(node.right)
            if node.val == 2:
                return bool(l or r)
            elif node.val == 3:
                return bool(l and r)
            else:
                return bool(node.val)

        return dfs(root)