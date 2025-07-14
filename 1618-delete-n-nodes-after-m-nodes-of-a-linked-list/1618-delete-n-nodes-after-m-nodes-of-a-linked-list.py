# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        # dummy = ListNode()
        # dummy.next = head
        # i = 0
        # while head:
        #     if i < m-1: # 0 < 2-1
        #         i += 1 # 1
        #     else:
        #         j = 0
        #         while j < n and head.next: # 0 < 3 
        #             head.next = head.next.next
        #             j += 1
        #         i = 0
        #     head = head.next
        # return dummy.next

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
            # move left as many as m
            i = 0
            while m > i and left.next:        
                left = left.next
                i +=1 

            # copy left to right
            right = left

            # move right as many as n
            j = 0
            while n > j and right.next:
                right = right.next
                j += 1
            
            # if j moved as many as n, remove in between
            # if not, it is the end
            if n == j:
                left.next = right.next
            else:
                left.next = None
        
        return dummy.next