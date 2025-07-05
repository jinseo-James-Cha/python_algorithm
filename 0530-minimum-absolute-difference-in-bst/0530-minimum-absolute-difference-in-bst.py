# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
            
        res = []
        dfs(root)
        minimum = float(inf)
        for i in range(len(res) - 1):
            temp = res[i + 1] - res[i]
            minimum = min(temp, minimum)
        return minimum