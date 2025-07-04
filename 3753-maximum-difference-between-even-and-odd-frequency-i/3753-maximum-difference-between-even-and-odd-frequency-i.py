from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        max_odd = float(-inf)
        min_even = float(inf)
        
        c = Counter(s)
        for v in c.values():
            if v % 2 == 0:
                min_even = min(min_even, v)
            else:
                max_odd = max(max_odd, v)
        
        return max_odd - min_even
                
                