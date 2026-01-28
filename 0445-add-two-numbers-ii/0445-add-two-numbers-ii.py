# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # stack
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        curr = ListNode()
        while s1 or s2:
            curr_s1, curr_s2 = 0, 0
            if s1:
                curr_s1 = s1.pop()
            
            if s2:
                curr_s2 = s2.pop()
            
            total = carry + curr_s1 + curr_s2
            curr.val = total % 10
            carry = total // 10
            next_node = ListNode(carry)
            next_node.next = curr
            curr = next_node
        
        return curr.next if carry == 0 else curr


        def reverseLinkedList(root):
            prev = None
            curr = root
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        reverse_l1 = reverseLinkedList(l1)
        reverse_l2 = reverseLinkedList(l2)
        carry = 0
        head = ListNode()
        dummy = head
        while reverse_l1 or reverse_l2:
            curr_l1_val, curr_l2_val = 0, 0
            if reverse_l1:
                curr_l1_val = reverse_l1.val
                reverse_l1 = reverse_l1.next
            
            if reverse_l2:
                curr_l2_val = reverse_l2.val
                reverse_l2 = reverse_l2.next
            
            total = carry + curr_l1_val + curr_l2_val
            node = ListNode(total % 10)
            dummy.next = node
            dummy = dummy.next
            carry = total // 10
        
        if carry:
            dummy.next = ListNode(carry)
        
        # return reverse back
        return reverseLinkedList(head.next)

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