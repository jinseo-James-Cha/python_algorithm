class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.ranl = [0] * size
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xset, yset = self.find(x), self.find(y)
        if xset == yset:
            return False

        if self.parent[xset] < self.parent[yset]:
            self.parent[xset] = yset
        elif self.parent[xset] > self.parent[yset]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        connected = 0
        for a, b in edges:
            if uf.union(a, b):
                connected += 1
        
        return n - connected






        def dfs(node):
            visited[node] = True
        
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        num_of_connected = 0
        visited = [False] * n
        for node in range(n):
            if not visited[node]:
                num_of_connected += 1
                dfs(node)

        return num_of_connected
