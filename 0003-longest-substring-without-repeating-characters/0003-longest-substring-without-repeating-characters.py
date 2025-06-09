# sliding window feeling !

# 0 <= s.length <= 5 * 10^4 -> O(N)
from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        dq = deque()

        left = 0
        for right in range(len(s)):
            temp = 1
            while s[right] in dq:
                dq.popleft()
                left += 1
            
            dq.append(s[right])
            m = max(len(dq), m)
        return m
