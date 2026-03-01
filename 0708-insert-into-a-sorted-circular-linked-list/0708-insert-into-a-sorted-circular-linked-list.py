"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        # find a node which has smaller than insertVal
        # and insert a new node there
        if not head:
            newNode = Node(insertVal, None)
            newNode.next = newNode
            return newNode

        prev, curr = head, head.next
        toInsert = False
        
        while True:
            if prev.val <= insertVal <= curr.val:
                # case 1: when found in between 
                toInsert = True
            elif prev.val > curr.val:
                # case 2: 
                # - the new value is the maximum, so need to put at the tail
                # - the new value is the minimum, so need to put at the beginning(== tail)
                if insertVal >= prev.val or insertVal <= curr.val:
                    toInsert = True

            if toInsert:
                prev.next = Node(insertVal, curr)
                return head
            
            prev, curr = prev.next, curr.next
            if prev == head:
                break
        
        # case 3:
        # nowhere to put new val
        prev.next = Node(insertVal, curr)
        return head