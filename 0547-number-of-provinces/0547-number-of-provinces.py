class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size # == depth, how many childrend in this node
    
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
        # DFS
        def dfs(city):
            visited[city] = True

            for j in range(len(isConnected)):
                if isConnected[city][j] and not visited[j]:
                    dfs(j)

        n = len(isConnected)
        num_of_province = 0
        visited = [False] * n

        for i in range(n):
            if not visited[i]:
                num_of_province += 1
                dfs(i)
        return num_of_province

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
        
        print(uf.parent) 
        print(uf.rank)
        return num_of_province

        
