# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # this is the kick !
        # we need the previous node of the target node !!!! -> easy to remove
        # so start from 0 -> new head
        res = ListNode(0, head)

        # dummy will remove node with head pointer, res will return as answer
        # linked list is sharing the address in memory, so make the copy easily
        dummy = res


        # head location - dummy location = n + 1, so lets move head ahead
        # n + 1 is for easy removal as I mentioned.
        # previous node is easier to remove the target node
        for _ in range(n):
            head = head.next

        # now head location - dummy = n + 1
        # let's move all together until head reaches the end
        while head:
            head = head.next
            dummy = dummy.next
        
        # now head is None
        # now dummy is the previous node of the target
        # remove "next node" which is target node
        dummy.next = dummy.next.next

        # good job dummy, return the original of res's next
        return res.next


    