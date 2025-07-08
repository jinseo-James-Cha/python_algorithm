# 1  -> orange color
# -1 -> blue color 

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [0] * len(graph)
        # determine if each graph component is bipartite
        for i in range(len(graph)):
            if colors[i] == 0 and not self.dfs(i, 1, graph, colors):
                return False
        return True
    
    # 0, 1, graph, 0000
    def dfs(self, node: int, color: int, graph: List[List[int]], colors: List[int]) -> bool:
        colors[node] = color # colors[0] = 1
        for neighbor in graph[node]: # [1, 3]
            if colors[neighbor] == color: # neighbor should have the same color with me
                return False

            if (colors[neighbor] == 0 and not self.dfs(neighbor, -color, graph, colors)):
                return False
        return True