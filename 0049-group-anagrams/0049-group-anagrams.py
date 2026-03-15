from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # counting
        d = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            d[tuple(count)].append(s)
        
        return list(d.values())




        d = defaultdict(list)
        for s in strs:
            sorted_s = sorted(s)
            d[tuple(sorted_s)].append(s)
        
        res = []
        for v in d.values():
            res.append(v)
        return res
            