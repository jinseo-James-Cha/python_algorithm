# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # v2 : Morris -> space(1)
        res = []
        current = root
        while current:
            if current.left is None:
                res.append(current.val)
                current = current.right
            else:
                predecessor = current.left
                # move to the left subtree's rightmost
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right

                # first visit -> create link
                if predecessor.right is None:
                    predecessor.right = current
                    res.append(current.val)
                    current = current.left
                else:
                    # second bisit -> remove link and move to right
                    predecessor.right = None
                    current = current.right
        return res

                





        # v1: dfs
        # def dfs(node: TreeNode):
        #     if not node:
        #         return
        #     res.append(node.val)
        #     dfs(node.left)
        #     dfs(node.right)
        
        # res = []
        # dfs(root)
        # return res