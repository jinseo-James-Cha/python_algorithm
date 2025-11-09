from collections import deque
import heapq
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # dijkstra algorithm
        if startGene == endGene:
            return 0
        
        dist = {}
        for b in bank:
            dist[b] = float('inf')
        dist[startGene] = 0

        if endGene not in dist:
            return -1

        q = [(0, startGene)]
        while q:
            d, curr_str = heapq.heappop(q)
            if d > dist.get(curr_str, float('inf')):
                continue
            
            if curr_str == endGene:
                return d
            
            for i in range(len(curr_str)):
                for ch in 'ACGT':
                    if curr_str[i] == ch:
                        continue
                    
                    neighbor_str = curr_str[:i] + ch + curr_str[i+1:]
                    if neighbor_str in dist and dist.get(neighbor_str, float('inf')) > dist[curr_str] + 1:
                        dist[neighbor_str] = dist[curr_str] + 1
                        heapq.heappush(q, (dist[neighbor_str], neighbor_str))
        return -1






        # BFS
        # shortest path from startGene to endGene
        # bank saves all edges
        if startGene == endGene:
            return 0
        
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1

        visited = set()
        queue = deque([(startGene, 0)])
        while queue:
            curr_str, curr_d = queue.popleft()
            
            for i, c in enumerate(curr_str):
                for choice in ['A', 'C', 'G', 'T']:
                    if c == choice:
                        continue
                    
                    temp_str = curr_str[:i] + choice + curr_str[i+1:]
                    if temp_str in bank_set and temp_str not in visited:
                        if temp_str == endGene:
                            return curr_d + 1
                        visited.add(temp_str)
                        queue.append((temp_str, curr_d+1))
        return -1
