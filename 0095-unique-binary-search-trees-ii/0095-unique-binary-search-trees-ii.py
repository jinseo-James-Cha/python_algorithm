# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dp(start, end):
            res = []
            if start > end:
                res.append(None)
                return res
            
            if (start, end) in memo:
                return memo[(start, end)]
            
            for i in range(start, end + 1):
                leftSubTrees = dp(start, i - 1)
                rightSubTrees = dp(i+1, end)

                for left in leftSubTrees:
                    for right in rightSubTrees:
                        root = TreeNode(i, left, right)
                        res.append(root)
            memo[(start, end)] = res
            return res
        memo = {}
        return dp(1, n)