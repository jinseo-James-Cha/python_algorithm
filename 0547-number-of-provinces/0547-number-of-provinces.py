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
    
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        n cities, some connected and some not -> connectivity question
        a - b - c => a and c connected indirectly

        A Province => a group of directly or indirectly connected cities..
        
        1, 1, 0
        1, 1, 0
        0, 0, 1

        - 0, 1, 2 cities..
        - i != j
        - 0 1 connected
        - should I check all ? or n / 2?
        - Indirected Adjacent Graph -> Union Find ?
        """
        n = len(isConnected)
        uf = UnionFind(n)

        num_of_province = n
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    if uf.union(i, j):
                        num_of_province -= 1
        
        return num_of_province

