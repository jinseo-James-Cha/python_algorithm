# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode() # return node.next after the below answer has all nodes
        answer = node # move answer to save all other nodes

        while list1 and list2:
            if list1.val < list2.val:
                answer.next = list1
                list1 = list1.next
            else:
                answer.next = list2
                list2 = list2.next
            answer = answer.next
        
        # merge the rest
        answer.next = list1 if list1 else list2
        
        return node.next