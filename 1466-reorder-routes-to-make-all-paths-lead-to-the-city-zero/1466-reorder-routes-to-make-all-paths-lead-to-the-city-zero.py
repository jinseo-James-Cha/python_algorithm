from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        only one way directed?
        a -> b

        leaf -> destination..-> topological sort?
        or just dfs?
        
        
        0 -> other cities?
        or leaves -> 0 and then count if it is not the path ?

        return minimum number....        
        """

        def dfs(city):
            nonlocal minimum_changed_edges
            visited[city] = True

            for neighbor in adj_list[city]:
                if not visited[neighbor]:
                    if (city, neighbor) in routes:
                        minimum_changed_edges += 1
                    dfs(neighbor)
                

        routes = set()
        for c in connections:
            routes.add(tuple(c))
        
        # later, if a route is not here, that means it needs to reorder the route so +1
        adj_list = defaultdict(set)
        for a, b in connections:
            adj_list[a].add(b)
            adj_list[b].add(a)

        minimum_changed_edges = 0
        visited = [False] * n
        dfs(0)
        return minimum_changed_edges
