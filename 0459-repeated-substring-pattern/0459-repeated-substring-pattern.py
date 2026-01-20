class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
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
