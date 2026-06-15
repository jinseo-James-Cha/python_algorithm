# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1 2 3 4
          S
              F

        1 2 3 4 5
          S
              F
        1 2
        S
          F      
        """
        # Fast and Slow pointers - two pointers
        if not head.next:
            return None

        dummy = ListNode()
        dummy.next = head
        slow, fast = dummy, dummy

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = slow.next.next
        return dummy.next