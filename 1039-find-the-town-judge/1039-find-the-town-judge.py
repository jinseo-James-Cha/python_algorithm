from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # 1 ~ n
        # town judge -> trust nobody
        # others -> trusts town judge

        # greedy
        if not trust:
            return 1 if n == 1 else -1 
            
        d = defaultdict(int)
        candidates = [True] * (n + 1)

        for k, v in trust:
            candidates[k] = False
            d[v] += 1
        
        for k, v in d.items():
            if v == n - 1 and candidates[k] == True:
                return k
        return -1