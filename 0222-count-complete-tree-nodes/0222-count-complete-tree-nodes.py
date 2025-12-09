# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # BFS
        if not root:
            return 0
        queue = deque([root])
        res = 0
        while queue:
            res += len(queue)
            for _ in range(len(queue)):
                curr_node = queue.popleft()
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
        return res

        

        # DFS
        if not root:
            return 0
        
        return self.countNodes(root.left) + self.countNodes(root.right) + 1






        # what do we need to have?
        # idk... let me count the number of node
        count = 0
        if not root:
            return count
            
        queue = deque([root])
        while queue:
            node = queue.popleft()
            count += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return count
        
        