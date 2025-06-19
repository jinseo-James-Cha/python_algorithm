class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # size n = len(grid)
        # 1 ~ n**2
        # ans[0] == a appears twice 
        # ans[1] == b is missing
        n = len(grid)
        ans = [0] * 2
        checked = [0] * ((n**2) + 1)
        for i in range(n):
            for num in grid[i]:
                checked[num] += 1
        
        for i in range(1, len(checked)):
            if checked[i] == 2:
                ans[0] = i
            if not checked[i]:
                ans[1] = i
        return ans
                