# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        
        # inorder = left -> root -> right
        # postorder = left -> right -> root
        def dfs(left_idx, right_idx):
            if left_idx > right_idx:
                return None
            
            val = postorder.pop()
            root = TreeNode(val)
            val_idx = inorder_index[val]
            
            root.right = dfs(val_idx+1, right_idx)
            root.left = dfs(left_idx, val_idx-1)
            return root
        
        inorder_index = {val: idx for idx, val in enumerate(inorder)}
        return dfs(0, len(inorder)-1)
    
    
    
    