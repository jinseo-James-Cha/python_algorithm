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
        # top down
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
