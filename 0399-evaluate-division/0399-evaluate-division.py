from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for i in range(len(equations)):
            a, b = equations[i]
            val = values[i]

            graph[a][b] = val
            graph[b][a] = 1.0 / val

        def dfs(source, target ,visited):
            if source not in graph or target not in graph:
                return -1.0
            
            if source == target:
                return 1.0
            
            visited.add(source)
            for neighbor, weight in graph[source].items():
                if neighbor not in visited:
                    result = dfs(neighbor, target, visited)
                    if result != -1.0:
                        return weight * result
            return -1.0
        
        res = []
        for a, b in queries:
            res.append(dfs(a, b, set()))
        return res
