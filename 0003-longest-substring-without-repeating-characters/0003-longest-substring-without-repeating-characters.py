# sliding window feeling !
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = max_length = 0
        char_set = set()
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length



# 0 <= s.length <= 5 * 10^4 -> O(N)
# from collections import deque
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         m = 0
#         dq = deque()

#         left = 0
#         for right in range(len(s)):
#             temp = 1
#             while s[right] in dq:
#                 dq.popleft()
#                 left += 1
            
#             dq.append(s[right])
#             m = max(len(dq), m)
#         return m
