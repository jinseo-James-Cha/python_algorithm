# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        head = ListNode()
        dummy = head
        while list1 and list2:
            l1_val = list1.val
            l2_val = list2.val

            if l1_val >= l2_val:
                dummy.next = list2
                list2 = list2.next
            else:
                dummy.next = list1
                list1 = list1.next
            
            dummy = dummy.next
        
        # while list1:
        #     dummy.next = list1
        #     list1 = list1.next
        #     dummy = dummy.next

        # while list2:
        #     dummy.next = list2
        #     list2 = list2.next
        #     dummy = dummy.next
        dummy.next = list1 if list1 is not None else list2
        return head.next
        