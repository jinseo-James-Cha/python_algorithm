# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # using morris with inorder -> ascending order
        # res[k-1]

        res = []
        current = root
        while current:
            if current.left is None:
                # visit
                res.append(current.val)
                current = current.right
            else:
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right
                
                # first visit to right? -> link to current
                if predecessor.right is None:
                    predecessor.right = current
                    current = current.left
                else:
                    # already have link? -> remove link and move right
                    predecessor.right = None # reset
                    res.append(current.val)
                    current = current.right
        return res[k-1]
