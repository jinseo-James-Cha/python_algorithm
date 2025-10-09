# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # stack
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return res[::-1]




        # recursive
        def postOrder(node):
            if not node:
                return
            
            postOrder(node.left)
            postOrder(node.right)
            res.append(node.val)
        
        res = []
        postOrder(root)
        return res






        res = []
        if not root:
            return res

        # DFS stack
        stack = [root]

        # use root -> right -> left
        # and then reverse 
        while stack:
            node = stack.pop()
            res.append(node.val)
            
            # LIFO stack so put left first and then right -> right first out left out later
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            
        res.reverse()
        return res
        

        # DFS recursive
        # def dfs(node: TreeNode):
        #     if not node:
        #         return
            
        #     dfs(node.left)
        #     dfs(node.right)
        #     res.append(node.val)

        # res = []
        # dfs(root)
        # return res