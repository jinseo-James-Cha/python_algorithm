# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res
        
        dq = deque()
        dq.append(root)
        while dq:
            temp = []
            for _ in range(len(dq)):
                node = dq.popleft()
                temp.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(temp)
        return res

# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         def addVal(answer, node: Optional[TreeNode], depth):
#             answer[depth].append(node.val)
#             return answer

#         if not root:
#             return []
        
#         answer = []
#         d = 0
#         answer = addVa(answer, root, d)

#         return self.levelOrder(root.left) + self.levelOrder(root.right)

        # answer = [[root.val]]
        # cur = root
        # while cur.left or cur.right:
        #     temp = []
        #     if cur.left:
        #         temp.append(cur.left.val)
        #     if cur.right:
        #         temp.append(cur.right.val)
        #     answer.append(temp)
        #     cur = cur.left if cur.left else cur.right

        # print(answer)
        

        