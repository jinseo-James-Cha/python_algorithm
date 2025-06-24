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
        # Define comparison based on ListNode's value
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # using min heap -> heapq
        
        # put all linked list in to heapq
        heap = []
        for head in lists:
            if head:
                heapq.heappush(heap, HeapNode(head))
        
        res = ListNode(-1)
        cur = res
        while heap:
            heap_node = heapq.heappop(heap)
            smallest_node = heap_node.node
            cur.next = smallest_node
            cur = cur.next

            if smallest_node.next:
                heapq.heappush(heap, HeapNode(smallest_node.next))

        return res.next
