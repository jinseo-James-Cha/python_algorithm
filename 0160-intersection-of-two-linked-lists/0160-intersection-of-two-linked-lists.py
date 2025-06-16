
#  wow this the kick
# I have to remember this for later haha
# time -> O(n + m)
# space -> O(1)
# idea is making the same length
# for example
# a : 123 789
# b : 56 789
# new a = a + b = 12378956 789
# new b = b + a = 56789123 789
# so easy to get 789 as intersection
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptr_A, ptr_B = headA, headB
        
        while ptr_A != ptr_B:
            ptr_A = ptr_A.next if ptr_A else headB
            ptr_B = ptr_B.next if ptr_B else headA
        
        return ptr_A

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         # return the intersected node
#         # get the length of the both linked lists and get the gap
#         # move long linked list for the gap
#         # and then check next is the same or not
#         m = n = 0
#         headA_len = headA
#         headB_len = headB

#         while headA_len.next:
#             headA_len = headA_len.next
#             m += 1
#         while headB_len.next:
#             headB_len = headB_len.next
#             n += 1

#         # 5, 6
#         if m > n:
#             for _ in range(m-n):
#                 headA = headA.next
#         if m < n:
#             for _ in range(n-m):
#                 headB = headB.next

#         while headA and headB:
#             if headA == headB:
#                 return headA

#             headA = headA.next
#             headB = headB.next
#         return None