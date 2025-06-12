# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # BST!!!!
        # uh !? return the value in the BST that is closest to the target?! print the smallest.
        # this is not about BFS ?!!! closest and smallest?!

        # keep tracking minumum gap beween val and target
        res = []
        minimum = float('inf')
        q = deque([root])

        while q:
            cur = q.popleft() # root
            if abs(cur.val - target) < minimum:
                # new closest came
                # reset minimum and candidate
                res = [cur.val]
                minimum = abs(cur.val - target)
            elif abs(cur.val - target) == minimum:
                # add another candidate
                res.append(cur.val)

            # next level
            # optimize with target num and BST 
            if cur.left and cur.val > target:
                q.append(cur.left)
            if cur.right and cur.val < target:
                q.append(cur.right)
        
        return min(res)
