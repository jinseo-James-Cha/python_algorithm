from collections import deque
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        # dp
        #   a b b a b a
        # a 1 0 0 1 0 1
        # b 0 2 1 0 2 0
        # b 0 1 3 0 1 0
        # a 1 0 0 4 0 2
        # b
        # a
        length = len(s)
        dp = [[0] * (length + 1) for _ in range(length + 1)]
        max_length = 0

        for i in range(1, length + 1):
            for j in range(i + 1, length + 1):
                if s[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_length = max(max_length, dp[i][j])
        return max_length


        # binary search range 0 ~ len(s)-1
        # time complexity: O(n^2 log n)
        def is_found_repeating_substring(s, size):
            seen = set()
            for i in range(len(s) - size + 1):
                curr = s[i : i + size]
                if curr in seen:
                    return True
                seen.add(curr)
            return False

        def version(s, size):
            curr = s[:size]
            queue = deque(curr)
            seen = set()
            seen.add(tuple(curr))
            for i in range(size, len(s)):
                queue.popleft()
                queue.append(s[i])
                t = tuple(queue)
                if t in seen:
                    return True
                seen.add(t)
            return False


        left = 1
        right = len(s) - 1 # this is the maximum len of repeating without overlaps
        max_len = 0
        while left <= right:
            mid = (left + right) // 2
            if version(s, mid):
                max_len = max(max_len, mid)
                left = mid + 1
            else:
                right = mid - 1
        return max_len



        # brute force
        # o(n**3) o of cubed 
        curr_size = len(s) - 1

        for size in range(len(s) - 1, 0, -1):
            seen = set()
            for i in range(len(s) - size+1):
                end = i
                curr_sub = s[end: end+size]
                if curr_sub in seen:
                    return size
                
                seen.add(curr_sub)
        
        return 0
