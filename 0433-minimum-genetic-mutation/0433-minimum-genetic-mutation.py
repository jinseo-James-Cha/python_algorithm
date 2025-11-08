from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # 8 characters -> A C G T
        # startGene -> endGene
        # AACCGGTT -> AACCGGTA is one mutation
        # bank -> all valid gene mutations

        # AACCGGTT start
        # AAACGGTA end
        # AACCGGTA bank1
        # AACCGCTA bank2
        # AAACGGTA bank3
        
        # AACCGGTT -> AACCGGTAbank1 -> AAACGGTAbank3 ==  end => 2

        # Minimum number from startGene to endGene
        # shortest path -> BFS dijkstra algorithm
        if startGene == endGene:
            return 0
                
        # O(1) search for bank
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1

        # dijkstra
        visited = set([startGene])
        queue = deque([(startGene, 0)]) # 
        while queue:
            curr_string, curr_weight  = queue.popleft()
            for i, ch in enumerate(curr_string):
                for choice in ['A', 'C', 'G', 'T']:
                    if ch == choice:
                        continue
                    else:
                        temp_string = curr_string[:i] + choice + curr_string[i+1:]
                        if temp_string in bank_set and temp_string not in visited:
                            visited.add(temp_string)
                            if temp_string == endGene:
                                return curr_weight + 1
                            queue.append((temp_string, curr_weight+1))
        return -1