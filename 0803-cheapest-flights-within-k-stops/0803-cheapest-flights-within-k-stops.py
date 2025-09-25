from collections import defaultdict, deque
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # from, to, price = flights[i]
        # at most k stops

        # bellman-ford
        dist = [float('inf')] * n
        dist[src] = 0

        for _ in range(k+1):
            temp = dist[:]
            for u, v, w in flights:
                if dist[u] != math.inf:
                    temp[v] = min(temp[v], dist[u] + w)
            
            dist = temp
        
        return -1 if dist[dst] == float('inf') else dist[dst]

        
        # no negative values -> dijkstra?
        graph = defaultdict(list)
        for f, t, p in flights:
            graph[f].append((t, p))

        stops = [float('inf')] * n

        # [current cost, current node, num of stops]
        pq = [0, src, 0]
        while pq:
            dist, node, step = heapq.heappop(pq)

            if step >= stops[node] or step > k + 1:
                continue
            
            stops[node] = step

            if node == dst:
                return dist
            
            for neighbor, price in graph[node]:
                heapq.heappush(pq, (dist+price, neighbor, step + 1))
        
        return -1









        # bfs
        graph = defaultdict(list)
        for f, t, p in flights:
            graph[f].append((t, p))
        
        
        dist = [math.inf] * n
        dist[src] = 0

        queue = deque([(src,0)])
        stops = 0
        while stops <= k and queue:
            size = len(queue)
            new_dist = dist[:]
            for _ in range(size):
                node, cost = queue.popleft()
                for neighbor, price in graph[node]:
                    if cost + price < new_dist[neighbor]:
                        new_dist[neighbor] = cost + price
                        queue.append((neighbor, new_dist[neighbor]))
            dist = new_dist
            stops += 1
        
        return -1 if dist[dst] == math.inf else dist[dst]

