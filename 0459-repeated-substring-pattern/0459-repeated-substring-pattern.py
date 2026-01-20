class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:




        
        # the length should be a divisor
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                pattern = s[:i] * (n // i)
                if s == pattern:
                    return True
        return False



        if len(s) == 1:
            return False

        curr = ""
        i = 0
        while i < len(s):
            if not curr or curr[0] != s[i]:
                curr += s[i]
                i += 1
                continue
            
            j = i
            while j < len(s):
                if curr != s[j:j+len(curr)]:
                    break
                j += len(curr)
            
            if j == len(s):
                return True
            
            curr += s[i]
            i += 1
        return False
