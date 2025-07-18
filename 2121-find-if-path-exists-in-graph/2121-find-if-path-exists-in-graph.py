from collections import defaultdict, deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(node: int) -> bool:
            if node == destination:
                return True
            for neighbor in adjacent_list[node]:
                if not seen[neighbor]:
                    seen[neighbor] = True
                    if dfs(neighbor):
                        return True
            return False

        adjacent_list = defaultdict(list)
        
        for u, v in edges:
            adjacent_list[u].append(v)
            adjacent_list[v].append(u)

        # # BFS
        seen = [False] * n
        seen[source] = True
        return dfs(source)



        # making adjacent list and check
        # using hashmap and num, list
        # adjacent_list = defaultdict(list)
        
        # for u, v in edges:
        #     adjacent_list[u].append(v)
        #     adjacent_list[v].append(u)

        # # # BFS
        # seen = [False] * n
        # seen[source] = True
        # queue = deque([source])

        # while queue:
        #     curr_node = queue.popleft()
        #     if curr_node == destination:
        #         return True
            
        #     for next_node in adjacent_list[curr_node]:
        #         if not seen[next_node]:
        #             seen[next_node] = True
        #             queue.append(next_node)

        # return False
