# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # l1.var + l1.var + prev(0 default 1 from previous sums) % 10
        # go to the end of each list and save
        def reverse_linkedlist(root):
            prev = None
            while root:
                temp = root.next
                root.next = prev
                prev = root
                root = temp
            return prev

        reversed_l1 = reverse_linkedlist(l1)
        reversed_l2 = reverse_linkedlist(l2)
        
        total_sum = 0
        carry = 0
        ans = ListNode()
        while reversed_l1 or reversed_l2:
            if reversed_l1:
                total_sum += reversed_l1.val
                reversed_l1 = reversed_l1.next
            if reversed_l2:
                total_sum += reversed_l2.val
                reversed_l2 = reversed_l2.next
            
            carry, ans_val = divmod(total_sum , 10)
            ans.val = ans_val
            head = ListNode(carry)
            head.next = ans
            ans = head
            total_sum = carry
        
        return ans.next if carry == 0 else ans