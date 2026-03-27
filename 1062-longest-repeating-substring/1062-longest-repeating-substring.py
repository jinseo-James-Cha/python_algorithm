from collections import deque
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        # Binary Search and Rabin-Karp
        # time complexity: O(n log n)
        # Hash(new) = (Hash(prev) - C(out)*base26) * base 26 + C(in)
        n = len(s)
        base = 26
        mod = 2**63 - 1

        def check(size):
            h = 0
            for i in range(size):
                h = (h * base + (ord(s[i]) - ord('a'))) % mod
            
            seen = {h}
            baseL = pow(base, size, mod)  # base^L % mod

            for i in range(1, n - size + 1):
                h = (h * base - (ord(s[i-1]) - ord('a')) * baseL + (ord(s[i+size-1]) - ord('a'))) % mod
                if h in seen:
                    return True
                seen.add(h)
            return False

        left, right = 1, n - 1
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
       
        # dp 
        # time complexity: O(n^2)
        # using 2D dp table => i, j
        # concept: if s[i] == s[j] 
        # if two different positions' letter are the same,
        # add + 1 from prev position from the both, i-1 and j-1
        length = len(s)
        dp = [[0] * (length + 1) for _ in range(length + 1)]
        max_length = 0

        for i in range(1, length + 1):
            for j in range(i + 1, length + 1):
                if s[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_length = max(max_length, dp[i][j])
        return max_length


        # binary search 
        # time complexity: O(n^2 log n)
        # range 0 ~ len(s)-1 -> log n
        # is_found_repeating_substring -> n^2
        def is_found_repeating_substring(s, size):
            seen = set()
            for i in range(len(s) - size + 1):
                curr = s[i : i + size]
                if curr in seen:
                    return True
                seen.add(curr)
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
