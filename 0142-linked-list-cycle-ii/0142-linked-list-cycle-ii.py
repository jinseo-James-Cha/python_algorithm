# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        cycle detection in linked list
        return the beginning of linked list

        if no cycle -> return null

        "pos"
        """
        seen = set()
        dummy = head
        while dummy is not None:
            if dummy in seen:
                return dummy
            else:
                seen.add(dummy)
                dummy = dummy.next
        return None