class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        maximize points
        pick nums[i] and delete it to earn nums[i] points
        delete every element equal to nums[i] - 1
        and nums[i] + 1
        """
        # 2 2 3 3 3 4
        # 2-4 , 3-9, 4-4
        
        # dp bottom up
        hashmap = defaultdict(int)
        max_number = 0
        for num in nums:
            hashmap[num] += num
            max_number = max(max_number, num)
        
        dp = [0] * (max_number + 1)
        dp[1] = hashmap[1]
        for i in range(2, max_number+1):
            dp[i] = max(dp[i-1], dp[i-2] + hashmap[i])
        return dp[-1]

        # dp top down
        hashmap = defaultdict(int)
        max_number = 0
        for num in nums:
            hashmap[num] += num
            max_number = max(max_number, num)
        

        def dp(num):
            if num == 0:
                return 0
            if num == 1:
                return hashmap[1]
            
            if num not in memo:
                memo[num] = max(dp(num-1), dp(num-2) + hashmap[num])
            return memo[num]

        memo = {}
        return dp(max_number)
