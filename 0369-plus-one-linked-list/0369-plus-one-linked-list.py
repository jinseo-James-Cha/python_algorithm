# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode):
            prev = None
            curr = node
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        reversedHead = reverse(head)
        
        carry = 1
        curr = reversedHead
        prev = None

        while curr and carry:
            total = curr.val + carry
            curr.val = total % 10
            carry = total // 10

            prev = curr
            curr = curr.next

        if carry:
            prev.next = ListNode(carry)

        return reverse(reversedHead)