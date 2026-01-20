class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Knuth-Morris-Pratt
        # O(n + m)
        m = len(needle)
        n = len(haystack)
        if n < m:
            return -1

        lps = [0] * m
        prev = 0
        i = 1
        while i < m:
            if needle[i] == needle[prev]:
                # Length of Longest Border Increased
                prev += 1
                lps[i] = prev
                i += 1
            else:
                # Only empty border exist
                if prev == 0:
                    lps[i] = 0
                    i += 1
                # Try finding longest border for this i with reduced prev
                else:
                    prev = lps[prev - 1]
        
        haystack_pointer = 0
        needle_pointer = 0

        while haystack_pointer < n:
            if haystack[haystack_pointer] == needle[needle_pointer]:
                needle_pointer += 1
                haystack_pointer += 1

                if needle_pointer == m:
                    return haystack_pointer - m
            else:
                if needle_pointer == 0:
                    haystack_pointer += 1
                else:
                    needle_pointer = lps[needle_pointer - 1]
        return -1
        

        # O(nm)
        for i in range(0, len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
        