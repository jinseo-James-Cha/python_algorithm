class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        # 첫집을 안터는 경우와
        # 마지막집을 안터는 경우
        # 로 쪼개서 풀면되지!
        def rob_houses(arr):
            if len(arr) == 1:
                return arr[0]
            
            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, len(arr)):
                dp[i] = max(dp[i-1], dp[i-2] + arr[i])
            
            return dp[-1]
        return max(rob_houses(nums[:-1]), rob_houses(nums[1:]))