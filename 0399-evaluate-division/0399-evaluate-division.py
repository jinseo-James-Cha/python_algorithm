from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # equations[i] = Ai, Bi
        # values[i] = VALi
        # A / B = val

        # queries[j] = Cj, Dj
        # Cj / Dj  = ?
        # or -1

        # a  b = 2.0 => b a => 1 / 2.0
        # b  c = 3.0 => c b => 1/ 3.0


        # a c => a -> b -> c = 2.0 * 3.0
        # b a => b -> a = 1/ 2.0
        def dfs(src, dest, curr, visited):
            visited.add(src)
            ret = -1.0
            neighbors = graph[src]
            if dest in neighbors:
                ret = curr * neighbors[dest]
            else:
                for neighbor, value in neighbors.items():
                    if neighbor in visited:
                        continue
                    ret = dfs(neighbor, dest, curr * value, visited)
                    if ret != -1.0:
                        break
            visited.remove(src)
            return ret

        graph = defaultdict(dict)
        for i, (a, b) in enumerate(equations):
            graph[a][b] = values[i]
            graph[b][a] = 1 / values[i]
        
        res = []
        for c, d in queries:
            if c not in graph or d not in graph:
                res.append(-1.0)
            elif c == d:
                res.append(1.0)
            else:
                res.append(dfs(c, d, 1.0, set()))
        return res