class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xset, yset = self.find(x), self.find(y)
        if xset == yset:
            return False
        
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
            self.rank[yset] += self.rank[xset]
        else:
            self.parent[yset] = xset
            self.rank[xset] += self.rank[yset]
        
        return True

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # Key point
        # Flatten
        # 2D matrix -> 1D
        # (num_Of_Col * curr_row) + curr_col

        n = len(grid)
        uf = UnionFind(n*n)
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def is_within_bounds(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    # flatten 2D index to 1D
                    curr = (n * row) + col
                    
                    for dr, dc in DIRS:
                        next_r, next_c = row+dr, col+dc
                        if is_within_bounds(next_r, next_c) and grid[next_r][next_c] == 1:
                            neighbor = (n*next_r) + next_c
                            uf.union(curr, neighbor)
        
        res = 0
        has_zero = False

        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    has_zero = True
                    curr_size = 1
                    unique_roots = set()
                    
                    for dr, dc in DIRS:
                        next_r, next_c = row+dr, col+dc
                        if is_within_bounds(next_r, next_c) and grid[next_r][next_c] == 1:
                            neighbor = (n * next_r) + next_c
                            root = uf.find(neighbor)
                            unique_roots.add(root)
                    
                    for root in unique_roots:
                        curr_size += uf.rank[root]
                    
                    res = max(res, curr_size)
        
        if not has_zero:
            return n * n
        return res


        """
        Question:
        - cell has 0 or 1
        - in the matrix and there are islands which are 1 and all connected.
        - return maximum size of island if I CHANGE a 0 to 1.

        => get maximum size of islands that can connect by one 0 cell in between

        Intuitive Solutions
        1. coloring the cells by its label and check 0 cells if there is any neighbor islands
        2. cell connections and size ? => Union-Find question

        1 1 0
        1 0 1
        0 1 1

        2 2 0
        2 0 3
        0 3 3

        2: 3
        3: 3
        """

        # I can color the island from 2 (0 and 1 are taken)
        n = len(grid)
        island_id = 2 
        id_size_hashmap = {}

        def is_within_bounds(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(row, col, island_id):
            grid[row][col] = island_id

            curr = 1
            for dr, dc in DIRS:
                next_row, next_col = row + dr, col + dc
                if is_within_bounds(next_row, next_col) and grid[next_row][next_col] == 1:
                    curr += dfs(next_row, next_col, island_id)
            return curr


        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    id_size_hashmap[island_id] = dfs(row, col, island_id)
                    island_id += 1
        
        res = 0
        for size in id_size_hashmap.values():
            res = max(res, size)

        # now check only 0 can have 
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    # I found 0 and check its neighbor and if it is not the same neighbor, I can add the size of id
                    added_id = set()
                    # my size as default
                    curr_size = 1

                    for dr, dc in DIRS:
                        next_r, next_c = row+dr, col+dc
                        if is_within_bounds(next_r, next_c) and grid[next_r][next_c] > 1:
                            neighbor_id = grid[next_r][next_c]
                            if neighbor_id not in added_id:
                                curr_size += id_size_hashmap[neighbor_id]
                                added_id.add(neighbor_id)
                    
                    res = max(res, curr_size)
        return res