# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# v3 : optimize with fast and slow pinters
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False


# v2: two pointers: fast and slow pointers
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        left = head
        right = head.next
        while left.next and right.next:
            if left == right:
                return True
            left = left.next
            right = right.next
        return False


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # how do I define it is cycle linked list or just long linked list?
        # 3 -> 2 next == -4 -> 2 next will be the name
        # can we compare them ? yes we can compare linked lists
        # let's use two pointer
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True
        
        return False
        