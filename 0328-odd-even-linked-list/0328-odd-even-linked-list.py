# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # odd and even
        # 1 2 3 4 5
        # odd1 3 5 even2 4 
        if not head or not head.next:
            return head

        odd_head = ListNode()
        odd_list = odd_head
        even_head = ListNode()
        even_list = even_head
        is_odd = True
        while head:
            if is_odd:
                odd_list.next = head
                odd_list = odd_list.next
            else:
                even_list.next = head
                even_list = even_list.next
            head = head.next
            is_odd = not is_odd
        
        even_list.next = None
        odd_list.next = even_head.next
        return odd_head.next
