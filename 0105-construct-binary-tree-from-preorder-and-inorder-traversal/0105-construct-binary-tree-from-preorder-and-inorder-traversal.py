# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(left_idx, right_idx):
            if left_idx > right_idx:
                return None
            
            val = queue.popleft()
            root = TreeNode(val)
            val_idx = inorder_idx[val]
            root.left = dfs(left_idx, val_idx-1)
            root.right = dfs(val_idx+1, right_idx)
            return root

        queue = deque(preorder)
        inorder_idx = {val: key for key, val in enumerate(inorder)}
        return dfs(0, len(inorder)-1)
