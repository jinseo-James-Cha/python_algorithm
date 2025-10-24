"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        def cloneNode(node):
            if node:
                if node in visited:
                    return visited[node]
                else:
                    newNode = Node(node.val, None, None)
                    visited[node] = newNode
                    return visited[node]
            return None

        old_node = head
        new_node = Node(head.val, None, None)
        visited = {}
        visited[old_node] = new_node
        while old_node:
            new_node.random = cloneNode(old_node.random)
            new_node.next = cloneNode(old_node.next)

            old_node = old_node.next
            new_node = new_node.next
        return visited[head]
