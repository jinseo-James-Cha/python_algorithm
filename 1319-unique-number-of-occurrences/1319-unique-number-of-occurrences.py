from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # count and then check number is taken or not?
        occ = defaultdict(int)
        for a in arr:
            occ[a] += 1
        
        uniq = set()
        for v in occ.values():
            if v in uniq:
                return False
            uniq.add(v)
        
        return True