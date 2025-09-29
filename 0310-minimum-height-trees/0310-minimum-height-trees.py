class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # MHT: Minimum Height Tree

        # find minimum height
        # minimum height == current height: add the root
        # if minimum height > current height: reset answer with [current root]

        # who can be root?

        # a -> b
        #  [[1,0],[1,2],[1,3]]
        # 1->0,2,3 

        # b -> a
        #  [[1,0],[1,2],[1,3]]
        # 0->1 
        # 2-> 1
        # 3 -> 1

        # kahn algorithm - topological sort
        if n <= 2:
            return [i for i in range(n)]
        
        neighbors = [set() for i in range(n)]
        for a, b in edges:
            neighbors[a].add(b)
            neighbors[b].add(a)

        leaves = [] # 0, 2 , 3
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)
        
        remaining_nodes = n # 4
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves) # 4-3 = 1
            new_leaves = []

            while leaves: # 0,2,3
                leaf = leaves.pop() # 3
                neighbor = neighbors[leaf].pop() # 1
                neighbors[neighbor].remove(leaf) # 1에 있는 3을 지워
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        
        return leaves