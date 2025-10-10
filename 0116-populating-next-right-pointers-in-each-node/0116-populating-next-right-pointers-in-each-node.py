"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # bfs
        # queue
        # 1
        # 3 2
        if not root:
            return root
        
        queue = deque([root])
        while queue:
            size = len(queue)
            prev = None
            for _ in range(size):
                node = queue.popleft()
                node.next = prev
                prev = node

                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        
        return root

