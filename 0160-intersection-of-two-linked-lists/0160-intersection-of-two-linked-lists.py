# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # return the intersected node
        # get the length of the both linked lists and get the gap
        # move long linked list for the gap
        # and then check next is the same or not
        m = n = 0
        headA_len = headA
        headB_len = headB

        while headA_len.next:
            headA_len = headA_len.next
            m += 1
        while headB_len.next:
            headB_len = headB_len.next
            n += 1

        # 5, 6
        if m > n:
            for _ in range(m-n):
                headA = headA.next
        if m < n:
            for _ in range(n-m):
                headB = headB.next

        while headA and headB:
            if headA == headB:
                return headA

            headA = headA.next
            headB = headB.next
        return None