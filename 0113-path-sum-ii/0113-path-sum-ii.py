# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, curr, remaining):
            nonlocal res
            if not node:
                return
            
            curr.append(node.val)
            if remaining == node.val and not node.left and not node.right:
                res.append(curr[:])
            else:
                if node.left:
                    dfs(node.left, curr, remaining - node.val)
                
                if node.right:
                    dfs(node.right, curr, remaining - node.val)
            curr.pop()

        res = []
        dfs(root, [], targetSum)
        return res
            