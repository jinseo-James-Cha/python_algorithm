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
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        DSU = UnionFind(n) # Disjoint Set Union
        for x, y in pairs:
            DSU.union(x, y)
        
        parent = [DSU.find(i) for i in range(n)]
        d = defaultdict(deque)
        
        for i in range(n):
            d[parent[i]].append(s[i])

        for key in d:
            d[key] = deque(sorted(d[key]))

        res = ""
        for i in range(n):
            d_key = parent[i]
            res += d[d_key].popleft()
        return res