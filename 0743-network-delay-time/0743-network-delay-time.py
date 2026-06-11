from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Dijkstra algorithm - heapq
        """
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))

        network_time = [float('inf')] * (n + 1)
        network_time[0] = 0
        network_time[k] = 0

        queue = [(0, k)]
        while queue:
            curr_time, curr_node = heapq.heappop(queue)
            if curr_time > network_time[curr_node]:
                continue
            
            for next_node, next_time in graph[curr_node]:
                total_time = next_time + curr_time
                if network_time[next_node] > total_time:
                    network_time[next_node] = total_time
                    heapq.heappush(queue, (total_time, next_node))
        
        return -1 if max(network_time) == float('inf') else max(network_time)
