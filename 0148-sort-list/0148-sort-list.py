# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        sort ?
        what can I choose to sort linkedlist?
        - cannot have random access through indexing -> no QuickSort

        divide     4->2->1->3      
        divide   4->2     1->3
        divide 4     2 1     3
        merge   2->4     1->3
        merge     1->2->3->4 

        # divide half in linked list -> using slow&fast pointers
        # merge -> compare first and second list and move next list until one is done
        """

        def find_second_half(head):
            slow = fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            
            second_half = slow.next
            slow.next = None
            return second_half
        
        def merge_lists(first_list, second_list):
            merged_list = ListNode()
            dummy = merged_list
            
            while first_list and second_list:
                if first_list.val < second_list.val:
                    dummy.next = first_list
                    first_list = first_list.next
                else:
                    dummy.next = second_list
                    second_list = second_list.next
                dummy = dummy.next
            
            dummy.next = first_list if first_list else second_list
            return merged_list.next

        if not head or not head.next:
                return head
            
        second_half_head = find_second_half(head)
        
        first_half_sorted = self.sortList(head)
        second_half_sorted = self.sortList(second_half_head)
        
        return merge_lists(first_half_sorted, second_half_sorted)

    