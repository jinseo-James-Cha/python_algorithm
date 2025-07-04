# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # BST
        # Q. 1 is the minimum all the time in BST? -> should return 1 once we meet?
        # minimum difference between any two nodes? -> need to save vals
        # check abs(node.val, arr[i]) -> save in minimum?
        # traverse all nodes and save in array?
        # and sort?
        # and sliding window by 2 elements?

        # Approaching
        # use inorder traverse cuz of BST left child < parent < right child
        # and save each node val into array -> ascending order
        # compare two pairs 
        
        # DFS inorder in BST
        def dfs(node: TreeNode):
            if not node:
                return

            dfs(node.left)
            vals.append(node.val)
            dfs(node.right)
            
        vals = []
        dfs(root)
        minimum = float(inf)
        for i in range(len(vals) - 1):
            minimum = min(abs(vals[i] - vals[i+1]), minimum)
        return minimum