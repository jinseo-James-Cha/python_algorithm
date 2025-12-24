class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # move from the leaf to Centroids..
        # if n is even num, we can have 2 centroids
        # if n is odd num, we can have 1 centroid

        # topological sort
        # leaf -> indegree remove -> center...

        # edge cases
        if n <= 2:
            return [i for i in range(n)]

        adj = defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        
        # get leaf
        leaves = []
        for node in range(n):
            if len(adj[node]) == 1:
                leaves.append(node)

        # loop until reaching centroids..
        remaining_leaves = n
        while remaining_leaves > 2:
            remaining_leaves -= len(leaves)

            new_leaves = []
            while leaves:
                leaf = leaves.pop()
                neighbor = adj[leaf].pop()
                
                adj[neighbor].remove(leaf)
                if len(adj[neighbor]) == 1:
                    new_leaves.append(neighbor)
            
            leaves = new_leaves
        return leaves
            
