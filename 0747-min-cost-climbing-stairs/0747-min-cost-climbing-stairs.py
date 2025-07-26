class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # top-down, recursion + memoization
        def minimum_cost(i: int):
            if i <= 1:
                return 0
            
            if i in memo:
                return memo[i]
            
            down_one = cost[i - 1] + minimum_cost(i - 1)
            down_two = cost[i - 2] + minimum_cost(i - 2)
            memo[i] = min(down_one, down_two)
            return memo[i]


        memo = {}
        return minimum_cost(len(cost))


        # bottom-up, tabulation, iterative
        # minimum_cost = [0] * (len(cost) + 1)

        # for i in range(2, len(cost) + 1):
        #     take_one_step = minimum_cost[i-1] + cost[i - 1]
        #     take_two_step = minimum_cost[i-2] + cost[i - 2]
        #     minimum_cost[i] = min(take_one_step, take_two_step)

        # return minimum_cost[-1]


        