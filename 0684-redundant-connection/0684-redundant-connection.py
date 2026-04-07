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
        
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # connect nodes based on edges order
        # and check if the nodes are already connected?
        # then return the edge
        # using union find
        if not edges:
            return []

        # 3 nodes needs 2 edges only what is the last redundant edge?
        n = len(edges) + 1
        uf = UnionFind(n)

        res = []
        for a, b in edges:
            if not uf.union(a, b):
                res = [a,b]
                break
        return res
