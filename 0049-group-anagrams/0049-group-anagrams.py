from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            sorted_s = sorted(s)
            d[tuple(sorted_s)].append(s)
        
        res = []
        for v in d.values():
            res.append(v)
        return res
            