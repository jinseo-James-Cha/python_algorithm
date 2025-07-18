# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        # return the sum of every tree node's tilt.
        # root = left + right
        # root = left(3 + 5 + 2) - right( 9 + 7)
        def dfs(node: TreeNode):
            nonlocal sum_of_tilt
            if not node:
                return 0
                
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            tilt = abs(left_sum - right_sum)
            sum_of_tilt += tilt

            return left_sum + right_sum + node.val

        sum_of_tilt = 0
        dfs(root)
        return sum_of_tilt
        
