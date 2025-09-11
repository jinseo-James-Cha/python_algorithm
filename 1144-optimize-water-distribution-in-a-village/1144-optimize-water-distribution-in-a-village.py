class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size+1))
        self.rank = [0] * (size+1)
    
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
    
    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        ordered_edges = []
        for index, weight in enumerate(wells):
            ordered_edges.append((weight, 0, index + 1))

        for h1, h2, weight in pipes:
            ordered_edges.append((weight, h1, h2))
        
        ordered_edges.sort(key=lambda x: x[0])

        uf = UnionFind(n)
        total_cost = 0
        for cost, h1, h2 in ordered_edges:
            if uf.union(h1, h2):
                total_cost += cost
        
        return total_cost
