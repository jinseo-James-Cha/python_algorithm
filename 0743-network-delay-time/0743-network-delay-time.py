from collections import deque, defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Dijkstra algorithm
        """
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))

        network_time = [float('inf')] * (n + 1)
        network_time[0] = 0
        network_time[k] = 0

        queue = deque([(0, k)])
        while queue:
            curr_time, curr_node = queue.popleft()
            if curr_time > network_time[curr_node]:
                continue
            
            for next_node, next_time in graph[curr_node]:
                total_time = next_time + curr_time
                if network_time[next_node] > total_time:
                    network_time[next_node] = total_time
                    queue.append((total_time, next_node))
        
        return -1 if max(network_time) == float('inf') else max(network_time)
