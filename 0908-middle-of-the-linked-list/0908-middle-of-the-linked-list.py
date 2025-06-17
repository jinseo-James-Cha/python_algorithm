# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# how can I solve fast.next.next is nonetype issue
# when the node has even numbers
# 1 2 3 4 5 6
# F   F   F 
# S S S
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head # 1 2
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        