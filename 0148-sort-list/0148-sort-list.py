# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # divide and conquer
        # top down merge sort
        # O(n logn) -> merge sort?!

        if not head or not head.next:
            return head
        
        mid = self.getPartition(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.mergeSortList(left, right)

    def mergeSortList(self, list1, list2):
        dummyHead = ListNode(0)
        tail = dummyHead
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2
        return dummyHead.next
    
    def getPartition(self, head):
        slow = head
        fast = head
        prev = None # to save slow's prev 

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None
        return slow  
