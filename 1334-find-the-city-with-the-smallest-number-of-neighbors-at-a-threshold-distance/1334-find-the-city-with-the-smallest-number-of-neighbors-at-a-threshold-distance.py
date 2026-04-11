class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        """
        n = num of cities 0 ~ n-1 label
        edges[i] = [from, to, weight] => from <-weight->-> to => bidirected
        distanceThreshold 


        return the city 0 ~ n-1
        with smallest number of cities that are reachable through some path
        and whose distance is at most distanceThreshold

        if multiple, max(candidates)


        I need to check a distance from a to b or even a to c to b -> floyd warshall
        if the distance <= distanceThreshold count city += 1
        return the smallest num with and highest city label if there are multiple
        """
        d = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            d[i][i] = 0

        for u,v,w in edges:
            d[u][v] = min(d[u][v], w)
            d[v][u] = min(d[v][u], w)

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if d[i][j] > d[i][k] + d[k][j]:
                        d[i][j] = d[i][k] + d[k][j]

        cities = [0] * n
        for i in range(n):
            for j in range(n):
                if i != j and d[i][j] <= distanceThreshold:
                    cities[i] += 1
    
        min_count = float('inf')
        result_city = -1
        for i, cnt in enumerate(cities):
            if cnt <= min_count:
                min_count = cnt
                result_city = i
        return result_city


