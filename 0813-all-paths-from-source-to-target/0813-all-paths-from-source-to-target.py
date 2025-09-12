class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # DAG - Directed Acyclic Graph
        # all path from 0 -> n-1
        # graph[i][j] -> connected
        # graph[0] -> [1, 2] -> 0node connects to 1, 2
        # graphp[1] -> [3] -> 1node connects to 3

        def dfs(node, curr,visited):
            if node  == len(graph)-1:
                res.append(curr[:])
                return 
            
            for n in graph[node]:
                if n not in visited:
                    curr.append(n)
                    visited.add(n)

                    dfs(n, curr, visited)

                    curr.pop()
                    visited.remove(n)
            
        res = []
        dfs(0, [0] ,set([0]))
        return res