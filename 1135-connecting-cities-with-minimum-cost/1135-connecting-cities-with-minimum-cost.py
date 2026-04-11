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
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        """
        n and cities 1 ~ n
        
        connections[i] = x <-cost-> y

        all connections with minimum cost -> kruskal
        - MST
        - Union Find
        """

        # sort by cost in ascending order
        connections.sort(key=lambda x:x[2])
        total_cost = 0

        uf = UnionFind(n+1)
        connected = 0
        for u,v,w in connections:
            if uf.union(u,v):
                total_cost += w
                connected += 1
        
        return total_cost if connected == n-1 else -1