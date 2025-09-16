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


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim's algorithm
        n = len(points)
        mst_cost = 0
        edges_used = 0
        
        # Track nodes which are visited.
        visited = [False] * n
        
        min_dist = [math.inf] * n
        min_dist[0] = 0
        
        while edges_used < n:
            curr_min_edge = math.inf
            curr_node = -1
            
            # Pick least weight node which is not in MST.
            for node in range(n):
                if not visited[node] and curr_min_edge > min_dist[node]:
                    curr_min_edge = min_dist[node]
                    curr_node = node
            
            mst_cost += curr_min_edge
            edges_used += 1
            visited[curr_node] = True
            
            # Update adjacent nodes of current node.
            for next_node in range(n):
                weight = abs(points[curr_node][0] - points[next_node][0]) +\
                         abs(points[curr_node][1] - points[next_node][1])
                
                if not visited[next_node] and min_dist[next_node] > weight:
                    min_dist[next_node] = weight
        
        return mst_cost
        
        # Prim's algorithm - by adding vertices
        n = len(points)
        visited = [False] * n
        heap = [(0,0)]

        mst_cost = 0
        edges_used = 0
        while edges_used < n:
            weight, curr_node = heapq.heappop(heap)

            if visited[curr_node]:
                continue
            
            visited[curr_node] = True
            mst_cost += weight
            edges_used += 1

            for next_node in range(n):
                if not visited[next_node]:
                    next_weight = abs(points[curr_node][0] - points[next_node][0]) + abs(points[curr_node][1] - points[next_node][1])
                    heapq.heappush(heap, (next_weight, next_node))
            
        return mst_cost








        # Kruskal's algorithm - by adding edges
        n = len(points)
        all_edges = []

        # save all edges between nodes with its weight
        for curr_node in range(n):
            for next_node in range(curr_node+1, n):
                weight = abs(points[curr_node][0] - points[next_node][0]) + abs(points[curr_node][1] - points[next_node][1])
                all_edges.append((weight, curr_node, next_node))
        
        # sort by weight
        all_edges.sort()

        # UnionFind 
        # connect all nodes with one
        uf = UnionFind(n)
        mst_weight = 0
        edges_used = 0 # to count n-1 is done.

        for weight, curr_node, next_node in all_edges:
            if uf.union(curr_node, next_node):
                mst_weight += weight
                edges_used += 1
            
            if edges_used == n-1:
                break
        return mst_weight
        
        