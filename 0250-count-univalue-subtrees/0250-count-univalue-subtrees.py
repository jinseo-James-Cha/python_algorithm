# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node):
            nonlocal res

            if not node:
                return True
            
            isLeftUniValue = dfs(node.left)
            isRightUnivalue = dfs(node.right)
            if isLeftUniValue and isRightUnivalue:
                if node.left and node.val != node.left.val:
                    return False
                if node.right and node.val != node.right.val:
                    return False
                res += 1
                return True
            return False
        
        res = 0
        dfs(root)
        return res
    