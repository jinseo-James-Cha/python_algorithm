from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union_set(self, x, y):
        xset = self.find(x)
        yset = self.find(y)
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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # union find 
        # disjoint-set data structure
        n = len(isConnected)
        uf = UnionFind(n)
        res = n

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1 and uf.union_set(i,j):
                    res -= 1
        
        return res



        # adjacent list
        def dfs(city):
            visited_cities[city] = True

            for next_city in range(n):
                if isConnected[city][next_city] == 1 and visited_cities[next_city] == False:
                    dfs(next_city)


        n = len(isConnected)
        res = 0
        visited_cities = [False] * n
            
        for city in range(n):
            if visited_cities[city] == False:
                res += 1
                dfs(city)
        return res


        # # DFS X
        # def is_within_bound(row, col):
        #     return 0 <= row < len(isConnected) and 0 <= col < len(isConnected[0])
        
        # def dfs(i, j):
        #     visited[i][j] = True
            
        #     for r, c in DIR:
        #         next_r, next_c = r + i, c + j
        #         if is_within_bound(next_r, next_c) and visited[next_r][next_c] == False and isConnected[next_r][next_c] == 1:
        #             dfs(next_r, next_c)
            
        
        # n = len(isConnected)
        # DIR = [(-1,0), (1,0), (0,-1), (0, 1)]
        # visited = [[False] * n for _ in range(n)]
        # res = 0

        # for i in range(n):
        #     for j in range(n):
        #         if isConnected[i][j] == 1 and visited[i][j] == False:
        #             res += 1
        #             dfs(i,j)

        # return res