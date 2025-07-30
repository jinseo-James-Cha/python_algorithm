from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 1. intuition
        # 0 ~ n - 1
        # edges[i] = [ai, bi] undirected <->
        # save label with level?
        # what is the valid tree? using one directional?
        # checking b and it should be come once only

        # 2. complexity
        # time: o(n)
        # space: o(n)

        # 3. data structure
        # hashmap: ajacent_list
        # array: seen
        if len(edges) != n-1:
            return False

        def dfs(node, parent):   
            if node in seen:
                return
            seen.add(node)
            for neighbour in adjacent_list[node]:
                if neighbour == parent:
                    continue
                if neighbour in seen:
                    return False
                if not dfs(neighbour, node):
                    return False
            return True
                
        adjacent_list = defaultdict(list)
        seen = set()
        for a, b in edges:
            adjacent_list[a].append(b)
            adjacent_list[b].append(a)

        return dfs(0, -1) and len(seen) == n
        
       
            
            
