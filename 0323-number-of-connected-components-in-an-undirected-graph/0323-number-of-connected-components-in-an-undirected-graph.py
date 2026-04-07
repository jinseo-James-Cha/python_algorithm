class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            visited[node] = True
        
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        num_of_connected = 0
        visited = [False] * n
        for node in range(n):
            if not visited[node]:
                num_of_connected += 1
                dfs(node)

        return num_of_connected
