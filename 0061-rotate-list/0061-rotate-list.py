# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        if k == 0:
            return head
        
        n = 1
        dummy = head
        while dummy.next:
            n += 1
            dummy = dummy.next
        dummy.next = head # n == 5


        new_head = head
        for _ in range(n - k % n):
            new_head = new_head.next
            dummy = dummy.next
        dummy.next = None
        return new_head
        

        