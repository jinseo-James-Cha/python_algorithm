class Solution:
    def longestDupSubstring(self, s: str) -> str:
        """
        find duplicate substring 
        return longest length duplicate substring

        constraint
        longest length => len(s) - 1
        minimum length => 1
        if nothing duplicated => 0

        brute force -> TLE
        check all substrings and return the longest

        - peusocode
        loop maximum size first 
            initialize a set to check dup
            create a substring
            check if it is already in the set
              if yes, return the current size
              if no, add in the set

        time complexity = O(n^3)
        space complexity = O(n^2)
        """
        # binary search
        def get_duplicate_substring(s, size):
            duplicates = set()
            for i in range(len(s) - size + 1): # 6 - 3 = 3 -> 0 1 2 3
                curr_str = s[i:i+size]
                if curr_str in duplicates:
                    return curr_str
                duplicates.add(curr_str)
            return ""

        n = len(s)
        left = 1 # minimum
        right = n-1 # maximum
        longest_dup = ""
        longest_len = 0
        while left <= right:
            curr_size = (left + right) // 2 # 1 + 5
            duplicate_string = get_duplicate_substring(s, curr_size)
            if longest_len < len(duplicate_string):
                longest_dup = duplicate_string
                longest_len = len(duplicate_string)
                left = curr_size + 1
            else:
                right = curr_size - 1

        return longest_dup

        # brute force
        # banana
        n = len(s) # 6
        for curr_size in range(n-1, 0, -1): # 5
            duplicates = set()
            for i in range(n - curr_size + 1): # 6 - 5 +1 => 0, 1
                curr_substring = s[i:i + curr_size] # 0:0+5, 1:1+5
                if curr_substring in duplicates:
                    return curr_substring
                duplicates.add(curr_substring)

        return ""


        