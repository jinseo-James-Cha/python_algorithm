from collections import defaultdict, deque

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
    
    def isConnected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # BFS
        if not edges:
            return True
        
        adjacent_list = defaultdict(list)
        for u, v in edges:
            adjacent_list[u].append(v)
            adjacent_list[v].append(u)
        
        visited = [False] * n
        visited[source] = True
        queue = deque([source])
        while queue:
            vertex = queue.popleft()
            if vertex == destination:
                return True
            
            for neighbor in adjacent_list[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return False
        
        # Union Find
        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a,b)
        
        return uf.isConnected(source, destination)


        adjacent_list = defaultdict(list)
        
        for u, v in edges:
            adjacent_list[u].append(v)
            adjacent_list[v].append(u)

        # BFS
        queue = deque([source])
        visited = [False] * n
        visited[source] = True

        while queue:
            vertex = queue.popleft()
            if vertex == destination:
                return True
            
            for neighbor in adjacent_list[vertex]:
                if visited[neighbor] == False:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        return False

        # DFS
        def dfs(vertex, visited):
            if vertex == destination:
                return True
            
            visited.add(vertex)
            for neighbor in adjacent_list[vertex]:
                if neighbor not in visited:
                    if dfs(neighbor, visited):
                        return True
            
            return False

        adjacent_list = defaultdict(list)
        for a, b in edges:
            adjacent_list[a].append(b)
            adjacent_list[b].append(a)
        
        return dfs(source, set())

        # DFS
        def dfs(node: int) -> bool:
            if node == destination:
                return True
            for neighbor in adjacent_list[node]:
                if not seen[neighbor]:
                    seen[neighbor] = True
                    if dfs(neighbor):
                        return True
            return False

        adjacent_list = defaultdict(list)
        
        for u, v in edges:
            adjacent_list[u].append(v)
            adjacent_list[v].append(u)

        seen = [False] * n
        seen[source] = True
        return dfs(source)

        # BFS
        adjacent_list = defaultdict(list)
        
        for u, v in edges:
            adjacent_list[u].append(v)
            adjacent_list[v].append(u)

        # # BFS
        seen = [False] * n
        seen[source] = True
        queue = deque([source])

        while queue:
            curr_node = queue.popleft()
            if curr_node == destination:
                return True
            
            for next_node in adjacent_list[curr_node]:
                if not visited[next_node]:
                    seen[next_node] = True
                    queue.append(next_node)

        return False
