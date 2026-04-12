class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        n servers -> 0 ~ n-1

        undirected server to serve
        connections[i] = a <-> b

        ### Critical connection
        - a connection wil make some servers unable to reach some other server
        - if it is removed

        return all critical connections -> return all critical edges in connections.

        3 - 1
           / \
          0 - 2   
        
        if I remove an edge, the graph is disconnected?
        """
        # Low link
        graph = defaultdict(list)

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        visited_time = 0
        ids = [-1] * n          # 방문 순서
        low = [0] * n           # 가장 위로 갈 수 있는 값
        res = []

        def dfs(u, parent):
            nonlocal visited_time

            ids[u] = low[u] = visited_time
            visited_time += 1

            for v in graph[u]:
                if v == parent:
                    continue

                if ids[v] == -1:
                    dfs(v, u)

                    # 돌아오면서 low 업데이트
                    low[u] = min(low[u], low[v])

                    # 🔥 bridge 조건
                    if low[v] > ids[u]:
                        res.append([u, v])

                else:
                    # back edge
                    low[u] = min(low[u], ids[v])

        for i in range(n):
            if ids[i] == -1:
                dfs(i, -1)

        return res

        

        # brute force
        # O(E * (V+E)) -> TLE
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(start, banned_edge):
            visited = set()
            stack = [start]
            visited.add(start)

            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if (node == banned_edge[0] and neighbor == banned_edge[1]) or \
                       (node == banned_edge[1] and neighbor == banned_edge[0]):
                        continue

                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

            return len(visited)

        res = []

        for u, v in connections:
            visited_count = dfs(0, (u, v))
            if visited_count != n:
                res.append([u, v])

        return res 


