# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # good node == root -> x there are no nodes with a value greater than X
        #          3
        #       1      4
        # here 3<=     here 4<=
        # keep updating maximum.. and curr val >= maximum count += 1 and reset maximum

        # bfs
        res = 0
        queue = deque([(root, float('-inf'))])
        while queue:
            node, maximum = queue.popleft()
            if node.val >= maximum:
                res += 1
                maximum = node.val
            if node.left:
                queue.append((node.left, maximum))
            if node.right:
                queue.append((node.right, maximum))
        return res


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