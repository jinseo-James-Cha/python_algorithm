class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:

        for g in grid:
            g.sort(reverse=True)
        
        res = 0
        for m in zip(*grid):
            res += max(m)
        return res