# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def dfs(node):
            if not node:
                return -1

            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)

            currHeight = max(leftHeight, rightHeight) + 1

            if len(res) <= currHeight:
                res.append([])

            res[currHeight].append(node.val)
            return currHeight

        res = []
        dfs(root)
        return res