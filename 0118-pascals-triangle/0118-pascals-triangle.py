# make dp triangle first?

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1] * i for i in range(1, numRows+1)]
        
        # print(dp) [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1]]
        # there is rule that first and the last element are skipped cuz they must be 1
        for i in range(2, numRows): # start with the third line?
            j = 1
            while j < len(dp[i]) - 1: # i == 3 ///// 1 < 3
                left = dp[i-1][j-1] # dp[2][0]
                right = dp[i-1][j] # dp[2][1]
                dp[i][j] = left + right
                j += 1

        return dp