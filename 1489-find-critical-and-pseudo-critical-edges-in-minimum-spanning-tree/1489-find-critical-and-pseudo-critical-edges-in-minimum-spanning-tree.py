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
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        """
        n -> node named 0 ~ n -1

        edges[i] ->  a <---weight---> b

        MST -> without cycle ->#edge = n-1 and minimum weights

        find all critical and pseudo-critial edges
        # critical edge => exclude an edge and its mst > base mst(all included mst)
        # pseudo edge => include an enge and its mst == base mst => it is part of mst

        and return the edges indices

        한 엣지를 지운 MST랑 base MST 비교해서
        - 지운 MST가 더 커졌다?
        → 아 이 엣지는 반드시 필요했구나 → critical

        - 지운 MST가 안 커졌다?
        → 아직 모름 (pseudo 아님)

        → 그 다음,
            이 엣지를 "강제로 포함"해서 MST 만들었을 때

            - base MST랑 같았다?
            → 이 엣지는 MST에 포함될 수 있음 → pseudo

        """
        def kruskal(exclude, include):
            uf = UnionFind(n)
            cost = 0
            
            # add the include edge first
            connected_edge = 0
            if include != -1:
                u, v, w, idx = edges_with_idx[include]
                if uf.union(u, v):
                    cost += w
                    connected_edge +=1

            # basic kruskal and exclude one edge
            for i, (u, v, w, idx) in enumerate(edges_with_idx):
                if i == exclude:
                    continue
                if uf.union(u, v):
                    cost += w
                    connected_edge +=1
            
            return cost if connected_edge == n - 1 else float('inf')

        uf = UnionFind(n)

        edges_with_idx = [edge + [i] for i, edge in enumerate(edges)]
        edges_with_idx.sort(key=lambda x:x[2])

        base = kruskal(-1, -1)

        critical = []
        pseudo = []
        for i in range(len(edges_with_idx)):
            # exclude check
            # exclude the edge and more than base? -> critical
            if kruskal(i, -1) > base:
                critical.append(edges_with_idx[i][3]) 
            # include check
            # include the edge and the same as base? -> pseudo
            elif kruskal(-1, i) == base:
                pseudo.append(edges_with_idx[i][3])
        
        return [critical, pseudo]