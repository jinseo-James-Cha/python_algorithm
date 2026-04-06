from collections import deque, defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # network 1 ~ n
        # u -> v with weight
        
        # starting from node k return minimum time for all visit
        # return -1 if not possible to visit
        
        # reset all with INF
        # and visit from starting node and neighbor, renew the weight
        # dijkstra
        
        graph = defaultdict(list)
        for src, tg, w in times:
            graph[src].append((tg, w))
        
        # graph[2] = [(1,1), (3,1)]
        # graph[3] = [(4, 1)]
        
        
        network = [float('inf')] * (n+1) # node -1 in network
        network[0] = 0 # node starts from 0 so this is not reachable
        network[k] = 0 # starting node has no weight
        
        queue = [(0, k )] # weight, node in queue
        while queue:
            weight, curr = heapq.heappop(queue)
            if network[curr] < weight:
                continue
            
            for neighbor, new_w in graph[curr]:
                if network[neighbor] > weight + new_w:
                    network[neighbor] = weight + new_w
                    heapq.heappush(queue, (network[neighbor], neighbor))
                
        return -1 if max(network) == float('inf') else max(network)