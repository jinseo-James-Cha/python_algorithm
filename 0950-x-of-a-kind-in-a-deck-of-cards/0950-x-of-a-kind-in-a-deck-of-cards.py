from collections import Counter
from math import gcd
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counter = list(Counter(deck).values())
        
        res = counter[0]
        for i in range(1, len(counter)):
            res = gcd(res, counter[i])
        
        return res > 1