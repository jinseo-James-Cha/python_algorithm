# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class HeapNode:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # take out minimum using min heap

        pq = []
        for head in lists:
            if head:
                heapq.heappush(pq, HeapNode(head))
        
        res = ListNode()
        dummy = res
        while pq:
            heap_node = heapq.heappop(pq)
            
            smallest_node = heap_node.node
            dummy.next = smallest_node
            dummy = dummy.next

            if smallest_node.next:
                smallest_node = smallest_node.next
                heapq.heappush(pq, HeapNode(smallest_node))
        
        return res.next