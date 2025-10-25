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
        if head is None:
            return head

        def cloneOldToNew(node):
            if node:
                if node in copied_hashmap:
                    return copied_hashmap[node]
                else:
                    copied_node = Node(node.val, None, None)
                    copied_hashmap[node] = copied_node
                    return copied_hashmap[node]
            return None

        old_node = head
        new_node = Node(old_node.val, None, None)
        copied_hashmap = {}
        copied_hashmap[old_node] = new_node
        while old_node:
            new_node.next = cloneOldToNew(old_node.next)
            new_node.random = cloneOldToNew(old_node.random)

            new_node = new_node.next
            old_node = old_node.next
        return copied_hashmap[head]
