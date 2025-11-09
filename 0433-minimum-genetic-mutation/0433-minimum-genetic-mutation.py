from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
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
