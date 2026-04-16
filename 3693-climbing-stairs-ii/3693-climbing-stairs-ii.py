class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        """
        0 ~ n
        one index array costs length n
        costs[i] = the cost of step i

        step i -> i+1, i+2, or i+3
        i to j -> costs[j] + (j-i)^2
        step 0 = 0


        0  1 2 3 4     n = 4

        minimum cost ->
        4 -> min(3, 2, 1) -> min(cost[2] + (4-3)*2, cost[1] + (4-2)^2, cost[0] + (4-1)^2)
                            -> min(3+1, 2+4, 1+9) -> 4
                            -> 2
        2 -> min(1, 0, -1) -> min(cost[0] + (2-1)*2, inf inf )
                             -> 1+ 1 -> 2
        """

        def dp(i):
            if i == 0:
                return 0
            
            if i not in memo:
                res = float('inf')
                if i >= 1:
                    res = min(res, dp(i-1) + 1**2)
                if i >= 2:
                    res = min(res, dp(i-2) + 2**2)
                if i >= 3:
                    res = min(res, dp(i-3) + 3**2)
                memo[i] = res + costs[i-1]
            
            return memo[i]
        memo = {}
        return dp(n)