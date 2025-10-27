# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time O(N)
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         # I think I can use two pointer and right - left = n
#         # once right arrives the end
#         # left arrives where we need to remove..
#         # but we need to reach one node bofore the target node we will remove
#         # head.next = head.next.next -> remove the next pointer.
#         answer = ListNode(-1)
#         answer.next = head
#         left = right = answer
#         # move right first
#         for _ in range(n):
#             right = right.next
#             if not right:
#                 return head

#         while right.next:
#             right = right.next
#             left = left.next

#         # remve the tarket node
#         left.next = left.next.next

#         return answer.next

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for i in range(n + 1):
            first = first.next
            print(first)

        while first is not None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next