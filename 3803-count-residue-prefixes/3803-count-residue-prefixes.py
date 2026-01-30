class Solution:
    def residuePrefixes(self, s: str) -> int:
        
        curr = ""
        count = 0
        for ch in s:
            curr += ch
            if len(curr) % 3 == len(set(curr)):
                count += 1
        return count