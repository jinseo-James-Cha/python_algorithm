# my solition 3 - built-in function reverse Beat 100%
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse() # can use in list not str type

# my solution 2 - two pointer
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         # left ->
#         # right <-
#         left = 0
#         right = len(s) - 1 # index
#         while right - left > 0:
#             s[left], s[right] = s[right], s[left]
#             left += 1
#             right -= 1


# my solition 1 - recursion
# slicing is creating new list, so it won't change the original
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         # space O(1)
#         return self.reverse(s, 0, len(s) - 1)
    
#     def reverse(self, s: List[str], start, end) -> List[str]:
#         if end - start < 1:
#             return s
#         s[start], s[end] = s[end], s[start]
#         start += 1
#         end -= 1
#         return self.reverse(s, start, end)
