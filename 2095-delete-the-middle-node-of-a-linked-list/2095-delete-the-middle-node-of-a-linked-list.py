# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # slow and fast pointers
        # like two pointers and stop at the middle
        # prev.next = prev.next.next
        # prev -> prev.next -> prev.next.next
        
        # causion -> even num -> right middle
        #   1 2 3 4
        #     s
        #       f
        #   2 1
        #   s
        #     f

        #   1 3 4 7 1 2 6
        #       s
        #             f
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        
        return dummy.next