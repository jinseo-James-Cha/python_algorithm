# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # insertion sort
        dummy = ListNode()
        curr = head

        while curr:
            prev = dummy
            while prev.next and prev.next.val <= curr.val:
                prev = prev.next

            temp = curr.next

            # 기존
            curr.next = prev.next
            prev.next = curr

            curr = temp
        
        return dummy.next    


        
        

        return head