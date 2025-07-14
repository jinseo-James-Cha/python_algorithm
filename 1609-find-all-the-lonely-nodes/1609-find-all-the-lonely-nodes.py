# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        
        def dfs(node: TreeNode, isLonely: bool = False):
            if not node:
                return

            if isLonely:
                res.append(node.val)

            dfs(node.left, not node.right)
            dfs(node.right, not node.left)
        res = []
        dfs(root, False)
        return res 