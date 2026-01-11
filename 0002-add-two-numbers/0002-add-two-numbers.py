# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """

        9 9 9 9 9 9
        9 9 9 9 

        """
        plus_one = False
        res = ListNode()
        dummy = res
        while l1 or l2 or plus_one:
            curr_total = 0
            if l1:
                curr_total += l1.val
                l1 = l1.next
            
            if l2:
                curr_total += l2.val
                l2 = l2.next
            
            curr_total += int(plus_one)
            plus_one = curr_total >= 10
            dummy.next = ListNode(curr_total % 10)
            dummy = dummy.next
        return res.next
            
