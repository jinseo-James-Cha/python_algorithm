from collections import defaultdict
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for x, y in paths:
            adj[x].append(y)        
            adj[y].append(x)
        
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            used_flowers = set()
            for neighbor in adj[i]:
                if res[neighbor] != 0:
                    used_flowers.add(res[neighbor])
            
            for flower in range(1, 5):
                if flower not in used_flowers:
                    res[i] = flower
                    break
        
        return res[1:]