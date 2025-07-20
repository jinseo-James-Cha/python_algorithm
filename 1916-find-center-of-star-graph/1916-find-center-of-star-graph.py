class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        cnt = [0] * (n + 2)

        for u, v in edges:
            cnt[u] += 1
            cnt[v] += 1
        
        res = 0
        for i, c in enumerate(cnt):
            if c == n:
                res = i
        return res