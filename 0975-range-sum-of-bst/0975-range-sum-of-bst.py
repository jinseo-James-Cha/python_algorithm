# v2: iterative 
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
        return ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # BST
        # left child is less than parent
        # right child is greater than parent.
        # left -> low < val < high
        # right -> parent < val < high
        # I think we can use recursive..
        # but no idea how to make..
        s = 0
        def addSum(node, low, high):
            nonlocal s
            if not node:
                return 0
                        
            if low <= node.val <= high:
                s += node.val
            
            if node.val > low:
                addSum(node.left, low, high)

            if node.val < high:
                addSum(node.right, low, high) 
        addSum(root, low, high)
        return s


        


        