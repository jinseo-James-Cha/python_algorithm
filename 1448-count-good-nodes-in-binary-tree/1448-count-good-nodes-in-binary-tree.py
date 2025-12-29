# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # good node == root -> x there are no nodes with a value greater than X
        #          3
        #       1      4
        # here 3<=     here 4<=
        # keep updating maximum.. and curr val >= maximum count += 1 and reset maximum
        def dfs(node, maximum):
            nonlocal count
            if not node:
                return

            if node.val >= maximum:
                count += 1
                maximum = node.val

            dfs(node.left, maximum)
            dfs(node.right, maximum)
        
        count = 0
        dfs(root, root.val)
        return count