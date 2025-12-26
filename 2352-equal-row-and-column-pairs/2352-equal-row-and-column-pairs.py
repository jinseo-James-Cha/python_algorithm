class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_hashmap = {}
        for row in grid:
            row_hashmap[tuple(row)] = row_hashmap.get(tuple(row), 0) + 1
        
        res = 0
        for col in zip(*grid):
            if col in row_hashmap:
                res += row_hashmap[col]
        return res