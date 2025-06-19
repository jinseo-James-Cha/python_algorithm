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
        # left edge + right edge?
        diameter = 0
        def moveToNextDepth(node):
            if not node:
                return -1
            nonlocal diameter

            # move till the leaf 
            left_path = moveToNextDepth(node.left) 
            right_path = moveToNextDepth(node.right)

            # out and +2 
            diameter = max(diameter, left_path + right_path + 2)
            print(node.val, diameter)

            return max(left_path, right_path) + 1

        moveToNextDepth(root)
        return diameter