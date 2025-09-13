class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        dp = [1] * n

        for right in range(n-1):
            if ratings[right] < ratings[right+1] and dp[right] >= dp[right+1]:
                dp[right+1] = 1 + dp[right]


        for left in range(n-1, 0, -1):
            if ratings[left-1] > ratings[left] and dp[left-1] <= dp[left]:
                dp[left-1] = 1 + dp[left]
        
        return sum(dp)