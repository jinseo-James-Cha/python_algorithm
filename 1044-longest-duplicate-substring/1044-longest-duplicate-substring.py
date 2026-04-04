class Solution:
    def longestDupSubstring(self, s: str) -> str:
        # Binary Search + Rabin-Karp + Rolling hash
        # Time complexity = O(N log N)
        # Space Complexity = O(N)
        """
        #Hashing
        b = 1
        c = 2
        d = 3
        H = (1 * 26^2) + (2 * 26^1) + (3 * 26^0) = 676 + 52 + 3 = 731

        #Rolling
        if it is decimal system, 12345
        123 -> 234
        1. remove 1 -> 1 * base10^2 -> 23
        2. times by base10-> 230
        3. add the next number 4 -> 234

        Hash(new) = (Hash(prev) - C(out)*base26) * base 26 + C(in)

        #Module
        to prevent hashing collision
        MOD = 10**9 + 7
        H = (H % MOD)
        """
        def search_dup(length):
            if length == 0:
                return -1
            
            h = 0
            for i in range(length):
                h = (h * base + nums[i]) % MOD
            
            seen = {h}
            aL = pow(base, length-1, MOD) 
            for start in range(1, len(s) - length + 1):
                # Hash(new) = (Hash(prev) - C(out)*base26) * base 26 + C(in)
                h = ((h - nums[start - 1] * aL) * base + nums[start + length - 1]) % MOD

                if h in seen:
                    return start
                seen.add(h)
            
            return -1


        MOD = 2**63 - 1
        base = 26
        n = len(s)

        nums = [ord(s[i]) - ord('a') for i in range(n)]

        start_idx = -1
        left, right = 1, n-1 # acceptable length for the answer, minimum 1 maximum n-1
        while left <= right:
            curr_length = (left + right) // 2

            found_dup = search_dup(curr_length)
            if found_dup != -1:
                max_len = curr_length
                start_idx = found_dup
                left = curr_length + 1
            else:
                right = curr_length - 1
                
        if start_idx != -1:
            return s[start_idx : start_idx + max_len]
        return ""




        # binary search for length
        # if found substring -> move longer length
        # if not, move shorter length        
        # Time complexity = O(N^2 log N)
        # Space Complexity = O(N^2)
        left = 1
        right = len(s) - 1

        max_len = 0
        longest_substring = ""
        while left <= right:
            length = (left + right) // 2

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
        # time complexity = O(n^3)
        # memory complexity = O(n^3)
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