# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy = head
        greater, less = ListNode(0, head), ListNode(0, head)
        greater_head = greater
        less_head = less
        while dummy:
            if dummy.val >= x:
                greater.next = dummy
                greater = greater.next
            else:
                less.next = dummy
                less = less.next
            dummy = dummy.next
        
        if greater.next:
            greater.next = None
        less.next = greater_head.next
        return less_head.next
