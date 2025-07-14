# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        # left moves m
        # copy left into right
        # right moves n
        # left.next = right.next

        # back to first again
        # til right reach end before n -> left.next and end
        dummy = ListNode()
        dummy.next = head

        left = dummy
        while left.next:
            i = 0
            while m > i and left.next:        
                left = left.next
                i +=1 

            right = left
            j = 0
            while n > j and right.next:
                right = right.next
                j += 1
            
            if n == j:
                left.next = right.next
            else:
                left.next = None
        
        return dummy.next