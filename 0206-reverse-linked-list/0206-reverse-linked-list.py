# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1 -> 2 -> 3 -> 4 -> 5 -> None
        """
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev