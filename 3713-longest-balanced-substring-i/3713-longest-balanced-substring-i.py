from collections import defaultdict
class Solution:
    def longestBalanced(self, s: str) -> int:
        """
        brute force
        check all substring
        time: o(n^2)
        """

        longest = 1
        for i in range(len(s)):
            curr = defaultdict(int)
            for j in range(i, len(s)):
                curr[s[j]] += 1
                if len(set(curr.values())) == 1:
                    longest = max(longest, j - i + 1)

        return longest