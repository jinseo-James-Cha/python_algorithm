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
        xset, yset = self.find(x), self.find(y)

        if xset == yset:
            return False
        
        if self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        elif self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        else:
            self.parent[xset] = yset
            yset += 1
        
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # union find
        if len(edges) != n-1:
            return False

        uf = UnionFind(n)
        res = n
        for a,b in edges:
            if not uf.union_set(a, b):
                return False
        return True





        if len(edges) != n-1:
            return False
            
        def dfs(node: int):
            if node in seen:
                return
            seen.add(node)
            for l in adjacent_list[node]:
                dfs(l)

        adjacent_list = defaultdict(list)
        for a, b in edges:
            adjacent_list[a].append(b)
            adjacent_list[b].append(a)
        
        seen = set()
        dfs(0)
        return len(seen) == n

        # 1. intuition
        # 0 ~ n - 1
        # edges[i] = [ai, bi] undirected <->
        # save label with level?
        # what is the valid tree? using one directional?
        # checking b and it should be come once only

        # 2. complexity
        # time: o(n)
        # space: o(n)

        # 3. data structure
        # hashmap: ajacent_list
        # array: seen
        # if len(edges) != n-1:
        #     return False

        # def dfs(node, parent):
        #     if node in seen:
        #         return False
        #     seen.add(node)
            
        #     for neighbour in adjacent_list[node]:
        #         if neighbour == parent:
        #             continue
        #         if neighbour in seen:
        #             return False
        #         if not dfs(neighbour, node):
        #             return False
        #     return True
                
        # adjacent_list = defaultdict(list)
        # seen = set()
        # for a, b in edges:
        #     adjacent_list[a].append(b)
        #     adjacent_list[b].append(a)

        # return dfs(0, -1) and len(seen) == n
        
       
            
            
