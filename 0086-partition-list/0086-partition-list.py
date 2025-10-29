# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        
        greater = greater_head = ListNode(0)
        less = less_head = ListNode(0)
        while head:
            if head.val >= x:
                greater.next = head
                greater = greater.next
            else:
                less.next = head
                less = less.next
            head = head.next
        
        if greater.next:
            greater.next = None
        less.next = greater_head.next
        return less_head.next
