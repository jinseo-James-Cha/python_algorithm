from bisect import bisect_left
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # binary 1-soldier 0-civilian
        # weaker => 1. soldier less 2. if same soldier i < j
        
        # return weakest rows for k much
        # 2 4 1 2 5
        # 2 0 3 1 4
        
        # bucket 
        buckets = [[] for _ in range(len(mat[0]) + 1)]
        for i, m in enumerate(mat):
            soldiers = m.count(1)
            buckets[soldiers].append(i)
        
        res = [x for bucket in buckets for x in bucket]
        return res[:k]

