class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        """
        2 4 6 8

        """
        values = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                values.append(grid[row][col])

        values.sort()

        n = len(values)
        median = values[n // 2]

        res = 0
        for val in values:
            if val % x != median % x:
                return -1
            
            res += abs(median - val) // x
        return res
