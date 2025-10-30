# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def dfs(left_idx, right_idx):
            if left_idx > right_idx:
                return None
            
            val = postorder.pop()
            root = TreeNode(val)
            root_idx = inorder_idx[val]

            root.right = dfs(root_idx+1, right_idx)
            root.left = dfs(left_idx, root_idx-1)
            return root
        
        inorder_idx = { v: k for k, v in enumerate(inorder)}
        return dfs(0, len(postorder)-1)


        def dfs(left_idx, right_idx):
            if left_idx > right_idx:
                return None
            
            val = postorder.pop() # 3
            root = TreeNode(val)
            
            index = idx_map[val] # 1

            root.right = dfs(index+1, right_idx) # 2, 4
            root.left = dfs(left_idx, index - 1) # 0, 0
            return root
        
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return dfs(0, len(inorder) - 1)