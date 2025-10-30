# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # recursive
        if not p and not q:
            return True
        
        if not p and q:
            return False
        
        if p and not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)






        # BFS

        def check(pp:TreeNode, qq:TreeNode):
            if not pp and not qq:
                return True
            if not pp or not qq:
                return False
            if pp.val != qq.val:
                return False
            return True
        queue = deque([(p, q)])
        while queue:
            curr_p, curr_q = queue.popleft()

            if not check(curr_p, curr_q):
                return False
            
            if curr_p:
                queue.append((curr_p.left, curr_q.left))
                queue.append((curr_p.right, curr_q.right))
            
        return True




        # DFS
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if  p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)