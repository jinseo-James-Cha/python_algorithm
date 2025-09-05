# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS
        if not root:
            return []
            
        res = []
        queue = deque([root])
        while queue:
            current = []
            for _ in range(len(queue)):
                node = queue.popleft()
                current.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(current)

        return res
        # 1. intuition
        # BFS every queue make temp [] and put into res at the end of each loop

        # 2. complexicy
        # BFS : O(N)

        # 3. data structure
        # queue = deque
        # temp =  List[int], 
        # res = List[List[int]]

        if not root:
            return []

        res = []
        queue = deque([root])
        while queue:
            temp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(temp)
        return res



        