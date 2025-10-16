from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]

        d = defaultdict(list)
        for s in strs:
            # how to make a str as unique key into dict's key
            temp_list = sorted(s)
            temp_str = "".join(temp_list)
            d[temp_str].append(s)

        res = []
        for v in d.values():
            res.append(v)
        return res

        