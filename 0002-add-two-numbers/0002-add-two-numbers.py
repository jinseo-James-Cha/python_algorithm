# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        dummy = res
        is_carry = False

        while l1 or l2 or is_carry:
            l1_val = 0 
            if l1 is not None:
                l1_val = l1.val
                l1 = l1.next
            
            l2_val= 0 
            if l2 is not None:
                l2_val = l2.val
                l2 = l2.next

            is_carry, remainder = divmod(l1_val+l2_val+is_carry, 10)
            curr_node = ListNode(remainder)
            dummy.next = curr_node
            dummy = dummy.next
        
        return res.next
        