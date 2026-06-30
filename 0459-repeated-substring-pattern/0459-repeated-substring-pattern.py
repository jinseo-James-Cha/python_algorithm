class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        abab

        a bab aba b
          ab ab
        """
        t = s + s
        if s in t[1:-1]:
            return True
        return False


        # brute force
        # check all size 1 to n/2
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                pattern = s[:i] * (n // i)
                if s == pattern:
                    return True
        return False