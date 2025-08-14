class Solution:
    def rob(self, nums: List[int]) -> int:
        # 일단 서클이라는 조건을 생각하지말고 쭉 가보는거지..
        # 그렇다면 n = max(n-2 + nums[n], n-1)이라는 가정인데
        # 맨 마지막을 선택할건지 말건지...
        # nums[1:] or nums[:-1]로 판단하는건디... 어떻게 이렇게 생각해낼수 있을까...

        # bottom-up optimatization
        if len(nums) == 1:
            return nums[0]
        
        def bottom_up_opti(houses):
            prev = 0
            prev_prev = 0
            for house in houses:
                current = max(prev_prev + house, prev)
                prev_prev = prev
                prev = current
            return prev
        return max(bottom_up_opti(nums[1:]), bottom_up_opti(nums[:-1]))


        # bottom-up / tabulation
        # if len(nums) == 1:
        #     return nums[0]
        
        # def bottom_up_dp(houses):
        #     n = len(houses)
        #     if n == 1:
        #         return houses[0]

        #     dp = [0] * n
        #     dp[0] = houses[0]
        #     dp[1] = max(houses[0], houses[1])
        #     for i in range(2, n):
        #         dp[i] = max(dp[i-2]+houses[i], dp[i-1])
            
        #     return dp[-1]
        
        # return max(bottom_up_dp(nums[1:]), bottom_up_dp(nums[:-1]))




        # top-down / memoization -> TLE
        # if len(nums) == 1:
        #     return nums[0]

        # def top_down_dp(n, houses ,memo):
        #     if n == 0:
        #         return houses[0]
        #     elif n == 1:
        #         return max(houses[0], houses[1])
        #     memo[n] = max(top_down_dp(n-2, houses, memo) + houses[n], top_down_dp(n-1, houses, memo))
        #     return memo[n]
        
        return max(top_down_dp(len(nums)-2, nums[1:], {}), top_down_dp(len(nums)-2, nums[:-1], {}))


        # bottom-up / tabulation
        
