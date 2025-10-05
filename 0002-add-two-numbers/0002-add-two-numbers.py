# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        is_next = False
        res = ListNode()
        dummy = res
        while l1 or l2:
            l1_num = 0
            l2_num = 0

            if l1:
                l1_num = l1.val
                l1 = l1.next

            if l2:
                l2_num = l2.val
                l2 = l2.next

            prev = 0
            if is_next:
                is_next = False
                prev = 1

            curr = l1_num + l2_num + prev

            if curr >= 10:
                is_next = True
                curr %= 10
            
            new_node = ListNode(curr)
            dummy.next = new_node
            dummy = dummy.next
        
        if is_next:
            new_node = ListNode(1)
            dummy.next = new_node
        return res.next

        