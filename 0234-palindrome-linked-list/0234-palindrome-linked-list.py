# Follow up: Could you do it in O(n) time and O(1) space?
class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur:
            temp = cur.next # save to keep moving forward
            cur.next = prev
            prev = cur
            cur = temp # return back to moving forward
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # define size and come to the middle ?
        # send tracker to the tail and check?
        # can I print reverse?
        # and save size in int 

        # use two pointers
        # slow moves one
        # fast moves two
        # slow arrives at the middle when fast arrives the end
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        
        rev = self.reverse(slow) 
        # reverse slow?! why?! # rev 54321
        # I got it !
        # now slow is at the mid!
        # after slow is all the second half!!
        # so, reverse the second half == slow and compare with head!
        while rev:
            if head.val != rev.val:
                return False
            head = head.next
            rev = rev.next
        return True


# my solution V1
# using stack to save all values from linked list
# MLE (Memory Limit Exceeded)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def check_first_and_last(self, s):
#          # now check first and last one
#         if len(s) <= 1:
#             return True
#         elif s[0] != s[-1]:
#             return False
#         return self.check_first_and_last(s[1:-1])

#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         stack = []
#         cur = head
#         while cur is not None:
#             stack.append(cur.val)
#             cur = cur.next
#         return self.check_first_and_last(stack)

        
        