# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # always even number...
        # if n 4
        # I move ->
        # save into 0 1 and then 1 0

        # if n 6
        # 0 5
        # 1 4
        # 2 3
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        
        # if n 4 -> 0 + 3 and 1 + 2
        n = len(vals)
        res = [0] * (n//2)
        for i in range(n//2):# 0, 1, 2
            res[i] += vals[i] + vals[n-i-1] # 0 + [4-0-1] 0 + 3 /////// 1 + 4-1-1 2 ///// 2 + 6- 2-1 3
        return max(res)
