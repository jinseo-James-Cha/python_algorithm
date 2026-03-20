class Solution:
    def longestDupSubstring(self, s: str) -> str:
        """
        possible answer 
        0 ~ len(s)-1

        binary search length
        if found substring -> move longer length
        if not, move shorter length

        b a n a n a = len 6

        start 3
        """
        left = 1
        right = len(s) - 1

        max_len = 0
        longest_substring = ""
        while left <= right:
            length = (left + right) // 2

            if length < max_len:
                break

            seen = set()
            updated = False
            for i in range(len(s) - length + 1): # 6 - 3 + 1
                curr_str = s[i:i+length]
                if curr_str in seen and max_len < length:
                    max_len = length
                    longest_substring = curr_str
                    updated = True
                else:
                    seen.add(curr_str)
            if updated:
                left = length + 1
            else:
                right = length - 1
        return longest_substring


        






        # brute force -> MLE
        # check all substrings and save in set
        # return the longest
        # time complexity = O(n^2)
        # memory complexity = O(n^2)
        max_len = 0
        res =  ""
        seen = set()
        for i in range(len(s)):
            curr = s[i]
            if curr in seen and len(curr) > max_len:
                max_len = len(curr)
                res = curr
            else:
                seen.add(curr)
            for j in range(i+1, len(s)):
                curr += s[j]
                if curr in seen and len(curr) > max_len:
                    max_len = len(curr)
                    res = curr
                else:
                    seen.add(curr)
        return res