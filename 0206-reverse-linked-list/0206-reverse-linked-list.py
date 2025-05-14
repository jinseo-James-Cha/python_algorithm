# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None

        while head:
            temp = head.next # keeping moving by connection, so save this connection in temp
            
            head.next = node # attach node into next
            node = head # attach head's val and node into node

            head = temp
        return node


# Recursive version
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next:
#             return head

#         new_head = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None
#         return new_head