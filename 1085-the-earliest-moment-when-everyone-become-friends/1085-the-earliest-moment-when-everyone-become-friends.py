class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xset, yset = self.find(x), self.find(y)

        if xset == yset:
            return False
        
        if self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        elif self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        else:
            self.parent[xset] = yset
            self.rank[yset] += 1
        return True


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # timestamp is asc order? no..

        logs.sort(key = lambda x: x[0] )

        # total union should be n
        res = 0

        uf = UnionFind(n)
        for t, x, y in logs:
            if uf.union(x, y):
                res += 1
            
            if res == n-1:
                return t
        
        return -1
        
            