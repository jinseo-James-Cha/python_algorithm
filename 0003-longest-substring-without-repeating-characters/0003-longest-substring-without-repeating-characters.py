# sliding window feeling !
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # do it again with proper sliding door
        # remove left and left += 1 keep checking its in there or not
        longest = 0
        left = 0
        window = set()
        for right in range(len(s)):
            # why I cannot understand how to remove dups
            # need to keep the order.. to remove in respectively
            while s[right] in window:
                # remove s[right] in window
                # use left pointer to remove by order
                window.remove(s[left])
                left += 1  # move to right
            
            window.add(s[right])
            longest = max(longest, right - left + 1)
        return longest
                


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
