from collections import defaultdict, deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # MHT -> remove leaves until > 2
        # undirected

        if n <= 2:
            return [i for i in range(n)]
        
        adj_list = [set() for i in range(n)]
        for a, b in edges:
            # undirected
            adj_list[a].add(b)
            adj_list[b].add(a)
        
        # initial node -> in_degree ==1
        leaves = []
        for i in range(n):
            if len(adj_list[i]) == 1:
                leaves.append(i)
        
        remaining_leaves = n
        while remaining_leaves > 2:
            remaining_leaves -= len(leaves)

            new_leaves = []

            # all leaves take out
            while leaves:
                leaf = leaves.pop()
                neighbor = adj_list[leaf].pop()
                
                adj_list[neighbor].remove(leaf)
                if len(adj_list[neighbor]) == 1:
                    new_leaves.append(neighbor)
            
            leaves = new_leaves
        
        return leaves





